How to Document Your Repository with Sphinx
============================================

Welcome to the comprehensive tutorial on documenting scientific Python projects 
with Sphinx! This guide demonstrates best practices for creating professional, 
publication-ready documentation complete with equations, cross-references, and 
automated API documentation.

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   experiment_setup
   publication_context

Introduction
------------

This repository provides a complete example of how to document scientific Python 
code using Sphinx. It demonstrates:

* **Automatic API documentation** from NumPy-style docstrings
* **Mathematical equations** with LaTeX notation  
* **Cross-references** between documentation sections
* **External links** to resources and publications
* **GitHub Pages deployment** via GitHub Actions

Whether you're documenting a research project, a scientific library, or a data 
analysis pipeline, this tutorial provides the foundation you need.

Features
--------

* 📚 **Complete Documentation Stack**: Sphinx with autodoc, napoleon, and RTD theme
* 🔢 **Mathematical Notation**: LaTeX equations rendered with MathJax
* 🔗 **Smart Linking**: Cross-references between docs and code
* 🤖 **Automated Deployment**: GitHub Actions workflow for GitHub Pages
* 📝 **NumPy-Style Docstrings**: Industry-standard documentation format
* 🎨 **Professional Theme**: Read the Docs theme for clean, accessible documentation

Quick Start
-----------

**1. Install Sphinx and Dependencies**

.. code-block:: bash

   pip install -r requirements.txt

The requirements include:

* ``sphinx>=7.0.0`` - Documentation generator
* ``sphinx-rtd-theme>=1.3.0`` - Read the Docs theme

**2. Build the Documentation Locally**

.. code-block:: bash

   cd docs
   make html

**3. View the Documentation**

Open ``docs/build/html/index.html`` in your web browser.

Documentation Structure
-----------------------

This tutorial is organized into several sections:

* :doc:`experiment_setup` - Demonstrates mathematical equations, tables, and technical documentation
* :doc:`publication_context` - Shows how to document citations, repositories, and research context
* API Documentation (below) - Auto-generated from Python docstrings

Mathematical Example
--------------------

Sphinx can render beautiful mathematical equations using LaTeX notation. For example,
the Gaussian (normal) distribution is defined as:

.. math::
   
   f(x | \mu, \sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}

where :math:`\mu` is the mean and :math:`\sigma^2` is the variance.

For more equations and mathematical documentation, see :doc:`experiment_setup`.

Sample Module API
------------------

This documentation includes a sample Python module with NumPy-style docstrings
that demonstrate proper scientific code documentation.

.. automodule:: sample_module
   :members:
   :undoc-members:
   :show-inheritance:

The :mod:`sample_module` provides functions for:

* Statistical calculations (:func:`sample_module.calculate_mean_std`)
* Linear regression (:func:`sample_module.linear_regression`)  
* Data normalization (:func:`sample_module.normalize_data`)
* Data analysis (:class:`sample_module.DataAnalyzer`)

Usage Example
-------------

Here's a quick example of using the sample module:

.. code-block:: python

   import numpy as np
   from sample_module import DataAnalyzer
   
   # Create sample data
   data = np.random.normal(loc=50, scale=10, size=100)
   
   # Analyze the data
   analyzer = DataAnalyzer(data, name='experimental_data')
   summary = analyzer.get_summary()
   
   print(f"Mean: {summary['mean']:.2f}")
   print(f"Median: {summary['median']:.2f}")
   print(f"Std Dev: {summary['std']:.2f}")

For more detailed examples, see the :doc:`experiment_setup` section.

Deploying to GitHub Pages
--------------------------

This repository includes a GitHub Actions workflow that automatically:

1. Builds the Sphinx documentation on every push to ``main``
2. Deploys the built HTML to GitHub Pages
3. Makes documentation available at ``https://<username>.github.io/<repository>/``

See :doc:`publication_context` for details on the deployment workflow.

Repository Links
----------------

* **GitHub Repository**: https://github.com/B-Wie/how_to_document_your_reposiory_with_sphinx
* **Documentation**: https://b-wie.github.io/how_to_document_your_reposiory_with_sphinx/
* **Sample Code**: `src/sample_module.py <../../src/sample_module.py>`_

Additional Resources
--------------------

* `Sphinx Documentation <https://www.sphinx-doc.org/>`_ - Official Sphinx documentation
* `NumPy Documentation Standard <https://numpydoc.readthedocs.io/>`_ - Docstring style guide
* `Read the Docs <https://docs.readthedocs.io/>`_ - Documentation hosting platform

Next Steps
----------

* Explore the :doc:`experiment_setup` to see equations, tables, and technical documentation
* Review :doc:`publication_context` for citation and repository information
* Check out the source code in ``src/sample_module.py`` to see NumPy-style docstrings in action
* Visit the `GitHub repository <https://github.com/B-Wie/how_to_document_your_reposiory_with_sphinx>`_ to view the complete setup

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
