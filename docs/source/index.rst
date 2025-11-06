Welcome to Test Sphinx Documentation!
======================================

This is a test repository for deploying Sphinx documentation to GitHub Pages.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Introduction
------------

This repository demonstrates how to build and deploy arbitrary Sphinx documentation
to a GitHub Pages URL ending with ``.github.io``.

Features
--------

* Automatic documentation building with GitHub Actions
* Deployment to GitHub Pages
* Modern Sphinx setup with popular extensions
* Easy to customize and extend

Getting Started
---------------

To build this documentation locally:

1. Install the required dependencies:

   .. code-block:: bash

      pip install -r requirements.txt

2. Build the documentation:

   .. code-block:: bash

      cd docs
      make html

3. View the documentation by opening ``docs/build/html/index.html`` in your browser.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
