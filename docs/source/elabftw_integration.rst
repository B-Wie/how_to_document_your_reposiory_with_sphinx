eLabFTW Integration Guide
=========================

This guide explains how to integrate eLabFTW (electronic lab notebook) with your Python analysis code and documentation to create a complete, traceable workflow from experiment to results.

What is eLabFTW?
----------------

`eLabFTW <https://www.elabftw.net/>`_ is a free, open-source electronic lab notebook (ELN) designed specifically for research laboratories. It provides:

* **Experiment documentation**: Record protocols, observations, and results
* **Equipment database**: Track instruments, specifications, and maintenance
* **Data management**: Store and organize research data with versioning
* **Collaboration tools**: Share experiments with team members
* **Compliance features**: Meet FDA 21 CFR Part 11, GLP, and other regulations
* **API access**: Integrate with other tools and workflows

Unlike generic lab notebooks, eLabFTW is designed by scientists for scientists, with features specifically for research reproducibility and traceability.

Why Integrate eLabFTW with GitHub?
-----------------------------------

Combining eLabFTW with GitHub creates a powerful research workflow:

.. list-table:: Complementary Strengths
   :widths: 30 35 35
   :header-rows: 1

   * - Aspect
     - eLabFTW Handles
     - GitHub Handles
   * - Data Storage
     - Raw experimental data, images
     - Code, small test datasets
   * - Documentation
     - Protocols, observations, notes
     - Code documentation, APIs
   * - Version Control
     - Data versioning, timestamps
     - Code versioning, branches
   * - Sharing
     - Within lab team, with stamp
     - Open source, public repos
   * - Compliance
     - Timestamps, signatures, audit logs
     - Code review, change tracking

**Key Principle**: Use each tool for what it does best, and link them together.

The Integrated Workflow
------------------------

Step 1: Document Experiment in eLabFTW
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before running an experiment:

1. **Create experiment record** in eLabFTW
   
   * Document the protocol and method
   * List equipment and materials needed
   * Note any deviations from standard procedures

2. **Link equipment records**
   
   * Reference instruments from the database
   * Include calibration information
   * Note any maintenance or issues

