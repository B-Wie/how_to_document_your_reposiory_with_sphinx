"""
Sample module for demonstrating scientific Python documentation.

This module provides functions for data analysis and statistical computations
commonly used in scientific research.
"""

import numpy as np
from typing import Union, Tuple, Optional


def calculate_mean_std(data: np.ndarray) -> Tuple[float, float]:
    """
    Calculate the mean and standard deviation of a dataset.
    
    This function computes the arithmetic mean and population standard deviation
    of the input data using NumPy's efficient implementations.
    
    Parameters
    ----------
    data : np.ndarray
        A 1D numpy array containing numerical data.
        
    Returns
    -------
    mean : float
        The arithmetic mean of the dataset.
    std : float
        The population standard deviation of the dataset.
        
    Examples
    --------
    >>> import numpy as np
    >>> data = np.array([1, 2, 3, 4, 5])
    >>> mean, std = calculate_mean_std(data)
    >>> print(f"Mean: {mean}, Std: {std:.2f}")
    Mean: 3.0, Std: 1.41
    
    Notes
    -----
    The standard deviation is calculated using the population formula (N divisor),
    not the sample formula (N-1 divisor).
    
    See Also
    --------
    numpy.mean : Compute the arithmetic mean.
    numpy.std : Compute the standard deviation.
    """
    mean = np.mean(data)
    std = np.std(data)
    return mean, std


def linear_regression(x: np.ndarray, y: np.ndarray) -> Tuple[float, float, float]:
    """
    Perform simple linear regression on two variables.
    
    Fits a linear model y = mx + b to the data using the least squares method.
    Returns the slope, intercept, and coefficient of determination (R²).
    
    Parameters
    ----------
    x : np.ndarray
        Independent variable data (1D array).
    y : np.ndarray
        Dependent variable data (1D array).
        
    Returns
    -------
    slope : float
        The slope (m) of the fitted line.
    intercept : float
        The y-intercept (b) of the fitted line.
    r_squared : float
        The coefficient of determination (R²), indicating goodness of fit.
        Values range from 0 to 1, where 1 indicates perfect fit.
        
    Raises
    ------
    ValueError
        If x and y have different lengths or if x has zero variance.
        
    Examples
    --------
    >>> import numpy as np
    >>> x = np.array([1, 2, 3, 4, 5])
    >>> y = np.array([2, 4, 5, 4, 5])
    >>> slope, intercept, r2 = linear_regression(x, y)
    >>> print(f"y = {slope:.2f}x + {intercept:.2f}, R² = {r2:.3f}")
    y = 0.60x + 2.20, R² = 0.462
    
    Notes
    -----
    The R² value is calculated as:
    
    .. math::
        R^2 = 1 - \\frac{SS_{res}}{SS_{tot}}
        
    where :math:`SS_{res}` is the residual sum of squares and 
    :math:`SS_{tot}` is the total sum of squares.
    
    References
    ----------
    .. [1] Draper, N. R., & Smith, H. (1998). Applied Regression Analysis 
           (3rd ed.). Wiley-Interscience.
    """
    if len(x) != len(y):
        raise ValueError("x and y must have the same length")
    
    if np.std(x) == 0:
        raise ValueError("x must have non-zero variance")
    
    # Calculate slope and intercept
    slope = np.cov(x, y)[0, 1] / np.var(x)
    intercept = np.mean(y) - slope * np.mean(x)
    
    # Calculate R²
    y_pred = slope * x + intercept
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r_squared = 1 - (ss_res / ss_tot) if ss_tot != 0 else 0
    
    return slope, intercept, r_squared


def normalize_data(data: np.ndarray, method: str = 'zscore') -> np.ndarray:
    """
    Normalize data using specified method.
    
    Transforms the input data to a standardized scale for improved
    comparability and analysis.
    
    Parameters
    ----------
    data : np.ndarray
        Input data to be normalized (1D or 2D array).
    method : {'zscore', 'minmax'}, optional
        Normalization method to use (default is 'zscore').
        
        * 'zscore': Standardize to zero mean and unit variance
        * 'minmax': Scale to [0, 1] range
        
    Returns
    -------
    normalized : np.ndarray
        Normalized data with the same shape as input.
        
    Raises
    ------
    ValueError
        If method is not 'zscore' or 'minmax'.
        
    Examples
    --------
    >>> import numpy as np
    >>> data = np.array([1, 2, 3, 4, 5])
    >>> normalized = normalize_data(data, method='zscore')
    >>> print(f"Mean: {np.mean(normalized):.2f}, Std: {np.std(normalized):.2f}")
    Mean: 0.00, Std: 1.00
    
    >>> normalized = normalize_data(data, method='minmax')
    >>> print(f"Min: {np.min(normalized):.2f}, Max: {np.max(normalized):.2f}")
    Min: 0.00, Max: 1.00
    
    Notes
    -----
    Z-score normalization is defined as:
    
    .. math::
        z = \\frac{x - \\mu}{\\sigma}
        
    Min-max normalization is defined as:
    
    .. math::
        x_{norm} = \\frac{x - x_{min}}{x_{max} - x_{min}}
    """
    if method == 'zscore':
        mean = np.mean(data)
        std = np.std(data)
        if std == 0:
            return np.zeros_like(data)
        return (data - mean) / std
    elif method == 'minmax':
        min_val = np.min(data)
        max_val = np.max(data)
        if max_val == min_val:
            return np.zeros_like(data)
        return (data - min_val) / (max_val - min_val)
    else:
        raise ValueError(f"Unknown method '{method}'. Use 'zscore' or 'minmax'.")


