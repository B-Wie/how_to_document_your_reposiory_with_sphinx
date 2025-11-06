Documentation Best Practices
============================

This guide provides practical advice for creating high-quality documentation for scientific Python projects, with a focus on beginner-friendly approaches and integration with lab workflows.

Why Documentation Matters
--------------------------

Good documentation:

* 📖 **Helps future you**: Remember what you did 6 months from now
* 🤝 **Enables collaboration**: Team members can understand and use your code
* 🔬 **Ensures reproducibility**: Others can replicate your analysis
* 📊 **Supports publication**: Methods section writes itself
* ⚖️ **Meets compliance**: Required for regulated industries
* 🎓 **Facilitates learning**: Onboard new lab members faster

**Reality check**: Writing documentation takes time, but saves much more time later.

Documentation Types
-------------------

Different documentation serves different purposes:

.. list-table:: Documentation Types
   :widths: 25 35 40
   :header-rows: 1

   * - Type
     - Purpose
     - Examples
   * - Code Documentation
     - Explain how functions work
     - Docstrings, inline comments
   * - User Guide
     - Show how to use the code
     - Tutorials, examples, workflows
   * - API Reference
     - List all functions/classes
     - Auto-generated from docstrings
   * - Theory/Methods
     - Explain the science
     - Equations, algorithms, references
   * - Contributing Guide
     - Help others contribute
     - Setup, style guide, PR process

**For beginners**: Start with docstrings and one example. Expand from there.

Writing Docstrings
------------------

Docstrings are documentation inside your code. Python uses NumPy-style docstrings:

Basic Structure
~~~~~~~~~~~~~~~

.. code-block:: python
   
   def function_name(parameter1, parameter2):
       """
       One-line summary of what the function does.
       
       Longer description with more details about the function,
       its purpose, and how it works. Can span multiple lines.
       
       Parameters
       ----------
       parameter1 : type
           Description of the first parameter.
       parameter2 : type
           Description of the second parameter.
           
       Returns
       -------
       return_type
           Description of what the function returns.
           
       Examples
       --------
       >>> result = function_name(1, 2)
       >>> print(result)
       3
       
       Notes
       -----
       Any additional notes, warnings, or important information.
       
       See Also
       --------
       related_function : Brief description of relation
       """
       # Function implementation
       pass

Docstring Sections
~~~~~~~~~~~~~~~~~~

**Required sections**:

* **Summary line**: One line explaining what it does
* **Parameters**: All input parameters with types
* **Returns**: What the function returns

**Recommended sections**:

* **Examples**: Actual code showing usage
* **Notes**: Important details, limitations, or warnings
* **See Also**: Links to related functions

**Optional sections**:

* **References**: Citations to papers or books
* **Raises**: Exceptions that might be raised

Example: Good Docstring
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
   
   def calculate_peak_area(time, absorbance, start_idx, end_idx):
       """
       Calculate the area under a chromatographic peak.
       
       Uses trapezoidal integration to compute the peak area between
       specified indices. This is a standard method for quantitative
       chromatography analysis.
       
       Parameters
       ----------
       time : np.ndarray
           Time values in minutes (1D array).
       absorbance : np.ndarray
           Absorbance values in mAU (1D array).
       start_idx : int
           Index of peak start in the data arrays.
       end_idx : int
           Index of peak end in the data arrays.
           
       Returns
       -------
       area : float
           Peak area in mAU·min.
           
       Examples
       --------
       >>> time = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
       >>> absorbance = np.array([2.0, 5.0, 8.0, 5.0, 2.0])
       >>> area = calculate_peak_area(time, absorbance, 0, 4)
       >>> print(f"Peak area: {area:.2f} mAU·min")
       Peak area: 2.00 mAU·min
       
       Notes
       -----
       For eLabFTW integration, document integration parameters
       (start/end indices, baseline correction) in the experiment
       record for full traceability.
       
       References
       ----------
       .. [1] Snyder, L. R., et al. (2010). Introduction to Modern
              Liquid Chromatography. Wiley.
       """
       return np.trapezoid(absorbance[start_idx:end_idx+1], 
                          time[start_idx:end_idx+1])

Type Hints
~~~~~~~~~~

Use type hints for clarity:

