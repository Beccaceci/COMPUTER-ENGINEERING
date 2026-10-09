import numpy as np
from pathlib import Path
import sys

# Add parent directory to path to allow importing utils
sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils.math_utils import log_GAU_ND, loglikelihood, vrow

if __name__ == "__main__":
    ROOT = Path(__file__).resolve().parent.parent
    solutions_dir = ROOT / "solutions" / "expected_results"
    
    # 1. 1D Density check
    print("--- 1D Density Check ---")
    XPlot = np.linspace(-8, 12, 1000)
    m = np.ones((1, 1)) * 1.0
    C = np.ones((1, 1)) * 2.0
    
    pdfSol_1D = np.load(solutions_dir / 'llGAU.npy')
    pdfGau_1D = log_GAU_ND(vrow(XPlot), m, C)
    error_1D = np.abs(pdfSol_1D - pdfGau_1D).max()
    print(f"Max error 1D density: {error_1D}")
    
    # 2. ND Density check
    print("\n--- ND Density Check ---")
    XND = np.load(solutions_dir / 'XND.npy')
    muND = np.load(solutions_dir / 'muND.npy')
    CND = np.load(solutions_dir / 'CND.npy')
    
    pdfSol_ND = np.load(solutions_dir / 'llND.npy')
    pdfGau_ND = log_GAU_ND(XND, muND, CND)
    error_ND = np.abs(pdfSol_ND - pdfGau_ND).max()
    print(f"Max error ND density: {error_ND}")
    
    # 3. Log-likelihood ND check
    print("\n--- Log-likelihood ND Check ---")
    mu_ML_ND = XND.mean(1, keepdims=True)
    C_ML_ND = ((XND - mu_ML_ND) @ (XND - mu_ML_ND).T) / float(XND.shape[1])
    
    ll_ND = loglikelihood(XND, mu_ML_ND, C_ML_ND)
    print(f"Log-likelihood (XND): {ll_ND} (Expected: -270.70478023795044)")
    
    # 4. Log-likelihood 1D check
    print("\n--- Log-likelihood 1D Check ---")
    X1D = np.load(solutions_dir / 'X1D.npy')
    mu_ML_1D = X1D.mean(1, keepdims=True)
    C_ML_1D = ((X1D - mu_ML_1D) @ (X1D - mu_ML_1D).T) / float(X1D.shape[1])
    
    ll_1D = loglikelihood(X1D, mu_ML_1D, C_ML_1D)
    print(f"Log-likelihood (X1D): {ll_1D} (Expected: -23227.077654602715)")
