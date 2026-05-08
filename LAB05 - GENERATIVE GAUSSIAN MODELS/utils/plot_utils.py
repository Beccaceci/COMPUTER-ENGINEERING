import os
import numpy
import matplotlib.pyplot as plt

def plot_histograms(DTR, LTR, output_dir):
    """
    Plots the normalized histograms and theoretical Gaussian PDFs 
    using side-by-side subplots and saves them to a dedicated folder.
    """
    # Create the target directory if it doesn't already exist
    os.makedirs(output_dir, exist_ok=True)
    
    num_features = DTR.shape[0]
    classes = numpy.unique(LTR)
    
    # We will use distinct colors for the two classes
    colors = {classes[0]: 'blue', classes[1]: 'red'}
    
    for i in range(num_features):
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        fig.suptitle(f'Gaussian Assumption Evaluation - Feature {i+1}', fontsize=14, fontweight='bold')
        
        for idx, c in enumerate(classes):
            X_c = DTR[i, LTR == c]
            ax = axes[idx] 
            
            # Plot the normalized histogram
            ax.hist(X_c, bins=30, density=True, alpha=0.6, color=colors[c], edgecolor='black')
            
            # Calculate ML mean and variance
            mu = numpy.mean(X_c)
            var = numpy.var(X_c)
            std = numpy.sqrt(var)
            
            # Generate the smooth PDF curve
            x_range = numpy.linspace(mu - 4*std, mu + 4*std, 1000)
            pdf = (1.0 / (std * numpy.sqrt(2 * numpy.pi))) * numpy.exp(-0.5 * ((x_range - mu) / std)**2)
            
            ax.plot(x_range, pdf, color='black', linewidth=2, linestyle='--')
            
            # Formatting
            ax.set_title(f'Class {c}')
            ax.set_xlabel(f'Feature {i+1} Value')
            ax.set_ylabel('Density')
        
        plt.tight_layout()
        
        # --- Save and close ---
        # Generate the filename and save the plot
        file_path = os.path.join(output_dir, f'feature_{i+1}_distribution.png')
        fig.savefig(file_path)
        
        # Free up memory by explicitly closing the figure
        plt.close(fig)
        
    print(f"Successfully saved {num_features} plots to the '{output_dir}' directory.")