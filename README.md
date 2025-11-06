# test_sphinx_documentation_deploy

Test repository for deploying Sphinx documentation to GitHub Pages.

## Overview

This repository demonstrates how to build and deploy arbitrary Sphinx documentation to a GitHub Pages URL ending with `.github.io`.

## Features

- **Automatic Deployment**: GitHub Actions workflow automatically builds and deploys documentation
- **Sphinx Documentation**: Modern Sphinx setup with popular extensions
- **GitHub Pages**: Documentation hosted at `https://b-wie.github.io/test_sphinx_documentation_deploy/`

## Setup

### Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Build documentation:
   ```bash
   cd docs
   make html
   ```

3. View documentation:
   Open `docs/build/html/index.html` in your browser

### Deployment

The documentation is automatically built and deployed to GitHub Pages when changes are pushed to the `main` or `master` branch. The GitHub Actions workflow:

1. Checks out the repository
2. Sets up Python and installs dependencies
3. Builds the Sphinx documentation
4. Deploys to the `gh-pages` branch
5. GitHub Pages serves the content at the `.github.io` URL

## Repository Structure

```
.
├── docs/
│   ├── source/
│   │   ├── conf.py          # Sphinx configuration
│   │   ├── index.rst        # Main documentation page
│   │   ├── _static/         # Static files
│   │   └── _templates/      # Custom templates
│   ├── Makefile             # Build commands for Unix
│   └── make.bat             # Build commands for Windows
├── .github/
│   └── workflows/
│       └── deploy-docs.yml  # GitHub Actions workflow
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore patterns
└── README.md               # This file
```

## Customization

### Modify Documentation Content

Edit files in `docs/source/`:
- `index.rst`: Main documentation page
- `conf.py`: Sphinx configuration (theme, extensions, etc.)

### Change Theme

Edit `docs/source/conf.py` and modify the `html_theme` variable. Popular themes include:
- `alabaster` (default)
- `sphinx_rtd_theme` (Read the Docs theme)
- `furo`
- `pydata_sphinx_theme`

### Add Extensions

Add Sphinx extensions to the `extensions` list in `docs/source/conf.py`.

## Requirements

- Python 3.7+
- Sphinx 7.0.0+
- sphinx-rtd-theme 1.3.0+

## License

This is a test repository for demonstration purposes.
