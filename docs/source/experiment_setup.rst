Experiment Setup
================

This section describes the experimental setup and methodology used in our research.

Overview
--------

Our experiments investigate data analysis techniques for scientific computing, 
with a focus on statistical methods and their applications. The experimental 
framework is built using Python and leverages the NumPy library for numerical computations.

Experimental Design
-------------------

The experimental workflow consists of three main phases:

1. **Data Collection**: Gathering raw data from sensors or simulations
2. **Data Processing**: Applying normalization and transformation techniques
3. **Statistical Analysis**: Computing descriptive statistics and performing regression analysis

Mathematical Framework
----------------------

Our analysis is based on standard statistical measures. The mean :math:`\mu` and 
standard deviation :math:`\sigma` are calculated as:

.. math::
   
   \mu = \frac{1}{N} \sum_{i=1}^{N} x_i

.. math::
   
   \sigma = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2}

where :math:`N` is the number of samples and :math:`x_i` represents individual data points.

For regression analysis, we use the least squares method. The coefficient of 
determination :math:`R^2` is computed as:

.. math::
   
   R^2 = 1 - \frac{\sum_{i=1}^{N} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{N} (y_i - \bar{y})^2}

where :math:`y_i` are the observed values, :math:`\hat{y}_i` are the predicted values,
and :math:`\bar{y}` is the mean of observed values.

Data Normalization Techniques
------------------------------

We implement two normalization methods:

**Z-score Normalization**

.. math::
   
   z = \frac{x - \mu}{\sigma}

This transforms data to have zero mean and unit variance, which is useful for 
comparing variables with different scales.

**Min-Max Normalization**

.. math::
   
   x_{norm} = \frac{x - x_{min}}{x_{max} - x_{min}}

This scales data to the range [0, 1], preserving the original distribution shape.

Implementation Details
----------------------

The experimental code is implemented in the :mod:`sample_module` module. 
Key functions include:

* :func:`sample_module.calculate_mean_std` - Computes mean and standard deviation
* :func:`sample_module.linear_regression` - Performs linear regression analysis
* :func:`sample_module.normalize_data` - Normalizes data using various methods

For complete API documentation, see the main :doc:`index` page.

Software Requirements
---------------------

The experiment requires the following software packages:

* **Python** ≥ 3.7
* **NumPy** ≥ 1.19.0 for numerical computations
* **Sphinx** ≥ 7.0.0 for documentation generation

For installation instructions, refer to the main `README.md <../README.md>`_ file
in the repository root.

Example Usage
-------------

Here's a simple example demonstrating the core functionality:

.. code-block:: python
   
   import numpy as np
   from sample_module import calculate_mean_std, normalize_data
   
   # Generate sample data
   data = np.random.normal(loc=10, scale=2, size=100)
   
   # Calculate statistics
   mean, std = calculate_mean_std(data)
   print(f"Mean: {mean:.2f}, Std: {std:.2f}")
   
   # Normalize data
   normalized = normalize_data(data, method='zscore')
   print(f"Normalized mean: {np.mean(normalized):.2f}")

Experimental Parameters
-----------------------

The following parameters were used across all experiments:

.. list-table:: Experiment Parameters
   :widths: 30 20 50
   :header-rows: 1

   * - Parameter
     - Value
     - Description
   * - Sample Size
     - 1000
     - Number of data points per experiment
   * - Significance Level
     - 0.05
     - Alpha value for statistical tests
   * - Normalization
     - Z-score
     - Default normalization method
   * - Outlier Threshold
     - 1.5 IQR
     - Threshold for outlier detection

Data Visualization
------------------

While this documentation focuses on computational methods, visualizations can be 
generated using matplotlib. For examples, see the `Matplotlib Gallery 
<https://matplotlib.org/stable/gallery/index.html>`_.

.. note::
   
   All figures should be saved in the ``docs/source/_static/figures/`` directory
   and referenced using the ``.. figure::`` directive for inclusion in documentation.

Reproducibility
---------------

To ensure reproducibility of results:

1. Use fixed random seeds when generating synthetic data
2. Document all software versions in ``requirements.txt``
3. Provide example scripts in the repository
4. Archive data and code with DOI (see :doc:`publication_context`)

For more information on reproducible research practices, see the 
`Turing Way Guide <https://the-turing-way.netlify.app/reproducible-research/overview.html>`_.

External Resources
------------------

Additional information can be found in these resources:

* `NumPy Documentation <https://numpy.org/doc/stable/>`_ - Official NumPy documentation
* `SciPy Lectures <https://scipy-lectures.org/>`_ - Tutorial material on scientific Python
* `Python Scientific Lecture Notes <https://scipy-lectures.org/intro/numpy/index.html>`_ - NumPy introduction

Code Repository
---------------

The complete source code is available in the GitHub repository:

* Main repository: https://github.com/B-Wie/how_to_document_your_reposiory_with_sphinx
* Sample module: `src/sample_module.py <../../../src/sample_module.py>`_

See Also
--------

* :doc:`publication_context` - Information about publications using this code
* :doc:`index` - Documentation home page