.. code-block:: python
   
   from typing import Tuple, List, Optional
   import numpy as np
   
   def find_peaks(time: np.ndarray, 
                  absorbance: np.ndarray,
                  threshold: float = 10.0) -> List[dict]:
       """
       Find peaks in chromatogram data.
       
       Parameters
       ----------
       time : np.ndarray
           Time values.
       absorbance : np.ndarray
           Absorbance values.
       threshold : float, optional
           Minimum peak height (default: 10.0).
           
       Returns
       -------
       list of dict
           Each dict contains 'retention_time', 'height', 'area'.
       """
       pass

Type hints help:
* Users understand what inputs are expected
* IDEs provide better autocomplete
* Tools can catch type errors

Writing User Guides
-------------------

User guides show *how* to use your code. Key principles:

Start with Installation
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst
   
   Installation
   ============
   
   Requirements
   ------------
   
   * Python 3.7 or higher
   * NumPy 1.19.0 or higher
   * eLabFTW instance (optional, for full workflow)
   
   Install
   -------
   
   Clone the repository:
   
   .. code-block:: bash
      
      git clone https://github.com/username/project.git
      cd project
   
   Install dependencies:
   
   .. code-block:: bash
      
      pip install -r requirements.txt

Provide Quick Start
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst
   
   Quick Start
   ===========
   
   Analyze an HPLC chromatogram in 3 steps:
   
   1. **Load data**:
   
   .. code-block:: python
      
      from hplc_analysis import load_chromatogram
      time, absorbance = load_chromatogram('data/sample.txt')
   
   2. **Find peaks**:
   
   .. code-block:: python
      
      from hplc_analysis import find_peaks
      peaks = find_peaks(time, absorbance, threshold=50.0)
   
   3. **View results**:
   
   .. code-block:: python
      
      for i, peak in enumerate(peaks, 1):
          print(f"Peak {i}: {peak['retention_time']:.2f} min")

Include Complete Examples
~~~~~~~~~~~~~~~~~~~~~~~~~~

Show realistic, complete workflows:

.. code-block:: rst
   
   Complete Workflow Example
   =========================
   
   This example shows the full analysis pipeline from data loading
   to results reporting, including eLabFTW integration.
   
   Step 1: Reference eLabFTW Experiment
   -------------------------------------
   
   Before starting, note your eLabFTW experiment ID::
   
       Experiment: #67890
       URL: https://your-instance.org/experiments.php?mode=view&id=67890
   
   Step 2: Load and Analyze Data
   ------------------------------
   
   .. code-block:: python
      
      import numpy as np
      from hplc_analysis import analyze_chromatogram
      
      # Reference eLabFTW in code
      # Experiment: https://your-instance.org/experiments.php?mode=view&id=67890
      
      results = analyze_chromatogram('data/sample.txt', threshold=50.0)
      
      print(f"Found {results['n_peaks']} peaks")
      for peak in results['peaks']:
          print(f"  RT: {peak['retention_time']:.2f} min")
          print(f"  Area: {peak['area']:.1f} mAU·min")
   
   Step 3: Document in eLabFTW
   ----------------------------
   
   Upload results to your eLabFTW experiment and include:
   
   * Peak table (CSV export)
   * Analysis parameters used
   * GitHub commit hash for reproducibility

Using Sphinx
------------

Sphinx converts documentation to beautiful HTML. Key concepts:

reStructuredText Basics
~~~~~~~~~~~~~~~~~~~~~~~~

reStructuredText (.rst files) is a markup language:

.. code-block:: rst
   
   Section Heading
   ===============
   
   Subsection
   ----------
   
   **Bold text** and *italic text*
   
   Bullet lists:
   
   * First item
   * Second item
   * Third item
   
   Numbered lists:
   
   1. Step one
   2. Step two
   3. Step three
   
   Code blocks:
   
   .. code-block:: python
      
      import numpy as np
      x = np.array([1, 2, 3])
   
   External links:
   
   `Python <https://python.org/>`_
   
   Cross-references:
   
   See :doc:`other_page` for more details.
   See :func:`module.function` for API docs.

Mathematical Equations
~~~~~~~~~~~~~~~~~~~~~~

Use LaTeX syntax for equations:

