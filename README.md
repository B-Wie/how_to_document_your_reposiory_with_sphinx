# Scientific Python Documentation Template for Lab Users

A beginner-friendly template for Python projects in scientific labs, showing how to document code with Sphinx and integrate with eLabFTW for complete experimental traceability.

## 🎯 What is This?

This repository provides a **complete working example** for scientists and lab users who want to:

1. **Document their Python analysis scripts** professionally using Sphinx
2. **Link code to lab experiments** managed in eLabFTW (electronic lab notebook)
3. **Create reproducible workflows** from experiment → data → analysis → results
4. **Deploy documentation** automatically to GitHub Pages

Perfect for scientists, lab managers, and students starting with Python, GitHub, and modern lab data management.

## 🔬 Why Use This Template?

### Traditional Lab Workflow (Without Integration)
❌ Lab notebook entries disconnected from data files  
❌ Analysis scripts scattered across computers  
❌ No clear link between experiments and results  
❌ Hard to reproduce analyses months later  
❌ Difficult to share methods with colleagues  

### Modern Integrated Workflow (With This Template)
✅ **eLabFTW** stores experiment protocols and raw data  
✅ **Python scripts** reference eLabFTW experiment IDs  
✅ **Documentation** explains methods and links to experiments  
✅ **GitHub** tracks code versions and changes  
✅ **Automatic deployment** keeps docs up-to-date  

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Basic familiarity with command line
- (Optional) Access to an eLabFTW instance for experiment tracking

### Installation

1. **Clone or fork this repository**:
   ```bash
   git clone https://github.com/B-Wie/how_to_document_your_reposiory_with_sphinx.git
   cd how_to_document_your_reposiory_with_sphinx
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Build the documentation locally**:
   ```bash
   cd docs
   make html
   ```

4. **View the documentation**:
   Open `docs/build/html/index.html` in your web browser

### Try the Example

Run the example HPLC analysis script:
```bash
python src/hplc_analysis.py
```

This analyzes a sample chromatogram and demonstrates eLabFTW integration patterns.

## 📁 Repository Structure

```
.
├── data/
│   └── sample_hplc_chromatogram.txt    # Example HPLC data with eLabFTW references
├── src/
│   ├── hplc_analysis.py                # HPLC analysis with eLabFTW integration
│   └── sample_module.py                # General scientific computing examples
├── docs/
│   ├── source/
│   │   ├── conf.py                     # Sphinx configuration
│   │   ├── index.rst                   # Documentation homepage
│   │   ├── elabftw_integration.rst     # eLabFTW workflow guide
│   │   └── best_practices.rst          # Documentation best practices
│   └── Makefile                        # Build commands
├── README.md                           # This file
├── CONTRIBUTING.md                     # Contribution guidelines
├── LICENSE.md                          # MIT license
└── requirements.txt                    # Python dependencies
```

## 🔗 eLabFTW Integration: Complete Workflow

### What is eLabFTW?

[eLabFTW](https://www.elabftw.net/) is a free, open-source electronic lab notebook (ELN) designed for research labs. It helps you:
- Document experiments with protocols and observations
- Manage equipment and resources
- Store and organize research data
- Ensure compliance and traceability

### The Integrated Workflow

```
┌─────────────┐
│  1. eLabFTW │  Document experiment protocol and equipment
│  Experiment │  Record parameters, upload raw data files
└──────┬──────┘
       │ Persistent ID: experiment #67890
       ↓
┌─────────────┐
│  2. GitHub  │  Store analysis code in version control
│  Repository │  Scripts reference eLabFTW experiment IDs
└──────┬──────┘
       │ 
       ↓
┌─────────────┐
│  3. Python  │  Run analysis with eLabFTW references in code
│  Analysis   │  Load data, process, generate results
└──────┬──────┘
       │
       ↓
┌─────────────┐
│  4. Results │  Upload results back to eLabFTW
│  Back to    │  Link GitHub commit for full traceability
│  eLabFTW    │  Document analysis parameters used
└─────────────┘
```

### Example: Referencing eLabFTW in Your Code

**In your data file header** (`data/sample_hplc_chromatogram.txt`):
```
# Experiment: eLabFTW #67890 (https://your-elabftw-instance.org/experiments.php?mode=view&id=67890)
# Equipment: HPLC-UV (eLabFTW ID: EQUIP-12345)
# Date: 2025-01-15
# Method: See eLabFTW experiment record for complete details
```

**In your Python script** (`src/hplc_analysis.py`):
```python
"""
HPLC Analysis Script

eLabFTW References:
- Experiment: https://your-elabftw-instance.org/experiments.php?mode=view&id=67890
- Equipment: https://your-elabftw-instance.org/database.php?mode=view&id=EQUIP-12345
"""

def analyze_chromatogram(filepath):
    """Analyze HPLC data. See eLabFTW experiment for method details."""
    # Your analysis code here
    pass
```

**In your documentation** (`docs/source/elabftw_integration.rst`):
```rst
This analysis corresponds to eLabFTW experiment #67890:
https://your-elabftw-instance.org/experiments.php?mode=view&id=67890

