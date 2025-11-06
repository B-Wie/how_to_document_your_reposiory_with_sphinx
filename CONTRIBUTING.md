# Contributing to This Repository

Thank you for your interest in contributing! This guide will help you get started with contributing to this scientific Python documentation template.

## For Beginners

This repository is designed to be beginner-friendly. If you're new to:
- **Python**: Check out [Python for Beginners](https://www.python.org/about/gettingstarted/)
- **Git/GitHub**: See [GitHub's Git Guides](https://github.com/git-guides)
- **Sphinx Documentation**: Visit [Sphinx Tutorial](https://www.sphinx-doc.org/en/master/tutorial/)
- **eLabFTW**: Read the [eLabFTW Documentation](https://doc.elabftw.net/)

Don't worry if you're learning—everyone was a beginner once!

## Ways to Contribute

### 1. Report Issues

Found a bug or have a suggestion? [Open an issue](https://github.com/B-Wie/how_to_document_your_reposiory_with_sphinx/issues) and describe:
- What you expected to happen
- What actually happened
- Steps to reproduce the issue
- Your environment (OS, Python version, etc.)

### 2. Improve Documentation

Good documentation is crucial for scientific projects. You can:
- Fix typos or clarify confusing sections
- Add examples or use cases
- Improve eLabFTW integration guidance
- Update outdated information
- Add more beginner-friendly explanations

### 3. Contribute Code

You can add:
- New analysis functions to `src/hplc_analysis.py`
- Additional example scripts for other analytical techniques
- Improvements to existing code
- Better error handling or validation

### 4. Share Examples

Help others by sharing:
- Your own eLabFTW integration workflows
- Example chromatograms or datasets
- Documentation templates you've created
- Tips and tricks for lab data management

## Getting Started

### Step 1: Set Up Your Development Environment

1. **Fork the repository** on GitHub (click the "Fork" button)

2. **Clone your fork** to your local machine:
   ```bash
   git clone https://github.com/YOUR-USERNAME/how_to_document_your_reposiory_with_sphinx.git
   cd how_to_document_your_reposiory_with_sphinx
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Test the setup** by building the documentation:
   ```bash
   cd docs
   make html
   ```
   
   Then open `docs/build/html/index.html` in your browser.

### Step 2: Create a Branch

Create a new branch for your changes:
```bash
git checkout -b descriptive-branch-name
```

Use descriptive names like:
- `fix-typo-in-readme`
- `add-gc-analysis-example`
- `improve-elabftw-docs`

### Step 3: Make Your Changes

- Edit files using your favorite text editor or IDE
- Test your changes thoroughly
- Follow the existing code style
- Add comments to explain complex logic
- Update documentation if you change functionality

### Step 4: Test Your Changes

Before submitting, make sure:

1. **Python code runs without errors**:
   ```bash
   python src/hplc_analysis.py
   ```

2. **Documentation builds successfully**:
   ```bash
   cd docs
   make clean
   make html
   ```
   
   Check for warnings or errors in the output.

3. **Check for broken links** in the documentation

### Step 5: Commit Your Changes

Write clear, descriptive commit messages:
```bash
git add .
git commit -m "Add GC-MS analysis example with eLabFTW integration"
```

Good commit messages:
- Start with a verb (Add, Fix, Update, Remove)
- Are concise but descriptive
- Explain *what* and *why*, not *how*

### Step 6: Push and Create a Pull Request

1. **Push your branch** to GitHub:
   ```bash
   git push origin your-branch-name
   ```

2. **Open a Pull Request** on GitHub:
   - Go to your fork on GitHub
   - Click "Compare & pull request"
   - Fill in the PR template with details about your changes
   - Link any related issues

3. **Wait for review** and address any feedback

## Code Style Guidelines

### Python Code

- Follow [PEP 8](https://pep8.org/) style guide
- Use meaningful variable and function names
- Write docstrings for all functions (NumPy style)
- Include type hints for function parameters and returns
- Keep functions focused and modular

Example:
```python
def calculate_retention_factor(retention_time: float, void_time: float) -> float:
    """
    Calculate the retention factor (k') for a chromatographic peak.
    
    Parameters
    ----------
    retention_time : float
        Peak retention time in minutes.
    void_time : float
        Column void time in minutes.
        
    Returns
    -------
    float
        Retention factor (dimensionless).
        
    Notes
    -----
    Document method parameters in eLabFTW experiment records.
    """
    return (retention_time - void_time) / void_time
```

### Documentation (reStructuredText)

- Use clear, concise language
- Include code examples with expected output
- Add cross-references to related sections
- Use proper heading hierarchy
- Include eLabFTW integration guidance where relevant

### eLabFTW Integration

When adding examples that reference experimental data:
- Show how to link to eLabFTW experiment records
- Include equipment/database item references
- Demonstrate use of persistent IDs/URLs
- Explain the workflow from experiment → data → analysis

## Testing

Currently, this is a documentation template without a formal test suite. When testing your changes:

1. **Run Python scripts** to ensure they execute without errors
2. **Build documentation** and check for warnings
3. **Verify all links** work correctly
4. **Test examples** with sample data
5. **Check cross-references** resolve properly

If you're adding significant functionality, consider adding basic tests.

## Documentation Best Practices

### When Writing Docs

- **Start with the user's perspective**: What are they trying to do?
- **Use examples**: Show, don't just tell
- **Be explicit**: Don't assume background knowledge
- **Link to resources**: Help users learn more
- **Keep it updated**: Documentation rots quickly

### For Scientific Context

- **Explain the science**: Don't assume everyone knows chromatography
- **Cite sources**: Reference papers, textbooks, standards
- **Show workflows**: How does this fit into lab work?
- **Link to eLabFTW**: Show how to connect code and lab records

## eLabFTW Integration Guidelines

When documenting eLabFTW integration:

### DO:
- ✅ Use persistent URLs (experiment IDs, database IDs)
- ✅ Show how to reference records in comments/docstrings
- ✅ Explain the workflow (lab → eLabFTW → GitHub → analysis)
- ✅ Give concrete examples with placeholder URLs
- ✅ Emphasize traceability and reproducibility

### DON'T:
- ❌ Include local equipment templates (use eLabFTW for this)
- ❌ Duplicate eLabFTW functionality in code
- ❌ Hardcode sensitive lab information
- ❌ Assume a specific eLabFTW instance configuration

Example of good eLabFTW reference:
```python
# Experiment record: https://your-elabftw-instance.org/experiments.php?mode=view&id=67890
# Equipment: HPLC-UV (eLabFTW ID: EQUIP-12345)
# Method details and raw data are stored in eLabFTW
```

## Questions?

- **General questions**: Open a [Discussion](https://github.com/B-Wie/how_to_document_your_reposiory_with_sphinx/discussions)
- **Bug reports**: Open an [Issue](https://github.com/B-Wie/how_to_document_your_reposiory_with_sphinx/issues)
- **Code questions**: Ask in your Pull Request

## Code of Conduct

Be respectful and constructive:
- Welcome newcomers and help them learn
- Give constructive feedback
- Focus on the work, not the person
- Be patient with beginners
- Celebrate contributions of all sizes

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Recognition

All contributors will be acknowledged in the project. Your contributions help the entire scientific Python community!

## Thank You!

Your contributions, whether big or small, help make this resource better for everyone in the scientific community. Thank you for taking the time to contribute! 🎉