.. code-block:: rst
   
   The peak area :math:`A` is calculated as:
   
   .. math::
      
      A = \int_{t_1}^{t_2} h(t) \, dt
   
   where :math:`h(t)` is the absorbance at time :math:`t`.

This renders as:

The peak area :math:`A` is calculated as:

.. math::
   
   A = \int_{t_1}^{t_2} h(t) \, dt

where :math:`h(t)` is the absorbance at time :math:`t`.

Cross-References
~~~~~~~~~~~~~~~~

Link between documentation pages:

.. code-block:: rst
   
   # Link to another page
   See :doc:`elabftw_integration` for details.
   
   # Link to a section
   See :ref:`writing-docstrings` for examples.
   
   # Link to a function
   Use :func:`hplc_analysis.find_peaks` to detect peaks.
   
   # Link to a module
   See :mod:`hplc_analysis` for all analysis functions.

Auto-Generated API Docs
~~~~~~~~~~~~~~~~~~~~~~~

Sphinx can automatically generate API documentation from docstrings:

.. code-block:: rst
   
   API Reference
   =============
   
   HPLC Analysis Module
   --------------------
   
   .. automodule:: hplc_analysis
      :members:
      :undoc-members:
      :show-inheritance:

This creates a complete API reference from your docstrings.

Organizing Documentation
-------------------------

Structure for Small Projects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text
   
   docs/source/
   ├── index.rst              # Homepage with quick start
   ├── installation.rst       # How to install
   ├── tutorial.rst           # Step-by-step guide
   ├── api.rst                # Auto-generated API docs
   └── elabftw.rst           # eLabFTW integration guide

Structure for Larger Projects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text
   
   docs/source/
   ├── index.rst
   ├── getting_started/
   │   ├── installation.rst
   │   ├── quickstart.rst
   │   └── configuration.rst
   ├── user_guide/
   │   ├── basic_usage.rst
   │   ├── advanced_topics.rst
   │   └── elabftw_integration.rst
   ├── api_reference/
   │   ├── analysis.rst
   │   ├── visualization.rst
   │   └── utilities.rst
   └── developer_guide/
       ├── contributing.rst
       ├── testing.rst
       └── release_process.rst

**For beginners**: Start with the simple structure. Reorganize as you grow.

eLabFTW Integration in Docs
----------------------------

Show Complete Workflows
~~~~~~~~~~~~~~~~~~~~~~~~

Document the full cycle:

.. code-block:: rst
   
   Laboratory Workflow
   ===================
   
   Before Running Analysis
   -----------------------
   
   1. Create eLabFTW experiment record
   2. Document method and parameters
   3. Upload raw data files
   4. Note experiment ID for reference
   
   During Analysis
   ---------------
   
   1. Reference eLabFTW ID in code header
   2. Load data with eLabFTW references
   3. Run analysis with documented parameters
   4. Save intermediate results
   
   After Analysis
   --------------
   
   1. Upload results to eLabFTW
   2. Link GitHub commit for traceability
   3. Document analysis parameters used
   4. Review and validate results

Provide Examples with eLabFTW Links
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst
   
   Example Analysis
   ================
   
   This example analyzes HPLC data from eLabFTW experiment #67890:
   
   https://your-elabftw-instance.org/experiments.php?mode=view&id=67890
   
   The experiment used equipment EQUIP-12345 (HPLC-UV system):
   
   https://your-elabftw-instance.org/database.php?mode=view&id=EQUIP-12345
   
   Method details, calibration data, and quality control results
   are documented in the eLabFTW records.

Document Where Things Go
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst
   
   Data Organization
   =================
   
   .. list-table::
      :widths: 30 35 35
      :header-rows: 1
   
      * - Data Type
        - Store In
        - Notes
      * - Raw instrument data
        - eLabFTW (attached to experiment)
        - Original files, unmodified
      * - Analysis scripts
        - GitHub repository
        - Version controlled
      * - Processed results
        - eLabFTW (attached to experiment)
        - With GitHub commit reference
      * - Protocols/methods
        - eLabFTW (database)
        - Shared across experiments
      * - Small test data
        - GitHub (data/ folder)
        - For examples and testing

Version Control for Documentation
----------------------------------

Documentation needs version control too:

Commit Documentation Changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
   
   # Good commit messages for docs
   git commit -m "Add HPLC analysis tutorial with examples"
   git commit -m "Fix broken links in API reference"
   git commit -m "Update installation instructions for Windows"

