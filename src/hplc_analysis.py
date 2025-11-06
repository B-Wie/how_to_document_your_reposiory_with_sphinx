"""
HPLC Chromatogram Analysis Module

This module provides functions for analyzing HPLC chromatogram data, including
peak detection and basic chromatographic parameter calculations.

eLabFTW Integration
-------------------
This analysis script is designed to work with chromatogram data exported from
laboratory instruments. Link your analysis to experimental records in eLabFTW:

* **Equipment Records**: Document instrument specifications and maintenance
  (e.g., https://your-elabftw-instance.org/database.php?mode=view&id=EQUIP-12345)
* **Experiment Records**: Reference the specific experimental run
  (e.g., https://your-elabftw-instance.org/experiments.php?mode=view&id=67890)

Example eLabFTW Reference in Code
----------------------------------
Always include eLabFTW links in your data files and analysis scripts:

.. code-block:: python

    # Link to eLabFTW experiment in file header or docstring
    # Experiment: https://your-elabftw-instance.org/experiments.php?mode=view&id=67890
    # Equipment: https://your-elabftw-instance.org/database.php?mode=view&id=EQUIP-12345

For more information on eLabFTW integration, see the documentation.
"""

import numpy as np
from typing import Tuple, List, Dict
from pathlib import Path


def load_chromatogram(filepath: str) -> Tuple[np.ndarray, np.ndarray]:
    """
    Load HPLC chromatogram data from a text file.
    
    Reads a two-column text file containing time and absorbance data.
    Lines starting with '#' are treated as comments and skipped.
    
    Parameters
    ----------
    filepath : str
        Path to the chromatogram data file. File should contain two columns:
        time (minutes) and absorbance (mAU).
        
    Returns
    -------
    time : np.ndarray
        Time values in minutes (1D array).
    absorbance : np.ndarray
        Absorbance values in mAU (1D array).
        
    Raises
    ------
    FileNotFoundError
        If the specified file does not exist.
    ValueError
        If the file format is invalid or cannot be parsed.
        
    Examples
    --------
    >>> time, absorbance = load_chromatogram('data/sample_hplc_chromatogram.txt')
    >>> print(f"Data points: {len(time)}")
    Data points: 101
    >>> print(f"Time range: {time[0]:.2f} - {time[-1]:.2f} min")
    Time range: 0.00 - 10.00 min
    
    Notes
    -----
    **eLabFTW Best Practice**: Include the eLabFTW experiment ID in the
    chromatogram file header as a comment. This creates a permanent link
    between your raw data and experimental documentation.
    
    Example file header::
    
        # Experiment: eLabFTW #67890
        # Equipment: HPLC-UV (eLabFTW ID: EQUIP-12345)
        # Time(min)    Absorbance(mAU)
        0.00    2.1
        ...
    
    See Also
    --------
    find_peaks : Detect peaks in the loaded chromatogram
    """
    filepath_obj = Path(filepath)
    if not filepath_obj.exists():
        raise FileNotFoundError(f"Chromatogram file not found: {filepath}")
    
    # Read data, skipping comment lines
    data = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                parts = line.split()
                if len(parts) >= 2:
                    try:
                        time_val = float(parts[0])
                        abs_val = float(parts[1])
                        data.append([time_val, abs_val])
                    except ValueError:
                        continue  # Skip lines that can't be converted to float
    
    if not data:
        raise ValueError(f"No valid data found in {filepath}")
    
    data_array = np.array(data)
    return data_array[:, 0], data_array[:, 1]


