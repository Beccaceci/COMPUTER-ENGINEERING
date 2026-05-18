import matplotlib.pyplot as plt

def plot_dcf_vs_c(C_values, min_dcf_list, act_dcf_list, title, save_path):
    """Plots minDCF and actDCF vs C on a logarithmic scale."""
    plt.figure(figsize=(8, 6))
    plt.plot(C_values, min_dcf_list, label='minDCF', marker='o', color='blue')
    plt.plot(C_values, act_dcf_list, label='actDCF', marker='x', color='red')
    plt.xscale('log')
    plt.xlabel('C (Regularization)')
    plt.ylabel('DCF')
    plt.title(title)
    plt.legend()
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
    print(f"Saved plot to: {save_path}")

def plot_rbf_dcfs_vs_c(C_values, min_dcfs_dict, act_dcfs_dict, title, save_path):
    """Plots minDCF and actDCF vs C for multiple gamma values on a logarithmic scale."""
    plt.figure(figsize=(10, 6))
    
    # Colors to differentiate gamma values
    colors = ['blue', 'red', 'green', 'orange', 'purple']
    
    for idx, gamma in enumerate(min_dcfs_dict.keys()):
        color = colors[idx % len(colors)]
        # Use solid lines for minDCF and dashed lines for actDCF
        plt.plot(C_values, min_dcfs_dict[gamma], label=rf'minDCF ($\gamma$={gamma})', color=color, linestyle='-', marker='o')
        plt.plot(C_values, act_dcfs_dict[gamma], label=rf'actDCF ($\gamma$={gamma})', color=color, linestyle='--', marker='x')
        
    plt.xscale('log')
    plt.xlabel('C (Regularization)')
    plt.ylabel('DCF')
    plt.title(title)
    
    # Place legend outside the plot to avoid overlapping lines
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
    print(f"Saved plot to: {save_path}")