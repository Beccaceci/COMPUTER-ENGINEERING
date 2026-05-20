import numpy
import matplotlib.pyplot as plt

def plot_confusion_matrix_heatmap(M, class_names, title, output_path):
    """
    Plots a graphical heatmap of the confusion matrix and saves it.
    """
    plt.figure(figsize=(6, 5))
    plt.imshow(M, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title(title)
    plt.colorbar()
    
    tick_marks = numpy.arange(len(class_names))
    plt.xticks(tick_marks, class_names)
    plt.yticks(tick_marks, class_names)
    
    plt.xlabel('True Class')
    plt.ylabel('Predicted Class')
    
    # Add text annotations inside the squares
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            plt.text(j, i, str(M[i, j]), horizontalalignment="center", 
                     color="white" if M[i, j] > M.max() / 2. else "black")
            
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def plot_roc_curve(FPR, TPR, output_path):
    """
    Plots the ROC curve given pre-computed FPR and TPR arrays.
    """
    plt.figure(figsize=(8, 6))
    plt.plot(FPR, TPR, linewidth=3, color='b')
    plt.grid(True, linestyle='--')
    plt.xlabel('FPR')
    plt.ylabel('TPR')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def plot_bayes_error(effPriorLogOdds, dcf_values, min_dcf_values, output_path, xlim =(-3, 3), ylim=(0, 1.1)):
    """
    Plots the normalized DCF and minimum normalized DCF as a function of prior log-odds.
    """
    plt.figure(figsize=(8, 6))
    
    # Plot both lines as requested
    plt.plot(effPriorLogOdds, dcf_values, label='DCF', color='r', linewidth=3)
    plt.plot(effPriorLogOdds, min_dcf_values, label='min DCF', color='b', linewidth=3)
    
    # Set limits
    plt.ylim(ylim)
    plt.xlim(xlim)
    
    # Labels and formatting
    plt.xlabel('prior log-odds')
    plt.ylabel('DCF value')
    plt.legend(loc='lower left')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()

def plot_bayes_error_comparison(effPriorLogOdds, dcf_1, min_dcf_1, dcf_2, min_dcf_2, output_path):
    """
    Plots the normalized DCF and minimum normalized DCF for two different classifiers as a function of prior log-odds for side-by-side comparison.
    """
    plt.figure(figsize=(8, 6))
    
    # Classifier 1 (Red and Blue)
    plt.plot(effPriorLogOdds, dcf_1, label='DCF (Cls 1)', color='r', linewidth=3)
    plt.plot(effPriorLogOdds, min_dcf_1, label='min DCF (Cls 1)', color='b', linewidth=3)
    
    # Classifier 2 (Orange and Light Blue/Cyan)
    plt.plot(effPriorLogOdds, dcf_2, label='DCF (Cls 2)', color='orange', linewidth=3)
    plt.plot(effPriorLogOdds, min_dcf_2, label='min DCF (Cls 2)', color='c', linewidth=3)
    
    # Set limits as specified by the laboratory
    plt.ylim([0, 1.1])
    plt.xlim([-3, 3])
    
    # Labels and formatting
    plt.xlabel('prior log-odds')
    plt.ylabel('DCF value')
    plt.legend(loc='lower left')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()