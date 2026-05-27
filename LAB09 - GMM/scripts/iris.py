import numpy as np
import os
import sys

from pathlib import Path
from GMMmodel.gmm_core import logpdf_GMM, apply_eigenvalue_constraint
from GMMmodel.gmm_em import EM_algorithm, EM_algorithm_diag, EM_algorithm_tied
from GMMmodel.gmm_lbg import LBG_algorithm, LBG_algorithm_diag, LBG_algorithm_tied
from utils.data_loaders import load_dataset, split_dataset, save_gmm, load_gmm  
from utils.bayes_utils import compute_normalised_empirical_Bayes_risk_binary, compute_min_dcf
from utils.plot_utils import *


if __name__ == "__main__":
    # --- SETUP & DATA LOADING ---
    ROOT = Path(".")
    dataset_dir = ROOT / "data" / "iris"
    output_dir = ROOT / "results" / "iris"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "iris_gmm_results.txt"

    iris_data_path = dataset_dir / "iris_dataset.csv"
    data_path = dataset_dir / "GMM_data_4D.npy"
    gmm_path = dataset_dir / "GMM_4D_3G_init.json"
    ref_ll_path = dataset_dir / "GMM_4D_3G_init_ll.npy"
    lbg_path = dataset_dir / "GMM_4D_4G_EM_LBG.json"


    # ===========================
    # 1. GMM LOG-DENSITY
    # ===========================
    print("=== GMM LOG-DENSITY TEST ===")

    # Load the dataset X
    X = np.load(data_path)

    # Load the initial GMM model
    gmm = load_gmm(gmm_path)

    # Compute the log-likelihoods
    computed_ll = logpdf_GMM(X, gmm)
    avg_ll = np.mean(computed_ll)

    # Compare the results
    reference_ll = np.load(ref_ll_path)
    expected_avg_ll = np.mean(reference_ll)
    is_correct = np.allclose(computed_ll, reference_ll)
    
    print(f"Computed Average Log-Likelihood: {avg_ll:.8f}")
    print(f"Expected Average Log-Likelihood: {expected_avg_ll:.8f}")

    if is_correct:
        print("\n✅ SUCCESS: Your computed log-densities match the reference exactly!")
    else:
        print("\n❌ ERROR: Your computed log-densities DO NOT match the reference.")


    # ===========================
    # 2. EM ALGORITHM
    # ===========================
    print("=== EM ALGORITHM ===")

    # Reload the initial GMM to ensure a clean state (since EM modifies it in-place)
    gmm_init = load_gmm(gmm_path)
    
    # Run the EM algorithm
    # Note: delta_l defaults to 1e-6 as specified in the lab text
    trained_gmm = EM_algorithm(X, gmm_init)
    
    # Compute the final average log-likelihood to check correctness
    final_marginals = logpdf_GMM(X, trained_gmm)
    final_avg_ll = np.mean(final_marginals)
    
    # The reference value provided in the laboratory text
    expected_avg_ll = -7.26325603
    
    print(f"Computed Average Log-Likelihood: {final_avg_ll:.8f}")
    print(f"Expected Average Log-Likelihood: {expected_avg_ll:.8f}")
    
    # Check if the computed value is close to the expected value
    if np.isclose(final_avg_ll, expected_avg_ll, atol=1e-6):
        print("✅ SUCCESS: The EM algorithm converged to the correct log-likelihood!")
    else:
        print("❌ ERROR: The EM algorithm did not reach the expected log-likelihood.")

    
    # ===================================
    # 3. EM ALGORITHM AFTER LBG SPLITTING
    # ===================================
    print("=== EM ALGORITHM AFTER LBG SPLITTING ===")

    # 1. Start with a 1-component GMM using the empirical mean and covariance of the dataset
    # We use keepdims=True to ensure mu has shape (D, 1)
    mu_global = np.mean(X, axis=1, keepdims=True)
    # We use bias=True to compute the ML estimate (dividing by N instead of N-1)
    C_global = np.cov(X, bias=True) 
    
    gmm_1 = [(1.0, mu_global, C_global)]

    # 2. Split to 2 components and run EM
    gmm_2 = LBG_algorithm(gmm_1)
    gmm_2_trained = EM_algorithm(X, gmm_2)

    # 3. Split to 4 components and run EM
    gmm_4 = LBG_algorithm(gmm_2_trained)
    trained_gmm_lbg = EM_algorithm(X, gmm_4)

    # Compute the final average log-likelihood for the 4-component LBG-initialized GMM
    final_marginals_lbg = logpdf_GMM(X, trained_gmm_lbg)
    final_avg_ll_lbg = np.mean(final_marginals_lbg)

    expected_avg_ll_lbg = -7.25337844

    print(f"Final Average Log-Likelihood (LBG 4-Comp): {final_avg_ll_lbg:.8f}")
    print(f"Expected Average Log-Likelihood: {expected_avg_ll_lbg:.8f}")

    # Check if the computed value is close to the expected value
    if np.isclose(final_avg_ll_lbg, expected_avg_ll_lbg, atol=1e-6):
        print("✅ SUCCESS: The EM algorithm after LBG splitting converged to the correct log-likelihood!")
    else:
        print("❌ ERROR: The EM algorithm after LBG splitting did not reach the expected log-likelihood.")

    
    # ====================================================
    # 4. DIAGONAL AND TIED GMM VARIANTS
    # ====================================================
    print("=== DIAGONAL AND TIED GMM ===")
    
    # The minimum eigenvalue constraint recommended by the lab text
    psi_val = 0.01 
    
    # Re-compute global statistics just in case
    mu_global = np.mean(X, axis=1, keepdims=True)
    C_global = np.cov(X, bias=True) 

    # --- DIAGONAL GMM (Targeting 4 Components) ---
    
    # 1. Start with 1-component GMM (ensure diagonal constraint is applied initially)
    C_global_diag = C_global * np.eye(C_global.shape[0])
    C_global_diag = apply_eigenvalue_constraint(C_global_diag, psi=psi_val)
    gmm_diag_1 = [(1.0, mu_global, C_global_diag)]

    # 2. LBG Split to 2, then train
    gmm_diag_2 = LBG_algorithm_diag(gmm_diag_1, alpha=0.1, psi=psi_val)
    trained_diag_2 = EM_algorithm_diag(X, gmm_diag_2, psi=psi_val)

    # 3. LBG Split to 4, then train
    gmm_diag_4 = LBG_algorithm_diag(trained_diag_2, alpha=0.1, psi=psi_val)
    trained_diag_4 = EM_algorithm_diag(X, gmm_diag_4, psi=psi_val)

    final_ll_diag = np.mean(logpdf_GMM(X, trained_diag_4))
    print(f"Final Average Log-Likelihood (Diagonal 4-Comp): {final_ll_diag:.8f}")


    # --- TIED GMM (Targeting 4 Components) ---
    print("\n--- Training Tied GMM (4 Components) ---")
    
    # 1. Start with 1-component GMM (Tied 1-component is just the standard MVG)
    C_global_tied = apply_eigenvalue_constraint(C_global, psi=psi_val)
    gmm_tied_1 = [(1.0, mu_global, C_global_tied)]

    # 2. LBG Split to 2, then train
    gmm_tied_2 = LBG_algorithm_tied(gmm_tied_1, alpha=0.1, psi=psi_val)
    trained_tied_2 = EM_algorithm_tied(X, gmm_tied_2, psi=psi_val)

    # 3. LBG Split to 4, then train
    gmm_tied_4 = LBG_algorithm_tied(trained_tied_2, alpha=0.1, psi=psi_val)
    trained_tied_4 = EM_algorithm_tied(X, gmm_tied_4, psi=psi_val)

    final_ll_tied = np.mean(logpdf_GMM(X, trained_tied_4))
    print(f"Final Average Log-Likelihood (Tied 4-Comp): {final_ll_tied:.8f}")


    # =========================
    # 5. GMM FOR CLASSIFICATION
    # =========================

    # Helper mapping to keep loops clean
    algorithms = {
        'full': (LBG_algorithm, EM_algorithm),
        'diag': (LBG_algorithm_diag, EM_algorithm_diag),
        'tied': (LBG_algorithm_tied, EM_algorithm_tied)
    }
    
    target_components = [1, 2, 4, 8, 16]
    cov_types = ['full', 'diag', 'tied']
    psi_val = 0.01

    # ---------------------------------------------------------
    # 5.1 GMM FOR CLASSIFICATION (MULTICLASS CASE)
    # ---------------------------------------------------------
    print("\nTraining Multiclass GMMs...")

    D_multi, L_multi = load_dataset(iris_data_path)
    (DTR_m, LTR_m), (DTE_m, LTE_m) = split_dataset(D_multi, L_multi, percTrain=2/3)
    classes_multi = np.unique(LTR_m)

    results_multi = {ct: {} for ct in cov_types}

    for cov_type in cov_types:
        LBG_fn, EM_fn = algorithms[cov_type]
        current_gmms = {}
        
        # Initialize 1-component GMMs
        for cls in classes_multi:
            DTR_cls = DTR_m[:, LTR_m == cls]
            mu_cls = np.mean(DTR_cls, axis=1, keepdims=True)
            C_cls = np.cov(DTR_cls, bias=True)
            
            if cov_type == 'diag':
                C_cls = C_cls * np.eye(C_cls.shape[0])
            
            C_cls = apply_eigenvalue_constraint(C_cls, psi_val)
            current_gmms[cls] = [(1.0, mu_cls, C_cls)]
            
            if cov_type != 'full': 
                current_gmms[cls] = EM_fn(DTR_cls, current_gmms[cls], psi=psi_val)
                
        # Iteratively split, train, and evaluate
        comp_count = 1
        while comp_count <= 16:
            if comp_count in target_components:
                # Evaluate current state
                log_likelihoods = np.zeros((len(classes_multi), DTE_m.shape[1]))
                for idx, cls in enumerate(classes_multi):
                    log_likelihoods[idx, :] = logpdf_GMM(DTE_m, current_gmms[cls])
                
                predicted = np.argmax(log_likelihoods, axis=0)
                error_rate = 1 - np.mean(predicted == LTE_m)
                results_multi[cov_type][comp_count] = error_rate * 100

            # Split and retrain
            if comp_count < 16:
                for cls in classes_multi:
                    DTR_cls = DTR_m[:, LTR_m == cls]
                    
                    split_gmm = LBG_fn(current_gmms[cls], alpha=0.1, psi=psi_val)
                    current_gmms[cls] = EM_fn(DTR_cls, split_gmm, psi=psi_val)
            
            comp_count *= 2

    # Output the Multiclass Table using our new utility function
    print_multiclass_table(results_multi, target_components, cov_types)


    # ---------------------------------------------------------
    # 5.2 GMM FOR CLASSIFICATION (BINARY CASE)
    # ---------------------------------------------------------
    print("\nTraining Binary GMMs...")

    binary_data_path = dataset_dir / "ext_data_binary.npy"
    binary_labels_path = dataset_dir / "ext_data_binary_labels.npy"
    
    D_bin = np.load(binary_data_path)
    L_bin = np.load(binary_labels_path)
    (DTR_b, LTR_b), (DTE_b, LTE_b) = split_dataset(D_bin, L_bin, percTrain=2/3)
    
    results_bin = {ct: {} for ct in cov_types}

    for cov_type in cov_types:
        LBG_fn, EM_fn = algorithms[cov_type]
        current_gmms = {}
        
        # Initialize 1-component GMMs
        for cls in [0, 1]:
            DTR_cls = DTR_b[:, LTR_b == cls]
            mu_cls = np.mean(DTR_cls, axis=1, keepdims=True)
            C_cls = np.cov(DTR_cls, bias=True)
            
            if cov_type == 'diag':
                C_cls = C_cls * np.eye(C_cls.shape[0])
            
            C_cls = apply_eigenvalue_constraint(C_cls, psi_val)
            current_gmms[cls] = [(1.0, mu_cls, C_cls)]
            
            if cov_type != 'full':
                current_gmms[cls] = EM_fn(DTR_cls, current_gmms[cls], psi=psi_val)
                
        # Iteratively split, train, and evaluate
        comp_count = 1
        while comp_count <= 16:
            if comp_count in target_components:
                # Evaluate current state using LLR
                log_pdf_1 = logpdf_GMM(DTE_b, current_gmms[1])
                log_pdf_0 = logpdf_GMM(DTE_b, current_gmms[0])
                llr = log_pdf_1 - log_pdf_0 
                
                # Parameters for the application
                pi1, Cfn, Cfp = 0.5, 1, 1
                
                # Compute minDCF (sweeps all thresholds)
                min_dcf = compute_min_dcf(llr, LTE_b, pi1, Cfn, Cfp)
                
                # Compute actDCF (requires theoretical threshold to build confusion matrix)
                threshold = -np.log((pi1 * Cfn) / ((1 - pi1) * Cfp))
                predictions = (llr > threshold).astype(int)
                
                # Build the 2x2 confusion matrix M
                M = np.zeros((2, 2))
                M[0, 0] = np.sum((predictions == 0) & (LTE_b == 0)) # True Negatives
                M[0, 1] = np.sum((predictions == 0) & (LTE_b == 1)) # False Negatives
                M[1, 0] = np.sum((predictions == 1) & (LTE_b == 0)) # False Positives
                M[1, 1] = np.sum((predictions == 1) & (LTE_b == 1)) # True Positives
                
                # Now we pass M, not llr!
                act_dcf = compute_normalised_empirical_Bayes_risk_binary(M, pi1, Cfn, Cfp)
                
                results_bin[cov_type][comp_count] = (min_dcf, act_dcf)

            # Split and retrain
            if comp_count < 16:
                for cls in [0, 1]:
                    DTR_cls = DTR_b[:, LTR_b == cls]
                    
                    split_gmm = LBG_fn(current_gmms[cls], alpha=0.1, psi=psi_val)
                    current_gmms[cls] = EM_fn(DTR_cls, split_gmm, psi=psi_val)
            
            comp_count *= 2

    # Output the Binary Table using our new utility function
    print_binary_table(results_bin, target_components, cov_types)