For equipment specifications and calibration records, see:
https://your-elabftw-instance.org/database.php?mode=view&id=EQUIP-12345
```

### Benefits of This Approach

1. **Complete Traceability**: Direct links from results back to experiments
2. **Reproducibility**: All information needed to repeat analysis is linked
3. **Collaboration**: Team members can find related experiments easily
4. **Compliance**: Meets data integrity requirements (FDA 21 CFR Part 11, GLP)
5. **Long-term Accessibility**: Persistent IDs survive file reorganization

## 📚 Documentation with Sphinx

### Why Sphinx?

Sphinx is the documentation tool used by most major Python projects (NumPy, SciPy, pandas). It:
- Generates beautiful HTML documentation from simple text files
- Automatically creates API documentation from docstrings
- Supports mathematical equations (LaTeX)
- Integrates with GitHub Pages for free hosting
- Is the industry standard for Python documentation

### Documentation Structure

This template includes:

1. **API Documentation**: Automatically generated from Python docstrings
2. **eLabFTW Integration Guide**: How to link experiments and code
3. **Best Practices**: Tips for scientific documentation
4. **Examples**: Working code with sample data

### Building Documentation

**Local build** (for testing):
```bash
cd docs
make html
```

**Automatic deployment** (via GitHub Actions):
- Push to `main` or `master` branch
- GitHub Actions automatically builds and deploys to GitHub Pages
- View at: `https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/`

See [GITHUB_PAGES_SETUP.md](GITHUB_PAGES_SETUP.md) for setup instructions.

## 🧪 Example: HPLC Data Analysis

The repository includes a complete example of HPLC chromatogram analysis:

### Features Demonstrated

- Loading data from text files with eLabFTW references
- Peak detection and integration algorithms
- Chromatographic calculations (resolution, retention time)
- Comprehensive NumPy-style docstrings
- eLabFTW integration in comments and documentation

### Running the Example

```bash
python src/hplc_analysis.py
```

Output:
```
HPLC Chromatogram Analysis
==================================================
eLabFTW Experiment: https://your-elabftw-instance.org/experiments.php?mode=view&id=67890
eLabFTW Equipment: https://your-elabftw-instance.org/database.php?mode=view&id=EQUIP-12345

File: data/sample_hplc_chromatogram.txt
Data points: 101
Time range: 0.00 - 10.00 min

Detected 2 peaks:
Peak 1: RT=2.10 min, Height=98.7 mAU
Peak 2: RT=5.70 min, Height=122.3 mAU

Peak Resolution: Rs = 1.71
==================================================
```

### Adapting for Your Needs

This example can be adapted for:
- **GC-MS analysis**: Modify for mass spectrometry data
- **UV-Vis spectroscopy**: Change to wavelength scans
- **Titration curves**: Adapt for pH/volume data
- **Enzyme kinetics**: Modify for rate calculations
- **Any instrument data**: Follow the same integration pattern

## 🎓 For Beginners

### New to Python?

- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html)
- [Python for Chemists](https://www.pythonforchemists.org/)

### New to Git/GitHub?

- [GitHub Skills](https://skills.github.com/)
- [Git Basics](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)
- [GitHub Docs](https://docs.github.com/en)

### New to Sphinx?

- [Sphinx Tutorial](https://www.sphinx-doc.org/en/master/tutorial/)
- [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
- [NumPy Docstring Guide](https://numpydoc.readthedocs.io/)

### New to eLabFTW?

- [eLabFTW Documentation](https://doc.elabftw.net/)
- [eLabFTW Demo](https://demo.elabftw.net/)
- [Setting up eLabFTW](https://doc.elabftw.net/install.html)

## 🔒 Best Practices

### Do NOT Store in GitHub:

- ❌ Sensitive experimental data (use eLabFTW)
- ❌ Large raw data files (link to eLabFTW instead)
- ❌ Patient/subject information (privacy concerns)
- ❌ Proprietary information (use private repos if needed)

### DO Store in GitHub:

- ✅ Analysis scripts and code
- ✅ Documentation
- ✅ Small example/test datasets
- ✅ Configuration files
- ✅ Requirements and dependencies

### Store in eLabFTW:

- 📔 Experiment protocols and procedures
- 📊 Raw data files from instruments
- 🔧 Equipment specifications and maintenance logs
- 📝 Observations and lab notes
- 📎 Supporting documents and images

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- How to set up a development environment
- Code style guidelines
- Documentation standards
- Pull request process

All skill levels welcome—this is a learning-friendly project!

## 📄 License

This project is licensed under the MIT License - see [LICENSE.md](LICENSE.md) for details.

## 🙏 Acknowledgments

This template builds on best practices from:
- The NumPy and SciPy documentation communities
- The Sphinx and Read the Docs projects
- The eLabFTW development team
- Scientific Python package maintainers
- Research software engineering community

## 📖 Live Documentation

View the full documentation at:
**https://b-wie.github.io/how_to_document_your_reposiory_with_sphinx/**

## ❓ Questions or Issues?

- 📖 Check the [documentation](https://b-wie.github.io/how_to_document_your_reposiory_with_sphinx/)
- 💬 Start a [discussion](https://github.com/B-Wie/how_to_document_your_reposiory_with_sphinx/discussions)
- 🐛 Report [issues](https://github.com/B-Wie/how_to_document_your_reposiory_with_sphinx/issues)
- 🤝 See [CONTRIBUTING.md](CONTRIBUTING.md) for how to help

## 🌟 Star This Repository

If you find this helpful, give it a star! It helps others discover this resource.

---

**Made with ❤️ for the scientific Python community**
