import numpy as np
import contextlib
from pathlib import Path

from utils.data_loaders import load_dataset, split_dataset
from GMMmodel.gmm_core import logpdf_GMM, apply_eigenvalue_constraint
from GMMmodel.gmm_em import EM_algorithm, EM_algorithm_diag, EM_algorithm_tied
from GMMmodel.gmm_lbg import LBG_algorithm, LBG_algorithm_diag, LBG_algorithm_tied
from utils.bayes_utils import compute_min_dcf, compute_normalised_empirical_Bayes_risk_binary
from utils.plot_utils import print_binary_table, plot_bayes_error

if __name__ == "__main__":
    # --- SETUP & DIRECTORIES ---
    ROOT = Path(".")
    dataset_dir = ROOT / "data" / "project"
    
    # Setup Metrics Directory
    metrics_dir = ROOT / "results" / "project"
    metrics_dir.mkdir(parents=True, exist_ok=True)
    metrics_path = metrics_dir / "project_gmm_results.txt"
    
    # Setup Plots Directory
    plots_dir = metrics_dir / "plots"
    plots_dir.mkdir(parents=True, exist_ok=True)

    print("Loading and splitting project dataset...")
    project_data_path = dataset_dir / "trainData.txt"
    D, L = load_dataset(project_data_path)
    (DTR, LTR), (DTE, LTE) = split_dataset(D, L, percTrain=2.0/3.0)

    # --- CONFIGURATION ---
    algorithms = {
        'full': (LBG_algorithm, EM_algorithm),
        'diag': (LBG_algorithm_diag, EM_algorithm_diag),
        'tied': (LBG_algorithm_tied, EM_algorithm_tied)
    }
    target_components = [1, 2, 4, 8, 16]
    cov_types = ['full', 'diag', 'tied']
    psi_val = 0.01
    
    results = {ct: {} for ct in cov_types}
    
    # *** IMPORTANT ***
    # Update these numbers based on the lowest minDCF from your previous runs!
    # This selects which model to plot for each variant.
    selected_components = {
        'full': 8,   
        'diag': 16,  
        'tied': 8    
    }
    llrs_to_plot = {} # Will store the LLRs for the selected models

    # --- EVALUATION LOOP ---
    print("\nTraining GMM Variants (This may take a moment)...")

    for cov_type in cov_types:
        LBG_fn, EM_fn = algorithms[cov_type]
        current_gmms = {}

        # 1. Initialize 1-component GMMs
        for cls in [0, 1]:
            DTR_cls = DTR[:, LTR == cls]
            mu_cls = np.mean(DTR_cls, axis=1, keepdims=True)
            C_cls = np.cov(DTR_cls, bias=True) 
            
            if cov_type == 'diag':
                C_cls = C_cls * np.eye(C_cls.shape[0])
            
            C_cls = apply_eigenvalue_constraint(C_cls, psi_val)
            current_gmms[cls] = [(1.0, mu_cls, C_cls)]
            
            if cov_type != 'full':
                current_gmms[cls] = EM_fn(DTR_cls, current_gmms[cls], psi=psi_val)

        # 2. Iteratively split, train, and evaluate
        comp_count = 1
        while comp_count <= 16:
            if comp_count in target_components:
                log_pdf_1 = logpdf_GMM(DTE, current_gmms[1])
                log_pdf_0 = logpdf_GMM(DTE, current_gmms[0])
                llr = log_pdf_1 - log_pdf_0

                pi1, Cfn, Cfp = 0.5, 1, 1
                min_dcf = compute_min_dcf(llr, LTE, pi1, Cfn, Cfp)

                threshold = -np.log((pi1 * Cfn) / ((1 - pi1) * Cfp))
                predictions = (llr > threshold).astype(int)
                
                M = np.zeros((2, 2))
                M[0, 0] = np.sum((predictions == 0) & (LTE == 0)) 
                M[0, 1] = np.sum((predictions == 0) & (LTE == 1)) 
                M[1, 0] = np.sum((predictions == 1) & (LTE == 0)) 
                M[1, 1] = np.sum((predictions == 1) & (LTE == 1)) 
                
                act_dcf = compute_normalised_empirical_Bayes_risk_binary(M, pi1, Cfn, Cfp)
                results[cov_type][comp_count] = (min_dcf, act_dcf)
                
                # Save the LLR scores if this matches our "best" selected component count
                if comp_count == selected_components[cov_type]:
                    llrs_to_plot[cov_type] = llr.copy()

            # Split and retrain
            if comp_count < 16:
                for cls in [0, 1]:
                    DTR_cls = DTR[:, LTR == cls]
                    split_gmm = LBG_fn(current_gmms[cls], alpha=0.1, psi=psi_val)
                    current_gmms[cls] = EM_fn(DTR_cls, split_gmm, psi=psi_val)
            
            comp_count *= 2

    # --- REPORTING (METRICS) ---
    print(f"\nWriting results table to {metrics_path}...")
    
    # 1. Print to Terminal
    print_binary_table(results, target_components, cov_types)
    
    # 2. Write to File using contextlib to redirect stdout
    with open(metrics_path, "w") as f:
        with contextlib.redirect_stdout(f):
            print("Project Dataset GMM Results:")
            print_binary_table(results, target_components, cov_types)

    
    # --- BAYES ERROR PLOTS ---
    print("\nGenerating Bayes Error Plots...")
    
    # Define the range of prior log-odds from -4 to +4
    eff_prior_log_odds = np.linspace(-4, 4, 21)
    pi_eff_array = 1 / (1 + np.exp(-eff_prior_log_odds))
    
    # For each selected model, compute the minDCF and actDCF across the range of effective priors and plot the results
    for cov_type, best_llr in llrs_to_plot.items():
        comp = selected_components[cov_type]
        min_dcf_list = []
        act_dcf_list = []
        
        # Compute minDCF and actDCF for each effective prior
        for pi in pi_eff_array:
            # Recompute minDCF and actDCF for the current effective prior
            m_dcf = compute_min_dcf(best_llr, LTE, pi, 1, 1)
            thresh = -np.log(pi / (1 - pi))
            preds = (best_llr > thresh).astype(int)
            
            M = np.zeros((2, 2))
            M[0, 0] = np.sum((preds == 0) & (LTE == 0))
            M[0, 1] = np.sum((preds == 0) & (LTE == 1))
            M[1, 0] = np.sum((preds == 1) & (LTE == 0))
            M[1, 1] = np.sum((preds == 1) & (LTE == 1))
            a_dcf = compute_normalised_empirical_Bayes_risk_binary(M, pi, 1, 1)
            
            min_dcf_list.append(m_dcf)
            act_dcf_list.append(a_dcf)
            
        plot_filename = plots_dir / f"bayes_error_{cov_type}_{comp}comp.png"
        
        plot_bayes_error(
            eff_prior_log_odds, 
            min_dcf_list, 
            act_dcf_list, 
            title=f"Bayes Error Plot: {cov_type.capitalize()} GMM ({comp} Comp)",
            save_path=plot_filename
        )
        
    print("Project analysis complete!")