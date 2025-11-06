# How to Document Your Repository with Sphinx

A comprehensive tutorial for creating professional scientific Python documentation using Sphinx, complete with equations, cross-references, API documentation, and automated GitHub Pages deployment.

## Overview

This repository demonstrates how to build publication-quality documentation for scientific Python projects. It provides a complete working example with:

- ✅ **NumPy-style docstrings** for clean, readable API documentation
- ✅ **Mathematical equations** rendered with LaTeX/MathJax
- ✅ **Cross-references** between documentation sections and code
- ✅ **External links** to resources and related work
- ✅ **Automated deployment** to GitHub Pages via GitHub Actions
- ✅ **Professional theme** using Read the Docs styling

Perfect for researchers, data scientists, and developers who want to document their Python code professionally.

## Features

### 📚 Complete Documentation Stack

- **Sphinx** with autodoc, napoleon, viewcode, and mathjax extensions
- **Read the Docs theme** for clean, professional appearance
- **Automatic API generation** from Python docstrings
- **GitHub Actions workflow** for continuous deployment

### 🔢 Scientific Documentation Support

- LaTeX equations with MathJax rendering
- NumPy-style docstring format
- Tables, figures, and code blocks
- Cross-references and citations

### 🤖 Automated Deployment

- Builds automatically on push to main/master
- Deploys to GitHub Pages
- No manual intervention required
- Live at: https://b-wie.github.io/how_to_document_your_reposiory_with_sphinx/

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `sphinx>=7.0.0` - Documentation generator
- `sphinx-rtd-theme>=1.3.0` - Read the Docs theme

### 2. Build Documentation Locally

```bash
cd docs
make html
```

### 3. View Documentation

Open `docs/build/html/index.html` in your web browser.

## Repository Structure

```
.
├── src/
│   └── sample_module.py      # Example Python module with NumPy-style docstrings
├── docs/
│   ├── source/
│   │   ├── conf.py                  # Sphinx configuration
│   │   ├── index.rst                # Documentation homepage
│   │   ├── experiment_setup.rst     # Example: equations, tables, links
│   │   ├── publication_context.rst  # Example: citations, repositories
│   │   ├── _static/                 # Static files (CSS, images, etc.)
│   │   └── _templates/              # Custom templates
│   ├── Makefile                     # Build commands (Unix)
│   ├── make.bat                     # Build commands (Windows)
│   └── README.md                    # Documentation deployment info
├── .github/
│   └── workflows/
│       └── deploy-docs.yml          # GitHub Actions deployment workflow
├── requirements.txt                  # Python dependencies
└── README.md                         # This file
```

## Tutorial: Creating Your Own Documentation

### Step 1: Set Up Sphinx

If starting from scratch, initialize Sphinx in your repository:

```bash
mkdir docs
cd docs
sphinx-quickstart
```

Answer the prompts:
- Separate source and build directories? **Yes**
- Project name: **Your Project Name**
- Author name: **Your Name**
- Project version: **1.0.0**
- Project language: **en**

### Step 2: Configure Sphinx Extensions

Edit `docs/source/conf.py` and add these extensions:

```python
extensions = [
    'sphinx.ext.autodoc',      # Auto-generate API docs from docstrings
    'sphinx.ext.napoleon',     # Support for NumPy-style docstrings
    'sphinx.ext.viewcode',     # Add links to source code
    'sphinx.ext.mathjax',      # Render LaTeX equations
]
```

Add your source code directory to the Python path:

```python
import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))
```

Set the theme:

```python
html_theme = 'sphinx_rtd_theme'
```

### Step 3: Write NumPy-Style Docstrings

Document your Python code using NumPy-style docstrings:

```python
def calculate_mean(data):
    """
    Calculate the arithmetic mean of a dataset.
    
    Parameters
    ----------
    data : array_like
        Input data as a 1D array or list.
        
    Returns
    -------
    float
        The mean of the input data.
        
    Examples
    --------
    >>> calculate_mean([1, 2, 3, 4, 5])
    3.0
    
    Notes
    -----
    Uses NumPy's mean implementation for efficiency.
    """
    return np.mean(data)
```

### Step 4: Create Documentation Pages

Create `.rst` files in `docs/source/` for your documentation:

**Example: docs/source/api.rst**
```rst
API Documentation
=================

.. automodule:: your_module
   :members:
   :undoc-members:
   :show-inheritance:
```

**Adding Mathematical Equations**
```rst
The formula is:

.. math::
   
   E = mc^2

where :math:`E` is energy, :math:`m` is mass, and :math:`c` is the speed of light.
```

**Adding Cross-References**
```rst
See :doc:`other_page` for more information.

Use :func:`your_module.function_name` to reference a function.
```

### Step 5: Update the Table of Contents

Add your pages to `docs/source/index.rst`:

```rst
.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   installation
   usage
   api
```

### Step 6: Build and Test

```bash
cd docs
make clean
make html
```

