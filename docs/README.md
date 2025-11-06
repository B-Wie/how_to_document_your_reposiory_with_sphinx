# Documentation Deployment Directory

This directory contains the Sphinx documentation build system and deployment configuration.

## Directory Structure

```
docs/
├── source/              # Source files for documentation
│   ├── conf.py         # Sphinx configuration
│   ├── index.rst       # Documentation homepage
│   ├── experiment_setup.rst      # Experimental methodology
│   ├── publication_context.rst   # Publication and citation info
│   ├── _static/        # Static files (images, CSS, etc.)
│   └── _templates/     # Custom Sphinx templates
├── build/              # Generated documentation (created by Sphinx)
│   └── html/          # HTML output (this gets deployed to GitHub Pages)
├── Makefile           # Build commands for Unix/Linux/Mac
├── make.bat           # Build commands for Windows
└── README.md          # This file

```

## Building Documentation Locally

### Prerequisites

Install the required Python packages:

```bash
pip install -r ../requirements.txt
```

### Building HTML Documentation

From this directory (`docs/`), run:

```bash
make html
```

The built documentation will be in `build/html/`. Open `build/html/index.html` in your browser to view it.

### Cleaning Build Files

To remove previously built files:

```bash
make clean
```

## Deployment to GitHub Pages

Documentation is automatically built and deployed to GitHub Pages via GitHub Actions:

1. **Trigger**: Pushes to `main` or `master` branch
2. **Build**: GitHub Actions runs `make html` 
3. **Deploy**: HTML files from `build/html/` are pushed to the `gh-pages` branch
4. **Publish**: GitHub Pages serves the content at your repository's `.github.io` URL

### Workflow File

The deployment workflow is defined in `.github/workflows/deploy-docs.yml`.

### Viewing Deployed Documentation

After the workflow completes, documentation is available at:
```
https://b-wie.github.io/how_to_document_your_reposiory_with_sphinx/
```

## Modifying Documentation

### Adding New Pages

1. Create a new `.rst` file in `source/`
2. Add it to the `toctree` directive in `source/index.rst`
3. Build locally to test
4. Push to trigger automatic deployment

### Updating Configuration

Edit `source/conf.py` to:
- Change theme or appearance
- Add Sphinx extensions
- Configure project metadata
- Adjust build settings

### Including Code Documentation

The documentation automatically generates API docs from Python docstrings using:
- `sphinx.ext.autodoc` - Extracts documentation from code
- `sphinx.ext.napoleon` - Parses NumPy-style docstrings
- `sphinx.ext.viewcode` - Adds links to source code

To document a new Python module:
1. Add it to the `src/` directory
2. Use NumPy-style docstrings
3. Reference it with `.. automodule::` in your `.rst` files

## File Formats

### reStructuredText (.rst)

Sphinx uses reStructuredText (RST) for documentation source files. Key features:

- **Headings**: Use underlines with `=`, `-`, `^`, etc.
- **Links**: `` `text <url>`_ `` for external links
- **Cross-refs**: `:doc:`page`` or `:ref:`label``
- **Code**: `` .. code-block:: language``
- **Math**: `` .. math::`` for equations

See the [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) for more details.

## Common Build Issues

### "Module not found" errors

Ensure Python can find your modules:
- Check that `sys.path` is configured in `source/conf.py`
- Verify relative paths are correct
- Install any dependencies your code requires

### "toctree contains reference to nonexistent document"

- Check that all files referenced in `toctree` exist
- Verify file names match exactly (case-sensitive)
- Don't include `.rst` extension in `toctree` entries

### Broken cross-references

- Ensure target labels exist: `` .. _label:``
- Use correct reference syntax: `:ref:`label``
- Check that referenced documents are in the build

## Resources

- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [reStructuredText Documentation](https://docutils.sourceforge.io/rst.html)
- [Read the Docs Tutorial](https://docs.readthedocs.io/en/stable/tutorial/)
- [NumPy Docstring Guide](https://numpydoc.readthedocs.io/)

## Questions?

For issues or questions:
1. Check the [Sphinx FAQ](https://www.sphinx-doc.org/en/master/faq.html)
2. Review existing documentation in `source/`
3. Open an issue on [GitHub](https://github.com/B-Wie/how_to_document_your_reposiory_with_sphinx/issues)