def find_peaks(time: np.ndarray, absorbance: np.ndarray, 
               threshold: float = 10.0, min_distance: int = 5) -> List[Dict[str, float]]:
    """
    Detect peaks in HPLC chromatogram data.
    
    Identifies local maxima in the absorbance signal that exceed a specified
    threshold. Returns peak properties including retention time, height, and
    approximate area.
    
    Parameters
    ----------
    time : np.ndarray
        Time values in minutes (1D array).
    absorbance : np.ndarray
        Absorbance values in mAU (1D array).
    threshold : float, optional
        Minimum peak height in mAU to be considered a peak (default: 10.0).
    min_distance : int, optional
        Minimum number of data points between peaks (default: 5).
        
    Returns
    -------
    peaks : list of dict
        List of detected peaks, where each peak is a dictionary containing:
        
        * 'retention_time': float - Peak retention time in minutes
        * 'height': float - Peak height in mAU
        * 'area': float - Approximate peak area (trapezoidal integration)
        * 'index': int - Index of peak maximum in the data array
        
    Examples
    --------
    >>> time, absorbance = load_chromatogram('data/sample_hplc_chromatogram.txt')
    >>> peaks = find_peaks(time, absorbance, threshold=50.0)
    >>> for i, peak in enumerate(peaks, 1):
    ...     print(f"Peak {i}: RT={peak['retention_time']:.2f} min, "
    ...           f"Height={peak['height']:.1f} mAU")
    Peak 1: RT=2.10 min, Height=98.7 mAU
    Peak 2: RT=5.70 min, Height=122.3 mAU
    
    Notes
    -----
    This is a simple peak detection algorithm suitable for well-resolved peaks.
    For complex chromatograms with overlapping peaks, consider using more
    sophisticated peak deconvolution methods.
    
    The peak area is calculated using trapezoidal integration from the point
    where absorbance drops below the threshold on either side of the peak.
    
    **Documentation in eLabFTW**: When documenting peak identification results,
    include them in your eLabFTW experiment record along with:
    
    * Integration parameters (threshold, baseline correction)
    * Peak assignments (compound identities)
    * Calibration curve information for quantification
    
    This ensures all analysis parameters are tracked with your experimental data.
    
    See Also
    --------
    load_chromatogram : Load chromatogram data from file
    calculate_resolution : Calculate peak resolution
    """
    peaks = []
    n = len(absorbance)
    
    # Find local maxima
    for i in range(1, n - 1):
        # Check if this point is a local maximum
        if (absorbance[i] > absorbance[i-1] and 
            absorbance[i] > absorbance[i+1] and 
            absorbance[i] > threshold):
            
            # Check minimum distance from previous peaks
            if peaks and (i - peaks[-1]['index']) < min_distance:
                # If new peak is higher, replace previous peak
                if absorbance[i] > peaks[-1]['height']:
                    peaks[-1] = {
                        'retention_time': time[i],
                        'height': absorbance[i],
                        'index': i
                    }
                continue
            
            # Calculate approximate peak area (simple integration)
            # Find peak start and end (where signal drops below threshold)
            start_idx = i
            while start_idx > 0 and absorbance[start_idx] > threshold * 0.1:
                start_idx -= 1
            
            end_idx = i
            while end_idx < n - 1 and absorbance[end_idx] > threshold * 0.1:
                end_idx += 1
            
            # Trapezoidal integration for area
            peak_area = np.trapezoid(absorbance[start_idx:end_idx+1], 
                                     time[start_idx:end_idx+1])
            
            peaks.append({
                'retention_time': time[i],
                'height': absorbance[i],
                'area': peak_area,
                'index': i
            })
    
    return peaks


def calculate_resolution(peak1: Dict[str, float], peak2: Dict[str, float], 
                        time: np.ndarray, absorbance: np.ndarray) -> float:
    """
    Calculate chromatographic resolution between two peaks.
    
    Resolution (Rs) is a measure of peak separation, defined as:
    
    .. math::
        R_s = \\frac{2(t_{R2} - t_{R1})}{w_1 + w_2}
    
    where :math:`t_{R1}` and :math:`t_{R2}` are retention times, and
    :math:`w_1` and :math:`w_2` are peak widths at baseline.
    
    Parameters
    ----------
    peak1 : dict
        First peak dictionary from find_peaks().
    peak2 : dict
        Second peak dictionary from find_peaks().
    time : np.ndarray
        Time values in minutes.
    absorbance : np.ndarray
        Absorbance values in mAU.
        
    Returns
    -------
    resolution : float
        Resolution value. Rs > 1.5 indicates baseline separation.
        
    Examples
    --------
    >>> time, absorbance = load_chromatogram('data/sample_hplc_chromatogram.txt')
    >>> peaks = find_peaks(time, absorbance, threshold=50.0)
    >>> if len(peaks) >= 2:
    ...     rs = calculate_resolution(peaks[0], peaks[1], time, absorbance)
    ...     print(f"Resolution: {rs:.2f}")
    Resolution: 4.23
    
    Notes
    -----
    This implementation estimates peak width at half height (FWHH) and converts
    to baseline width using the approximation: baseline_width ≈ 2 * FWHH.
    
    **Quality Control**: Document resolution values in eLabFTW for method
    validation and quality control. Include acceptance criteria (typically
    Rs > 1.5 for baseline separation).
    
    References
    ----------
    .. [1] Snyder, L. R., Kirkland, J. J., & Dolan, J. W. (2010).
           Introduction to Modern Liquid Chromatography (3rd ed.). Wiley.
    """
    # Calculate retention time difference
    rt_diff = abs(peak2['retention_time'] - peak1['retention_time'])
    
    # Estimate peak widths at half height
    def estimate_peak_width(peak_dict):
        idx = peak_dict['index']
        half_height = peak_dict['height'] / 2.0
        
        # Find left half-height point
        left_idx = idx
        while left_idx > 0 and absorbance[left_idx] > half_height:
            left_idx -= 1
        
        # Find right half-height point
        right_idx = idx
        n = len(absorbance)
        while right_idx < n - 1 and absorbance[right_idx] > half_height:
            right_idx += 1
        
        # Width at half height
        fwhh = time[right_idx] - time[left_idx]
        # Approximate baseline width (4σ for Gaussian peak)
        return 2.0 * fwhh
    
    w1 = estimate_peak_width(peak1)
    w2 = estimate_peak_width(peak2)
    
    # Calculate resolution
    resolution = 2.0 * rt_diff / (w1 + w2)
    return resolution


