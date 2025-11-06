Publication Context
===================

This page provides information about publications, citations, and research context
related to this repository and its documentation.

About This Repository
---------------------

This repository serves as a comprehensive tutorial for documenting scientific Python 
projects using Sphinx. It demonstrates best practices for creating professional, 
publication-ready documentation that includes:

* API documentation with NumPy-style docstrings
* Mathematical equations and formulas
* Cross-references between documentation sections
* External links to resources and related work
* Example code and usage demonstrations

The repository is maintained at: https://github.com/B-Wie/how_to_document_your_reposiory_with_sphinx

Repository Structure
--------------------

The project is organized as follows:

.. code-block:: text
   
   .
   ├── src/
   │   └── sample_module.py      # Example Python module with docstrings
   ├── docs/
   │   ├── source/
   │   │   ├── conf.py           # Sphinx configuration
   │   │   ├── index.rst         # Documentation homepage
   │   │   ├── experiment_setup.rst  # Experimental methodology
   │   │   └── publication_context.rst  # This file
   │   ├── Makefile              # Build commands (Unix)
   │   ├── make.bat              # Build commands (Windows)
   │   └── README.md             # Deployment information
   ├── requirements.txt          # Python dependencies
   └── README.md                 # Main project documentation

Citation
--------

If you use this repository or adapt its documentation structure for your research, 
please cite it as follows:

.. code-block:: bibtex
   
   @software{sphinx_documentation_tutorial,
     author = {B-Wie},
     title = {How to Document Your Repository with Sphinx},
     year = {2025},
     url = {https://github.com/B-Wie/how_to_document_your_reposiory_with_sphinx},
     note = {Tutorial for scientific Python documentation}
   }

Related Publications
--------------------

This documentation methodology is inspired by best practices from the scientific 
Python community. While this specific repository is a tutorial, it follows 
conventions established in major scientific software projects.

**Recommended Reading:**

* Documentation practices align with recommendations from the 
  `SciPy Documentation Guide <https://numpy.org/doc/stable/dev/howto-docs.html>`_
* NumPy-style docstrings follow the `NumPy Documentation Standard 
  <https://numpydoc.readthedocs.io/en/latest/format.html>`_
* Sphinx extensions used are documented in the 
  `Sphinx Documentation <https://www.sphinx-doc.org/>`_

Software Documentation
----------------------

This project demonstrates several Sphinx extensions essential for scientific documentation:

**sphinx.ext.autodoc**
   Automatically generates documentation from Python docstrings. See the 
   API documentation generated from :mod:`sample_module`.

**sphinx.ext.napoleon**
   Enables parsing of NumPy-style docstrings, making them more readable than 
   traditional reStructuredText. Example: :func:`sample_module.linear_regression`.

**sphinx.ext.viewcode**
   Adds links to highlighted source code, allowing readers to view implementation 
   details directly. Try clicking the "[source]" links in the API documentation.

**sphinx.ext.mathjax**
   Renders mathematical equations using MathJax. See equations in 
   :doc:`experiment_setup` for examples.

Documentation Workflow
----------------------

The documentation generation workflow is as follows:

1. **Write Code** - Implement functions with comprehensive NumPy-style docstrings
2. **Create RST Files** - Write narrative documentation in reStructuredText format
3. **Configure Sphinx** - Set up ``conf.py`` with appropriate extensions
4. **Build Locally** - Run ``make html`` to preview documentation
5. **Deploy** - Push to GitHub and let GitHub Actions deploy to GitHub Pages

For detailed setup instructions, see the main :doc:`index` page.

GitHub Pages Deployment
-----------------------

This repository uses GitHub Actions to automatically build and deploy documentation 
to GitHub Pages. The deployment process:

* Triggers on every push to the ``main`` or ``master`` branch
* Installs dependencies from ``requirements.txt``
* Builds HTML documentation using Sphinx
* Deploys to the ``gh-pages`` branch
* Serves at: https://b-wie.github.io/how_to_document_your_reposiory_with_sphinx/

See the ``.github/workflows/deploy-docs.yml`` file for workflow details.

Contributing to Documentation
-----------------------------

Documentation contributions are welcome! To contribute:

1. Fork the repository on GitHub
2. Clone your fork locally
3. Create a new branch for your changes
4. Make documentation improvements
5. Test locally with ``make html``
6. Submit a pull request

For more details, see the `GitHub repository 
<https://github.com/B-Wie/how_to_document_your_reposiory_with_sphinx>`_.

Best Practices
--------------

When documenting scientific software, follow these best practices:

**Code Documentation**
   * Use NumPy-style docstrings for all public functions and classes
   * Include parameter types, return values, and examples
   * Document exceptions and edge cases
   * Add mathematical notation when relevant

**Narrative Documentation**
   * Explain the scientific context and methodology
   * Provide installation instructions and system requirements
   * Include usage examples with expected outputs
   * Link to external resources and references

**Maintenance**
   * Keep documentation synchronized with code changes
   * Update examples when APIs change
   * Test documentation builds in CI/CD pipelines
   * Version documentation alongside code releases

See Also
--------

* :doc:`experiment_setup` - Detailed experimental methodology and implementation
* :doc:`index` - Documentation homepage with quick start guide
* :mod:`sample_module` - API documentation for example code

External Resources
------------------

* `Write the Docs <https://www.writethedocs.org/>`_ - Community for documentation creators
* `Documenting Python Code <https://realpython.com/documenting-python-code/>`_ - Tutorial on Python documentation
* `The Good Docs Project <https://thegooddocsproject.dev/>`_ - Templates for technical documentation

License and Acknowledgments
----------------------------

This tutorial repository is provided as an educational resource for the scientific 
Python community. It builds upon documentation practices developed by:

* The NumPy and SciPy development teams
* The Sphinx development community  
* The Read the Docs project
* Scientific Python package maintainers

For questions or suggestions about this documentation, please open an issue on 
`GitHub <https://github.com/B-Wie/how_to_document_your_reposiory_with_sphinx/issues>`_.
