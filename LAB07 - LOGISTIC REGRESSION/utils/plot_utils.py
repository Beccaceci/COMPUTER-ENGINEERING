import matplotlib.pyplot as plt

def plot_dcf_vs_lambda(lambdas, act_dcfs, min_dcfs, output_path):
    """
    Plots the Actual DCF and Minimum DCF against lambda values.
    """
    plt.figure(figsize=(8, 6))
    plt.plot(lambdas, act_dcfs, label='Actual DCF', color='r', linewidth=2)
    plt.plot(lambdas, min_dcfs, label='Minimum DCF', color='b', linewidth=2)
    
    # Use logarithmic scale for the x-axis
    plt.xscale('log', base=10)
    
    plt.xlabel('Lambda')
    plt.ylabel('DCF')
    plt.title('Standard Logistic Regression: DCF vs Lambda')
    plt.legend()
    plt.grid(True, which="both", ls="--", alpha=0.5)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()