def analyze_chromatogram(filepath: str, threshold: float = 10.0) -> Dict:
    """
    Complete analysis workflow for an HPLC chromatogram.
    
    Loads data, detects peaks, and calculates chromatographic parameters.
    Provides a comprehensive summary suitable for reporting in laboratory
    notebooks or publications.
    
    Parameters
    ----------
    filepath : str
        Path to chromatogram data file.
    threshold : float, optional
        Peak detection threshold in mAU (default: 10.0).
        
    Returns
    -------
    results : dict
        Analysis results containing:
        
        * 'filepath': str - Input file path
        * 'n_points': int - Number of data points
        * 'time_range': tuple - (min_time, max_time) in minutes
        * 'peaks': list - Detected peaks with properties
        * 'n_peaks': int - Number of detected peaks
        * 'baseline': float - Estimated baseline absorbance
        
    Examples
    --------
    >>> results = analyze_chromatogram('data/sample_hplc_chromatogram.txt', 
    ...                                threshold=50.0)
    >>> print(f"Detected {results['n_peaks']} peaks")
    Detected 2 peaks
    >>> for i, peak in enumerate(results['peaks'], 1):
    ...     print(f"Peak {i}: RT={peak['retention_time']:.2f} min")
    Peak 1: RT=2.10 min
    Peak 2: RT=5.70 min
    
    Notes
    -----
    **Complete Workflow with eLabFTW**:
    
    1. **Before Analysis**:
       
       * Create experiment record in eLabFTW with method details
       * Record instrument ID and calibration information
       * Upload raw data file to eLabFTW
    
    2. **During Analysis**:
       
       * Run this analysis function
       * Reference eLabFTW experiment ID in analysis script header
    
    3. **After Analysis**:
       
       * Export results to CSV or JSON
       * Upload results to eLabFTW experiment record
       * Link GitHub repository/commit in eLabFTW for code traceability
       * Document any manual peak assignments or corrections
    
    This workflow ensures complete traceability from raw data to final results.
    
    See Also
    --------
    load_chromatogram : Load data file
    find_peaks : Peak detection algorithm
    """
    # Load data
    time, absorbance = load_chromatogram(filepath)
    
    # Detect peaks
    peaks = find_peaks(time, absorbance, threshold=threshold)
    
    # Calculate baseline (median of first 10% of data)
    n_baseline = max(1, len(absorbance) // 10)
    baseline = np.median(absorbance[:n_baseline])
    
    # Compile results
    results = {
        'filepath': filepath,
        'n_points': len(time),
        'time_range': (float(time[0]), float(time[-1])),
        'peaks': peaks,
        'n_peaks': len(peaks),
        'baseline': float(baseline)
    }
    
    return results


if __name__ == '__main__':
    # Example usage - analyze the sample chromatogram
    # This demonstrates the complete workflow for HPLC data analysis
    
    # Reference to eLabFTW (replace with your instance URLs)
    print("HPLC Chromatogram Analysis")
    print("=" * 50)
    print("eLabFTW Experiment: https://your-elabftw-instance.org/experiments.php?mode=view&id=67890")
    print("eLabFTW Equipment: https://your-elabftw-instance.org/database.php?mode=view&id=EQUIP-12345")
    print()
    
    # Analyze chromatogram
    data_file = 'data/sample_hplc_chromatogram.txt'
    results = analyze_chromatogram(data_file, threshold=50.0)
    
    # Print summary
    print(f"File: {results['filepath']}")
    print(f"Data points: {results['n_points']}")
    print(f"Time range: {results['time_range'][0]:.2f} - {results['time_range'][1]:.2f} min")
    print(f"Baseline: {results['baseline']:.2f} mAU")
    print(f"\nDetected {results['n_peaks']} peaks:")
    print("-" * 50)
    
    for i, peak in enumerate(results['peaks'], 1):
        print(f"\nPeak {i}:")
        print(f"  Retention Time: {peak['retention_time']:.2f} min")
        print(f"  Height: {peak['height']:.1f} mAU")
        print(f"  Area: {peak['area']:.1f} mAU·min")
    
    # Calculate resolution if multiple peaks found
    if results['n_peaks'] >= 2:
        print("\nPeak Resolution:")
        print("-" * 50)
        time, absorbance = load_chromatogram(data_file)
        for i in range(len(results['peaks']) - 1):
            rs = calculate_resolution(results['peaks'][i], results['peaks'][i+1], 
                                     time, absorbance)
            print(f"Peak {i+1} - Peak {i+2}: Rs = {rs:.2f}")
    
    print("\n" + "=" * 50)
    print("Analysis complete. Document results in eLabFTW experiment record.")