Keep Docs Synchronized
~~~~~~~~~~~~~~~~~~~~~~~

When changing code:

1. **Update docstrings** if function signatures change
2. **Update examples** if usage patterns change
3. **Update tutorials** if workflows change
4. **Check cross-references** still work
5. **Rebuild docs** to catch issues

Version Documentation
~~~~~~~~~~~~~~~~~~~~~

For releases, document the version:

.. code-block:: python
   
   # In docs/source/conf.py
   version = '1.0'  # Short X.Y version
   release = '1.0.0'  # Full version

Tag releases in Git:

.. code-block:: bash
   
   git tag -a v1.0.0 -m "Version 1.0.0 release"
   git push origin v1.0.0

Common Mistakes to Avoid
-------------------------

❌ **No Documentation**

"The code is self-documenting" - No, it's not.

✅ **Fix**: Start with minimal docstrings. Expand gradually.

❌ **Outdated Documentation**

Documentation describes old version of code.

✅ **Fix**: Update docs when changing code. Test examples.

❌ **Assuming Too Much Knowledge**

"Obviously you need to preprocess the data first..."

✅ **Fix**: Write for beginners. Explain each step.

❌ **No Examples**

Just parameter lists without showing usage.

✅ **Fix**: Add at least one working example per function.

❌ **Broken Links**

Cross-references point to nonexistent pages.

✅ **Fix**: Build docs locally and check for warnings.

❌ **Inconsistent Style**

Random mix of formatting and organization.

✅ **Fix**: Follow this template. Be consistent.

Tools and Resources
-------------------

Documentation Tools
~~~~~~~~~~~~~~~~~~~

* **Sphinx**: Main documentation generator
* **sphinx-rtd-theme**: Professional Read the Docs theme
* **napoleon**: NumPy docstring support
* **autodoc**: Auto-generate API docs
* **doctest**: Test code examples in docstrings

Checking Documentation
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
   
   # Build and check for warnings
   cd docs
   make clean
   make html
   
   # Check for broken links
   make linkcheck
   
   # Spell check (if aspell installed)
   find source -name "*.rst" -exec aspell check {} \;

Learning Resources
~~~~~~~~~~~~~~~~~~

* `Sphinx Documentation <https://www.sphinx-doc.org/>`_
* `NumPy Docstring Guide <https://numpydoc.readthedocs.io/>`_
* `Write the Docs <https://www.writethedocs.org/>`_
* `Documentation Guide <https://www.divio.com/blog/documentation/>`_

Example Documentation Checklist
--------------------------------

Use this checklist for your documentation:

.. code-block:: text
   
   Code Documentation
   ==================
   
   [ ] All functions have docstrings
   [ ] Docstrings include Parameters and Returns
   [ ] At least one example per main function
   [ ] Type hints on function signatures
   [ ] Complex logic has inline comments
   [ ] eLabFTW references where applicable
   
   User Guide
   ==========
   
   [ ] Installation instructions included
   [ ] Quick start example provided
   [ ] Complete workflow example shown
   [ ] eLabFTW integration explained
   [ ] Troubleshooting section exists
   [ ] Links to external resources
   
   API Reference
   =============
   
   [ ] Auto-generated from docstrings
   [ ] All modules documented
   [ ] Cross-references work
   [ ] Examples build without errors
   
   Build and Deploy
   ================
   
   [ ] Builds locally without errors
   [ ] No broken links (linkcheck passes)
   [ ] Equations render correctly
   [ ] GitHub Actions workflow configured
   [ ] Deploys to GitHub Pages

Getting Help
------------

If you're stuck on documentation:

1. **Check existing examples** in this repository
2. **Search Sphinx documentation** for specific features
3. **Look at similar projects** (NumPy, SciPy, pandas)
4. **Ask in discussions** on GitHub
5. **Start simple** and improve iteratively

Remember: **Perfect documentation doesn't exist**. Good enough documentation that actually exists is infinitely better than perfect documentation that never gets written.

See Also
--------

* :doc:`index` - Main documentation
* :doc:`elabftw_integration` - eLabFTW integration guide
* :mod:`hplc_analysis` - Example code with complete documentation