3. **Note the experiment ID**
   
   * eLabFTW assigns a unique ID (e.g., #67890)
   * This becomes your persistent reference
   * Use it in all related files and analyses

**Example eLabFTW Experiment Entry**::

    Title: HPLC Analysis of Compound Mixture A
    
    Protocol:
    - Column: C18, 250x4.6mm (Equipment DB ID: EQUIP-12345)
    - Mobile phase: 60% MeOH / 40% Water
    - Flow rate: 1.0 mL/min
    - Detection: UV 254nm
    - Injection volume: 20 µL
    
    Expected peaks: 2 (compound A at ~2 min, compound B at ~6 min)

Step 2: Collect Data with eLabFTW References
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When collecting data from instruments:

1. **Include eLabFTW ID in file headers**

.. code-block:: text
   
   # HPLC Chromatogram Data
   # Experiment: eLabFTW #67890 
   # URL: https://your-elabftw-instance.org/experiments.php?mode=view&id=67890
   # Equipment: HPLC-UV (eLabFTW DB ID: EQUIP-12345)
   # Date: 2025-01-15
   # Analyst: Jane Doe
   
   # Time(min)    Absorbance(mAU)
   0.00    2.1
   0.10    2.3
   ...

2. **Upload raw data to eLabFTW**
   
   * Attach instrument output files to experiment
   * Keep original file names with timestamps
   * Document any data processing steps

3. **Record observations**
   
   * Note any unusual results
   * Document troubleshooting steps
   * Link to equipment maintenance if issues arise

Step 3: Write Analysis Code with References
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Your Python analysis scripts should reference eLabFTW:

.. code-block:: python
   
   """
   HPLC Chromatogram Analysis
   
   This script analyzes HPLC data from experiment #67890.
   
   eLabFTW References
   ------------------
   Experiment: https://your-elabftw-instance.org/experiments.php?mode=view&id=67890
   Equipment: https://your-elabftw-instance.org/database.php?mode=view&id=EQUIP-12345
   
   Method details, raw data, and protocols are stored in eLabFTW.
   """
   
   import numpy as np
   from pathlib import Path
   
   def load_chromatogram(filepath):
       """
       Load HPLC data from file.
       
       Parameters
       ----------
       filepath : str
           Path to data file. File should include eLabFTW experiment
           reference in header for traceability.
       
       Notes
       -----
       Always reference the eLabFTW experiment ID in data files:
       # Experiment: eLabFTW #67890
       """
       # Implementation here
       pass

**Best Practices for Code Comments**:

* Include eLabFTW URL at the top of analysis scripts
* Reference equipment IDs when method-specific
* Link to protocols for parameter explanations
* Document any deviations from eLabFTW method

Step 4: Document Analysis in Sphinx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In your Sphinx documentation, link to eLabFTW records:

.. code-block:: rst
   
   HPLC Analysis Example
   =====================
   
   This example analyzes data from eLabFTW experiment #67890:
   https://your-elabftw-instance.org/experiments.php?mode=view&id=67890
   
   Method
   ------
   
   The HPLC method is documented in eLabFTW. Key parameters:
   
   * **Equipment**: HPLC-UV system (eLabFTW DB: EQUIP-12345)
   * **Column**: C18, 250x4.6mm
   * **Mobile phase**: See eLabFTW for complete composition
   * **Flow rate**: 1.0 mL/min
   
   For complete method details, calibration information, and quality
   control data, refer to the eLabFTW equipment record:
   https://your-elabftw-instance.org/database.php?mode=view&id=EQUIP-12345

Step 5: Return Results to eLabFTW
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After completing analysis:

1. **Upload results files**
   
   * CSV/Excel files with processed data
   * Figures and plots
   * Statistical summaries

2. **Link GitHub commit**
   
   * Include GitHub commit hash in eLabFTW
   * Link to specific code version used
   * Ensures reproducibility

3. **Document analysis parameters**
   
   * Threshold values used
   * Integration parameters
   * Any manual corrections

**Example eLabFTW Results Entry**::

    Analysis Results (2025-01-15)
    
    Code: https://github.com/username/repo/commit/abc123def
    Script: src/hplc_analysis.py
    
    Results:
    - Peak 1: RT = 2.10 min, Area = 101.2 mAU·min (Compound A)
    - Peak 2: RT = 5.70 min, Area = 139.0 mAU·min (Compound B)
    - Resolution: Rs = 1.71 (baseline separation)
    
    Analysis parameters:
    - Peak threshold: 50.0 mAU
    - Baseline: 2.4 mAU
    - Integration: Trapezoidal method
    
    Files attached:
    - chromatogram_plot.png
    - peak_table.csv
    - analysis_summary.json

Persistent References: IDs vs URLs
-----------------------------------

eLabFTW provides two types of references:

Experiment IDs
~~~~~~~~~~~~~~

* **Format**: Integer (e.g., 67890)
* **Short reference**: "#67890"
* **URL**: ``https://your-instance.org/experiments.php?mode=view&id=67890``

**Use when**: Referencing within your organization, brief mentions in code comments

Database Item IDs
~~~~~~~~~~~~~~~~~

* **Format**: Integer with prefix (e.g., EQUIP-12345)
* **Categories**: Equipment, protocols, resources
* **URL**: ``https://your-instance.org/database.php?mode=view&id=12345``

**Use when**: Referencing equipment, standard protocols, shared resources

Permanent URLs
~~~~~~~~~~~~~~

eLabFTW IDs are permanent and survive:

* ✅ Server migrations
* ✅ Database backups and restores
* ✅ File reorganizations
* ✅ Archiving and long-term storage

**Best practice**: Always use full URLs in documentation and data files for maximum permanence.

Example: Complete Workflow
---------------------------

Here's a complete example showing the integrated workflow:

1. **eLabFTW Experiment #67890**
   
   Protocol documents HPLC method and uploads raw data file
   ``sample_hplc_chromatogram.txt``

2. **GitHub Repository**
   
   Contains analysis code in ``src/hplc_analysis.py`` with eLabFTW references

3. **Data File** (``data/sample_hplc_chromatogram.txt``)

.. code-block:: text
   
   # HPLC Chromatogram Data
   # Experiment: eLabFTW #67890
   # URL: https://your-elabftw-instance.org/experiments.php?mode=view&id=67890
   # Equipment: HPLC-UV (eLabFTW ID: EQUIP-12345)
   ...data follows...

4. **Python Script** (``src/hplc_analysis.py``)

.. code-block:: python
   
   """
   HPLC Analysis
   
   eLabFTW Experiment: https://your-instance.org/experiments.php?mode=view&id=67890
   eLabFTW Equipment: https://your-instance.org/database.php?mode=view&id=EQUIP-12345
   """
   
   results = analyze_chromatogram('data/sample_hplc_chromatogram.txt')
   # Analysis code...

5. **Results Back to eLabFTW**
   
   Upload results with link: ``GitHub commit: abc123def456``

This creates a complete, bidirectional link between experiment and analysis.

API Integration (Advanced)
---------------------------

For advanced users, eLabFTW provides a REST API for programmatic access:

Reading Data
~~~~~~~~~~~~

.. code-block:: python
   
   import requests
   
   # Authentication
   api_key = "your_api_key_here"  # From eLabFTW user account
   headers = {"Authorization": f"Bearer {api_key}"}
   base_url = "https://your-elabftw-instance.org/api/v2"
   
   # Get experiment data
   exp_id = 67890
   response = requests.get(f"{base_url}/experiments/{exp_id}", headers=headers)
   experiment = response.json()
   
   print(f"Title: {experiment['title']}")
   print(f"Date: {experiment['date']}")

Uploading Results
~~~~~~~~~~~~~~~~~

.. code-block:: python
   
   # Upload a file to experiment
   exp_id = 67890
   files = {'file': open('results.csv', 'rb')}
   response = requests.post(
       f"{base_url}/experiments/{exp_id}/uploads",
       headers=headers,
       files=files
   )

**Note**: Store API keys securely, never commit them to Git repositories. Use environment variables or secure configuration files.

Security Considerations
-----------------------

When integrating eLabFTW and GitHub:

Public vs Private Repositories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Public repos**: Share code, NOT sensitive data
* **Private repos**: Can include more details, but still avoid patient data
* **eLabFTW**: Keep all sensitive experimental data here with access controls

What NOT to Include in GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

❌ **Never commit**:

* Patient/subject identifiable information
* Proprietary compound structures
* Unpublished sensitive results
* eLabFTW API keys or passwords
* Complete raw data sets (link to eLabFTW instead)

✅ **Safe to include**:

* Analysis code and scripts
* Documentation and examples
* Small test/demo datasets
* Public protocols and methods
* Links to eLabFTW records (if instance is internal)

Compliance and Regulations
---------------------------

This workflow supports regulatory compliance:

FDA 21 CFR Part 11
~~~~~~~~~~~~~~~~~~

* **Electronic records**: eLabFTW provides timestamps and signatures
* **Audit trails**: Both eLabFTW and Git track all changes
* **Access controls**: eLabFTW manages user permissions
* **Data integrity**: Version control prevents unauthorized changes

Good Laboratory Practice (GLP)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Traceability**: Direct links from results to raw data
* **Documentation**: Complete method documentation in eLabFTW
* **Reproducibility**: Code in Git + data in eLabFTW = full reproduction
* **Archives**: Both systems support long-term data retention

Tips for Lab Implementation
----------------------------

Getting Started
~~~~~~~~~~~~~~~

1. **Start small**: Use for one project or technique first
2. **Create templates**: Make eLabFTW experiment templates for common procedures
3. **Train team**: Ensure everyone knows how to reference eLabFTW in code
4. **Document workflow**: Create lab-specific guidelines based on this template
5. **Review regularly**: Check that links are working and practices are followed

Lab-Specific Guidelines
~~~~~~~~~~~~~~~~~~~~~~~

Consider creating a lab document that specifies:

* Your eLabFTW instance URL
* Naming conventions for experiment IDs
* Where to store different data types
* Required metadata in data files
* Code review requirements
* Documentation standards

Example Lab Template
~~~~~~~~~~~~~~~~~~~~

Create a template in your repository (``docs/lab_template.md``):

.. code-block:: markdown
   
   # Lab Analysis Template
   
   ## Before You Start
   
   - [ ] Create eLabFTW experiment record
   - [ ] Note experiment ID: ___________
   - [ ] Document equipment used (with DB IDs)
   - [ ] Upload raw data files to eLabFTW
   
   ## During Analysis
   
   - [ ] Reference eLabFTW ID in code header
   - [ ] Include eLabFTW URL in comments
   - [ ] Test code with sample data
   - [ ] Document any deviations or issues
   
   ## After Analysis
   
   - [ ] Upload results to eLabFTW
   - [ ] Link GitHub commit in eLabFTW
   - [ ] Verify all links work
   - [ ] Archive complete workflow

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Problem**: eLabFTW URLs are long and unwieldy in code

**Solution**: Use short experiment IDs in comments with full URL in file headers

.. code-block:: python
   
   # Header: Full URL
   """
   Experiment: https://your-instance.org/experiments.php?mode=view&id=67890
   """
   
   # Inline comments: Short reference
   def analyze_peak():
       """Analyze peak (see eLabFTW #67890 for method)."""
       pass

**Problem**: Team members forget to reference eLabFTW

**Solution**: Add checks to your code:

.. code-block:: python
   
   def validate_data_file(filepath):
       """Check that data file contains eLabFTW reference."""
       with open(filepath) as f:
           header = f.read(500)  # First 500 chars
           if "elabftw" not in header.lower():
               print("WARNING: No eLabFTW reference found in file header")

**Problem**: eLabFTW instance URL changed after migration

**Solution**: Use relative paths where possible, document migration in Git

Further Resources
-----------------

eLabFTW Documentation
~~~~~~~~~~~~~~~~~~~~~

* `Official Documentation <https://doc.elabftw.net/>`_
* `API Documentation <https://doc.elabftw.net/api/>`_
* `User Guide <https://doc.elabftw.net/user-guide.html>`_

Related Tools
~~~~~~~~~~~~~

* `Jupyter Notebooks <https://jupyter.org/>`_ - Can embed eLabFTW links in notebooks
* `Binder <https://mybinder.org/>`_ - Share reproducible computational environments
* `Zenodo <https://zenodo.org/>`_ - Archive code and data with DOIs

See Also
--------

* :doc:`index` - Main documentation
* :doc:`best_practices` - Documentation best practices
* :mod:`hplc_analysis` - Example analysis code with eLabFTW integration
