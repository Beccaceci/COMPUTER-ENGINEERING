import numpy
from pathlib import Path

from utils.data_loaders import load_dataset, split_dataset
from utils.bayes_utils import compute_optimal_bayes_binary, compute_normalised_empirical_Bayes_risk_binary, compute_min_dcf
from utils.math_utils import compute_confusion_matrix
from utils.plot_utils import plot_bayes_error

from models.MVG import compute_mvg_loglikelihoods
from models.TiedMVG import compute_tied_mvg_loglikelihoods
from models.NaiveBayes import compute_naive_bayes_loglikelihoods


if __name__ == "__main__":
    ROOT = Path(".")
    
    # Define output directory and file
    results_dir = ROOT / "results" / "project"
    results_dir.mkdir(parents=True, exist_ok=True)
    output_file = results_dir / "lab06_project_evaluation.txt"
    
    # Helper to print and save simultaneously
    output_lines = []
    def emit(text=""):
        print(text)
        output_lines.append(text)

    # 1. Load the Project Dataset
    D, L = load_dataset(ROOT / "data" / "project" / "trainData.txt")
    (DTR, LTR), (DTE, LTE) = split_dataset(D, L, percTrain=2.0 / 3.0)

    # =========================================================================
    # PART 1: EVALUATION ON GIVEN APPLICATIONS (0.1, 0.5, 0.9) WITH UNIT COSTS
    # =========================================================================
    
    # 2. Get the Class-Conditional Log-Likelihoods for all 3 models
    emit("Training models and computing log-likelihoods...")
    S_log_mvg = compute_mvg_loglikelihoods(DTR, LTR, DTE)
    S_log_tied = compute_tied_mvg_loglikelihoods(DTR, LTR, DTE)
    S_log_nb = compute_naive_bayes_loglikelihoods(DTR, LTR, DTE)
    
    # 3. Convert to Binary Log-Likelihood Ratios (LLR = log(f|1) - log(f|0))
    llr_mvg = S_log_mvg[1, :] - S_log_mvg[0, :]
    llr_tied = S_log_tied[1, :] - S_log_tied[0, :]
    llr_nb = S_log_nb[1, :] - S_log_nb[0, :]
    
    models = {
        "Standard MVG": llr_mvg,
        "Naive Bayes": llr_nb,
        "Tied MVG": llr_tied
    }
    
    # 4. Define the 5 applications from the lab text
    applications = [
        (0.5, 1.0, 1.0),
        (0.9, 1.0, 1.0),
        (0.1, 1.0, 1.0),
        (0.5, 1.0, 9.0),
        (0.5, 9.0, 1.0)
    ]
    
    # 5. Evaluate
    emit("\n=========================================================================")
    emit("--- PROJECT EVALUATION: ACTUAL DCF AND MIN DCF ---")
    emit("=========================================================================")
    
    for pi1, Cfn, Cfp in applications:
        # Calculate Effective Prior to show the theoretical link
        pi_tilde = (pi1 * Cfn) / (pi1 * Cfn + (1 - pi1) * Cfp)
        
        emit(f"\nApplication: (pi1={pi1}, Cfn={Cfn}, Cfp={Cfp}) ---> Effective Prior: {pi_tilde:.2f}")
        emit("-" * 65)
        emit(f"{'Model Name':<18} | {'Actual DCF_n':^15} | {'Min DCF':^15}")
        emit("-" * 65)
        
        for name, llr in models.items():
            # A. Get optimal predictions
            pred = compute_optimal_bayes_binary(llr, pi1, Cfn, Cfp)
            
            # B. Compute confusion matrix
            M = compute_confusion_matrix(pred, LTE, num_classes=2)
            
            # C. Compute normalized DCF and Min DCF
            DCF_n = compute_normalised_empirical_Bayes_risk_binary(M, pi1, Cfn, Cfp)
            min_DCF = compute_min_dcf(llr, LTE, pi1, Cfn, Cfp)
            
            # Record row
            emit(f"{name:<18} | {DCF_n:^15.3f} | {min_DCF:^15.3f}")

    # 6. Save accumulated lines to file
    with open(output_file, "w") as f:
        f.write("\n".join(output_lines))
        
    print(f"\n[SUCCESS] Results successfully saved to {output_file}")

    # =========================================================================
    # PART 2: EVALUATION ON EFFECTIVE PRIORS (0.1, 0.5, 0.9)
    # =========================================================================
    
    # Define the 3 effective prior applications with unit costs
    eff_applications = [
        (0.1, 1.0, 1.0),
        (0.5, 1.0, 1.0),
        (0.9, 1.0, 1.0)
    ]
    
    emit("\n\n=========================================================================")
    emit("--- EFFECTIVE PRIORS EVALUATION AND BAYES ERROR PLOTS ---")
    emit("=========================================================================")
    
    for pi_tilde, Cfn, Cfp in eff_applications:
        emit(f"\nApplication: pi_tilde={pi_tilde:.1f} (Cfn=1, Cfp=1)")
        emit("-" * 65)
        emit(f"{'Model Name':<18} | {'Actual DCF_n':^15} | {'Min DCF':^15}")
        emit("-" * 65)
        
        for name, llr in models.items():
            # Compute optimal decisions
            pred = compute_optimal_bayes_binary(llr, pi_tilde, Cfn, Cfp)
            M = compute_confusion_matrix(pred, LTE, num_classes=2)
            
            # Compute actual DCF and minimum DCF
            DCF_n = compute_normalised_empirical_Bayes_risk_binary(M, pi_tilde, Cfn, Cfp)
            min_DCF = compute_min_dcf(llr, LTE, pi_tilde, Cfn, Cfp)
            
            emit(f"{name:<18} | {DCF_n:^15.3f} | {min_DCF:^15.3f}")


    # =========================================================================
    # PART 3: BAYES ERROR PLOTS
    # =========================================================================
    emit("\nGenerating Bayes Error plots for MVG, Tied, and Naive Bayes...")
    
    # Sweep prior log odds in the range (-4, +4)
    effPriorLogOdds = numpy.linspace(-4, 4, 21)
    pi_array = 1 / (1 + numpy.exp(-effPriorLogOdds))
    
    for name, llr in models.items():
        dcf_values = []
        min_dcf_values = []
        
        for pi_tilde in pi_array:
            pred = compute_optimal_bayes_binary(llr, pi_tilde, 1.0, 1.0)
            M = compute_confusion_matrix(pred, LTE, num_classes=2)
            
            # For each model, gather both minimum and actual DCF
            dcf_values.append(compute_normalised_empirical_Bayes_risk_binary(M, pi_tilde, 1.0, 1.0))
            min_dcf_values.append(compute_min_dcf(llr, LTE, pi_tilde, 1.0, 1.0))
            
        # Format filename to avoid spaces
        safe_name = name.replace(" ", "_")
        plot_path = results_dir / f"Bayes_Error_{safe_name}.png"
        
        # Plot the Bayes error plot for the specific classifier
        plot_bayes_error(effPriorLogOdds, dcf_values, min_dcf_values, plot_path, xlim=[-4, 4], ylim=[0, 1.1])
        
        emit(f"Saved Bayes Error Plot for {name} -> {plot_path.name}")