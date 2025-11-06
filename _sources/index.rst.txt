Scientific Python Documentation with eLabFTW Integration
========================================================

Welcome! This repository provides a **beginner-friendly template** for Python projects in scientific labs, demonstrating how to create professional documentation with Sphinx and integrate with eLabFTW electronic lab notebooks for complete experimental traceability.

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   elabftw_integration
   best_practices

What You'll Learn
-----------------

This template demonstrates:

* 📖 **Professional Documentation**: Using Sphinx to create beautiful, searchable docs
* 🔗 **eLabFTW Integration**: Linking code to experiment records for full traceability
* 🧪 **Complete Workflows**: From lab experiment → data → analysis → results
* 🤝 **Best Practices**: Industry-standard approaches for scientific computing
* 🚀 **Automated Deployment**: Publishing docs to GitHub Pages automatically

Perfect for scientists, students, and lab users starting with Python, GitHub, and modern lab data management.

Why This Template?
------------------

Traditional Lab Workflow Problems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

❌ Lab notebook entries disconnected from analysis code  
❌ Data files scattered across computers  
❌ No clear link between experiments and results  
❌ Hard to reproduce analyses months later  
❌ Methods sections written from memory  

Modern Integrated Solution
~~~~~~~~~~~~~~~~~~~~~~~~~~~

✅ **eLabFTW** stores experiment protocols, equipment info, and raw data  
✅ **GitHub** manages analysis code with full version history  
✅ **Python scripts** reference eLabFTW experiment IDs directly  
✅ **Sphinx docs** explain methods and link everything together  
✅ **Automated publishing** keeps documentation current  

**Result**: Complete traceability from experiment to publication.

Quick Start
-----------

1. **Clone the repository**:

.. code-block:: bash

   git clone https://github.com/B-Wie/how_to_document_your_reposiory_with_sphinx.git
   cd how_to_document_your_reposiory_with_sphinx

2. **Install dependencies**:

.. code-block:: bash

   pip install -r requirements.txt

3. **Try the example**:

.. code-block:: bash

   python src/hplc_analysis.py

4. **Build the documentation**:

.. code-block:: bash

   cd docs
   make html

Then open ``docs/build/html/index.html`` in your browser.

Example: HPLC Chromatogram Analysis
------------------------------------

This repository includes a complete HPLC analysis example demonstrating eLabFTW integration:

Loading Data with eLabFTW References
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The sample data file includes eLabFTW experiment references:

.. code-block:: text

   # HPLC Chromatogram Data
   # Experiment: eLabFTW #67890
   # URL: https://your-elabftw-instance.org/experiments.php?mode=view&id=67890
   # Equipment: HPLC-UV (eLabFTW ID: EQUIP-12345)
   # Time(min)    Absorbance(mAU)
   0.00    2.1
   ...

Analysis Code with Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The analysis script demonstrates:

* NumPy-style docstrings with complete parameter documentation
* eLabFTW references in module and function docstrings
* Type hints for clarity
* Working examples with sample data

Try it:

.. code-block:: bash

   python src/hplc_analysis.py

Output:

.. code-block:: text

   HPLC Chromatogram Analysis
   ==================================================
   eLabFTW Experiment: https://your-elabftw-instance.org/experiments.php?mode=view&id=67890
   eLabFTW Equipment: https://your-elabftw-instance.org/database.php?mode=view&id=EQUIP-12345

   File: data/sample_hplc_chromatogram.txt
   Data points: 101
   Time range: 0.00 - 10.00 min
   Baseline: 2.40 mAU

   Detected 2 peaks:
   --------------------------------------------------
   Peak 1: RT=2.10 min, Height=98.7 mAU
   Peak 2: RT=5.70 min, Height=122.3 mAU

   Peak Resolution: Rs = 1.71

What is eLabFTW?
----------------

`eLabFTW <https://www.elabftw.net/>`_ is a free, open-source electronic lab notebook designed for research laboratories. It provides:

* **Experiment Documentation**: Record protocols, observations, and results
* **Equipment Database**: Track instruments, specifications, and maintenance
* **Data Management**: Store and organize research data with versioning
* **Collaboration**: Share experiments with team members
* **Compliance**: Meet FDA 21 CFR Part 11, GLP regulations
* **Persistent IDs**: Every experiment gets a permanent reference number

Combined with GitHub for code and Sphinx for documentation, eLabFTW completes the research workflow:

.. code-block:: text

   eLabFTW Experiment → GitHub Code → Python Analysis → Results back to eLabFTW
   
   (Protocol & Data) → (Version Control) → (Reproducible) → (Complete Record)

The Complete Workflow
----------------------

Step 1: Document in eLabFTW
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create experiment record with:

* Protocol and method details
* Equipment used (with database IDs)
* Raw data files uploaded
* Note the experiment ID (e.g., #67890)

Step 2: Write Analysis Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reference eLabFTW in your Python scripts:

.. code-block:: python

   """
   HPLC Analysis Script
   
   eLabFTW References:
   - Experiment: https://your-instance.org/experiments.php?mode=view&id=67890
   - Equipment: https://your-instance.org/database.php?mode=view&id=EQUIP-12345
   """
   
   from hplc_analysis import analyze_chromatogram
   
   # Load data (file header includes eLabFTW reference)
   results = analyze_chromatogram('data/sample.txt')

Step 3: Generate Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sphinx automatically builds docs from your docstrings:

.. code-block:: bash

   cd docs
   make html

Documentation includes:

* Auto-generated API reference
* eLabFTW integration guide
* Best practices for scientific docs
* Working code examples

Step 4: Return Results to eLabFTW
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Upload results to experiment record:

* Processed data and figures
* Analysis parameters used
* **GitHub commit reference** for reproducibility

This closes the loop: experiment → analysis → results → permanent record.

API Documentation
-----------------

HPLC Analysis Module
~~~~~~~~~~~~~~~~~~~~

The :mod:`hplc_analysis` module provides functions for analyzing HPLC chromatogram data with eLabFTW integration.

.. automodule:: hplc_analysis
   :members:
   :undoc-members:
   :show-inheritance:

Key functions:

* :func:`hplc_analysis.load_chromatogram` - Load data from text files
* :func:`hplc_analysis.find_peaks` - Detect peaks in chromatograms
* :func:`hplc_analysis.calculate_resolution` - Calculate peak resolution
* :func:`hplc_analysis.analyze_chromatogram` - Complete analysis workflow

Sample Module (General Scientific Computing)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :mod:`sample_module` module demonstrates general scientific computing with NumPy-style documentation.

.. automodule:: sample_module
   :members:
   :undoc-members:
   :show-inheritance:

This module includes:

* :func:`sample_module.calculate_mean_std` - Statistical calculations
* :func:`sample_module.linear_regression` - Regression analysis
* :func:`sample_module.normalize_data` - Data normalization
* :class:`sample_module.DataAnalyzer` - Data analysis class

Repository Structure
--------------------

.. code-block:: text

   .
   ├── data/
   │   └── sample_hplc_chromatogram.txt    # Example data with eLabFTW refs
   ├── src/
   │   ├── hplc_analysis.py                # HPLC analysis with eLabFTW
   │   └── sample_module.py                # General scientific computing
   ├── docs/
   │   ├── source/
   │   │   ├── conf.py                     # Sphinx configuration
   │   │   ├── index.rst                   # This page
   │   │   ├── elabftw_integration.rst     # eLabFTW workflow guide
   │   │   └── best_practices.rst          # Documentation best practices
   │   └── Makefile                        # Build commands
   ├── README.md                           # Main repository documentation
   ├── CONTRIBUTING.md                     # Contribution guidelines
   ├── LICENSE.md                          # MIT license
   └── requirements.txt                    # Python dependencies

For Beginners
-------------

New to Python?
~~~~~~~~~~~~~~

* `Python Tutorial <https://docs.python.org/3/tutorial/>`_
* `NumPy Quickstart <https://numpy.org/doc/stable/user/quickstart.html>`_
* `Python for Chemists <https://www.pythonforchemists.org/>`_

New to Git/GitHub?
~~~~~~~~~~~~~~~~~~

* `GitHub Skills <https://skills.github.com/>`_
* `Git Basics <https://git-scm.com/book/en/v2/Getting-Started-Git-Basics>`_
* `GitHub Guides <https://guides.github.com/>`_

New to Sphinx?
~~~~~~~~~~~~~~

* `Sphinx Tutorial <https://www.sphinx-doc.org/en/master/tutorial/>`_
* `reStructuredText Primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
* `NumPy Docstring Guide <https://numpydoc.readthedocs.io/>`_

New to eLabFTW?
~~~~~~~~~~~~~~~

* `eLabFTW Documentation <https://doc.elabftw.net/>`_
* `eLabFTW Demo <https://demo.elabftw.net/>`_
* `Installation Guide <https://doc.elabftw.net/install.html>`_

Next Steps
----------

Ready to dive deeper?

* **Learn eLabFTW Integration**: Read the :doc:`elabftw_integration` guide
* **Improve Your Docs**: Check out :doc:`best_practices`
* **Explore the Code**: Browse the :mod:`hplc_analysis` module
* **Contribute**: See `CONTRIBUTING.md <https://github.com/B-Wie/how_to_document_your_reposiory_with_sphinx/blob/main/CONTRIBUTING.md>`_

Deploying to GitHub Pages
--------------------------

This repository includes GitHub Actions automation:

1. **Push to main/master** - Triggers automatic build
2. **Documentation builds** - Sphinx generates HTML
3. **Deploys to GitHub Pages** - Published automatically
4. **View at**: ``https://<username>.github.io/<repository>/``

See `GITHUB_PAGES_SETUP.md <https://github.com/B-Wie/how_to_document_your_reposiory_with_sphinx/blob/main/GITHUB_PAGES_SETUP.md>`_ for setup instructions.

Links and Resources
-------------------

**This Repository**:

* GitHub: https://github.com/B-Wie/how_to_document_your_reposiory_with_sphinx
* Documentation: https://b-wie.github.io/how_to_document_your_reposiory_with_sphinx/
* Issues: https://github.com/B-Wie/how_to_document_your_reposiory_with_sphinx/issues

**Documentation Tools**:

* `Sphinx <https://www.sphinx-doc.org/>`_ - Documentation generator
* `Read the Docs <https://readthedocs.org/>`_ - Documentation hosting
* `NumPy Docstring Standard <https://numpydoc.readthedocs.io/>`_ - Docstring format

**Lab Data Management**:

* `eLabFTW <https://www.elabftw.net/>`_ - Electronic lab notebook
* `Zenodo <https://zenodo.org/>`_ - Research data archiving
* `OSF <https://osf.io/>`_ - Open Science Framework

Contributing
------------

Contributions welcome! This is a learning-friendly project. See `CONTRIBUTING.md <https://github.com/B-Wie/how_to_document_your_reposiory_with_sphinx/blob/main/CONTRIBUTING.md>`_ for:

* How to set up development environment
* Code style guidelines
* Documentation standards
* Pull request process

All skill levels welcome!

License
-------

MIT License - see `LICENSE.md <https://github.com/B-Wie/how_to_document_your_reposiory_with_sphinx/blob/main/LICENSE.md>`_.

Acknowledgments
---------------

Built on best practices from:

* NumPy and SciPy documentation communities
* Sphinx and Read the Docs projects
* eLabFTW development team
* Scientific Python package maintainers
* Research software engineering community

Questions?
----------

* 📖 Read the guides: :doc:`elabftw_integration` and :doc:`best_practices`
* 💬 Start a `discussion <https://github.com/B-Wie/how_to_document_your_reposiory_with_sphinx/discussions>`_
* 🐛 Report `issues <https://github.com/B-Wie/how_to_document_your_reposiory_with_sphinx/issues>`_

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