Check for warnings or errors and fix them.

### Step 7: Set Up GitHub Actions Deployment

Create `.github/workflows/deploy-docs.yml`:

```yaml
name: Deploy Sphinx Documentation

on:
  push:
    branches:
      - main
      - master
  workflow_dispatch:

permissions:
  contents: write

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Build documentation
      run: |
        cd docs
        make html
    
    - name: Add .nojekyll
      run: touch docs/build/html/.nojekyll
    
    - name: Deploy to GitHub Pages
      uses: peaceiris/actions-gh-pages@v4
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./docs/build/html
```

### Step 8: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** → **Pages**
3. Under **Source**, select **Deploy from a branch**
4. Select branch **gh-pages** and folder **/ (root)**
5. Click **Save**

Wait a few minutes, then visit:
```
https://<username>.github.io/<repository>/
```

## Adding Publication Context

### Citations

Include citations in your documentation:

```rst
Citation
--------

.. code-block:: bibtex
   
   @article{author2025,
     title={Your Paper Title},
     author={Author Name},
     journal={Journal Name},
     year={2025}
   }
```

### Repository Links

Link to your code:

```rst
* Repository: https://github.com/username/repository
* Documentation: https://username.github.io/repository/
* Source Code: `src/module.py <../../../src/module.py>`_
```

### External Resources

```rst
Additional Resources
--------------------

* `NumPy Documentation <https://numpy.org/doc/>`_
* `Sphinx Documentation <https://www.sphinx-doc.org/>`_
* `Python Scientific Lecture Notes <https://scipy-lectures.org/>`_
```

## Documentation Best Practices

### For Code Documentation

- ✅ Use NumPy-style docstrings for all public functions and classes
- ✅ Include type hints in function signatures
- ✅ Provide examples in docstrings with expected outputs
- ✅ Document parameters, return values, and exceptions
- ✅ Add mathematical notation where relevant
- ✅ Link to related functions and classes

### For Narrative Documentation

- ✅ Start with installation instructions
- ✅ Provide quick start examples
- ✅ Explain the scientific context and methodology
- ✅ Include usage examples with code blocks
- ✅ Link to external resources and references
- ✅ Maintain a clear structure with table of contents

### For Maintenance

- ✅ Build documentation locally before committing
- ✅ Check for broken links and references
- ✅ Update docs when changing APIs
- ✅ Version documentation with code releases
- ✅ Test examples to ensure they work

## Example: Sample Module

This repository includes `src/sample_module.py` demonstrating:

- NumPy-style docstrings with full parameter documentation
- Mathematical equations in docstrings
- Usage examples
- Type hints
- Comprehensive function and class documentation

See the [live documentation](https://b-wie.github.io/how_to_document_your_reposiory_with_sphinx/) for the rendered result.

## Troubleshooting

### "Module not found" when building

Ensure `sys.path` is configured in `conf.py`:

```python
import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))
```

### Equations not rendering

Add `sphinx.ext.mathjax` to extensions in `conf.py`.

### Cross-references broken

- Check that target files exist and are in the toctree
- Use correct syntax: `:doc:`page`` (without `.rst`)
- For code: `:func:`module.function`` or `:class:`module.ClassName``

### GitHub Pages not updating

- Check Actions tab for workflow failures
- Verify `gh-pages` branch exists
- Ensure Pages is enabled in repository settings
- Wait a few minutes after deployment

## Resources

### Sphinx Documentation

- [Sphinx Official Documentation](https://www.sphinx-doc.org/)
- [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
- [Sphinx Extensions](https://www.sphinx-doc.org/en/master/usage/extensions/index.html)

### Python Documentation

- [NumPy Docstring Guide](https://numpydoc.readthedocs.io/en/latest/format.html)
- [PEP 257 – Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

### Themes and Styling

- [Read the Docs Theme](https://sphinx-rtd-theme.readthedocs.io/)
- [Sphinx Themes Gallery](https://sphinx-themes.org/)
- [Furo Theme](https://pradyunsg.me/furo/)

### Scientific Python

- [NumPy Documentation](https://numpy.org/doc/)
- [SciPy Lectures](https://scipy-lectures.org/)
- [Scientific Python Lectures](https://lectures.scientific-python.org/)

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Build and test documentation locally
5. Submit a pull request

## License

This tutorial repository is provided as an educational resource for the scientific Python community.

## Acknowledgments

This documentation tutorial builds upon best practices from:

- The NumPy and SciPy documentation teams
- The Sphinx development community
- The Read the Docs project
- Scientific Python package maintainers

## Questions?

- 📖 [View the live documentation](https://b-wie.github.io/how_to_document_your_reposiory_with_sphinx/)
- 🐛 [Report issues on GitHub](https://github.com/B-Wie/how_to_document_your_reposiory_with_sphinx/issues)
- 💬 [Ask questions in discussions](https://github.com/B-Wie/how_to_document_your_reposiory_with_sphinx/discussions)