class DataAnalyzer:
    """
    A class for performing common data analysis operations.
    
    This class provides methods for statistical analysis, data transformation,
    and visualization preparation for scientific datasets.
    
    Parameters
    ----------
    data : np.ndarray
        Input dataset to analyze.
    name : str, optional
        Name identifier for the dataset (default is 'dataset').
        
    Attributes
    ----------
    data : np.ndarray
        The stored dataset.
    name : str
        The dataset name.
    n_samples : int
        Number of samples in the dataset.
        
    Examples
    --------
    >>> import numpy as np
    >>> data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    >>> analyzer = DataAnalyzer(data, name='test_data')
    >>> summary = analyzer.get_summary()
    >>> print(summary['mean'])
    5.5
    
    Notes
    -----
    This class is designed for 1D numerical datasets. For multidimensional
    data, consider reshaping or using specialized tools.
    """
    
    def __init__(self, data: np.ndarray, name: str = 'dataset'):
        """Initialize the DataAnalyzer."""
        self.data = data
        self.name = name
        self.n_samples = len(data)
    
    def get_summary(self) -> dict:
        """
        Get statistical summary of the dataset.
        
        Returns
        -------
        dict
            Dictionary containing statistical measures:
            
            * 'mean': arithmetic mean
            * 'median': median value
            * 'std': standard deviation
            * 'min': minimum value
            * 'max': maximum value
            * 'q25': 25th percentile
            * 'q75': 75th percentile
            
        Examples
        --------
        >>> import numpy as np
        >>> analyzer = DataAnalyzer(np.array([1, 2, 3, 4, 5]))
        >>> summary = analyzer.get_summary()
        >>> summary['median']
        3.0
        """
        return {
            'mean': np.mean(self.data),
            'median': np.median(self.data),
            'std': np.std(self.data),
            'min': np.min(self.data),
            'max': np.max(self.data),
            'q25': np.percentile(self.data, 25),
            'q75': np.percentile(self.data, 75)
        }
    
    def detect_outliers(self, method: str = 'iqr', threshold: float = 1.5) -> np.ndarray:
        """
        Detect outliers in the dataset.
        
        Parameters
        ----------
        method : {'iqr', 'zscore'}, optional
            Method for outlier detection (default is 'iqr').
            
            * 'iqr': Interquartile range method
            * 'zscore': Z-score method
            
        threshold : float, optional
            Threshold for outlier detection (default is 1.5 for IQR, 
            typically 3.0 for z-score).
            
        Returns
        -------
        np.ndarray
            Boolean array indicating outliers (True) and inliers (False).
            
        Examples
        --------
        >>> import numpy as np
        >>> data = np.array([1, 2, 3, 4, 5, 100])  # 100 is an outlier
        >>> analyzer = DataAnalyzer(data)
        >>> outliers = analyzer.detect_outliers(method='iqr')
        >>> print(data[outliers])
        [100]
        
        Notes
        -----
        The IQR method considers values outside of 
        :math:`[Q1 - threshold \\times IQR, Q3 + threshold \\times IQR]`
        as outliers, where :math:`IQR = Q3 - Q1`.
        """
        if method == 'iqr':
            q1 = np.percentile(self.data, 25)
            q3 = np.percentile(self.data, 75)
            iqr = q3 - q1
            lower = q1 - threshold * iqr
            upper = q3 + threshold * iqr
            return (self.data < lower) | (self.data > upper)
        elif method == 'zscore':
            z_scores = np.abs((self.data - np.mean(self.data)) / np.std(self.data))
            return z_scores > threshold
        else:
            raise ValueError(f"Unknown method '{method}'. Use 'iqr' or 'zscore'.")
