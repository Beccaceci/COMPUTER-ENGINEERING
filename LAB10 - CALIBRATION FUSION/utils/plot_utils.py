import numpy as np
import matplotlib.pyplot as plt

def print_multiclass_table(results_multi, target_components, cov_types):
    """
    Prints the classification error rates for the Multiclass GMM models.
    """
    titles = {'full': 'Full Covariance', 'diag': 'Diagonal Covariance', 'tied': 'Tied Covariance'}
    
    print("\n" + "="*70)
    print(f"{'GMM Type (Multiclass)':<25} | {'1':<6} | {'2':<6} | {'4':<6} | {'8':<6} | {'16':<6}")
    print("-" * 70)
    
    for ct in cov_types:
        row = f"{titles[ct]:<25} | "
        row += " | ".join([f"{results_multi[ct][c]:>5.1f}%" for c in target_components])
        print(row)
        
    print("="*70)

def print_binary_table(results_bin, target_components, cov_types):
    """
    Prints the minDCF and actDCF for the Binary GMM models.
    """
    titles = {'full': 'Full Covariance', 'diag': 'Diagonal Covariance', 'tied': 'Tied Covariance'}
    
    print("\n" + "="*85)
    print(f"{'GMM Type (Binary)':<20} | {'1':<10} | {'2':<10} | {'4':<10} | {'8':<10} | {'16':<10}")
    print("-" * 85)
    
    for ct in cov_types:
        row = f"{titles[ct]:<20} | "
        row += " | ".join([f"{results_bin[ct][c][0]:.4f}/{results_bin[ct][c][1]:.4f}" for c in target_components])
        print(row)
        
    print("="*85)

def plot_bayes_error(eff_prior_log_odds, min_dcf_list, act_dcf_list, title="Bayes Error Plot", save_path=None):
    """
    Generates a Bayes Error plot (minDCF and actDCF over varying priors).
    Required for the final Project section of the laboratory.
    """
    plt.figure(figsize=(8, 6))
    plt.plot(eff_prior_log_odds, act_dcf_list, label='Actual DCF', color='red', linewidth=2)
    plt.plot(eff_prior_log_odds, min_dcf_list, label='Minimum DCF', color='blue', linestyle='--', linewidth=2)
    plt.xlim([min(eff_prior_log_odds), max(eff_prior_log_odds)])
    plt.ylim([0, 1.1])
    plt.xlabel('Prior Log-Odds')
    plt.ylabel('DCF Value')
    plt.title(title)
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.tight_layout()
    
    # Save the plot if a path is provided
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to: {save_path}")
        
    # plt.show()
    plt.close() # Closes the figure to free up memory

def plot_bayes_errors_multi(eff_prior_log_odds, results_dict, title, save_path):
    """
    Plots minDCF and actDCF curves for multiple models.
    
    Args:
        eff_prior_log_odds: Array of prior log-odds (x-axis).
        results_dict: Dictionary containing results for each model.
                      Format: {model_name: {'min_dcf': array, 'act_dcf': array, 'style': string}}
        title: Plot title.
        save_path: Path to save the plot figure.
    """
    plt.figure(figsize=(8, 6))
    for label, res in results_dict.items():
        if res.get('min_dcf') is not None:
            plt.plot(eff_prior_log_odds, res['min_dcf'], label=f"minDCF ({label})", linestyle='--')
        if res.get('act_dcf') is not None:
            plt.plot(eff_prior_log_odds, res['act_dcf'], label=f"actDCF ({label})", linestyle=res.get('style', '-'))
            
    plt.xlim([min(eff_prior_log_odds), max(eff_prior_log_odds)])
    plt.ylim([0, 1.2])
    plt.xlabel('prior log-odds')
    plt.ylabel('normalized DCF')
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()