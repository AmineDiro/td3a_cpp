#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..')))
from td3a_cpp import __version__  # noqa

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx_gallery.gen_gallery',
    'alabaster',
    'matplotlib.sphinxext.plot_directive',
    'pyquickhelper.sphinxext.sphinx_runpython_extension',
    'pyquickhelper.sphinxext.sphinx_epkg_extension',
]

templates_path = ['_templates']
html_logo = '_static/logo.png'
source_suffix = '.rst'
master_doc = 'index'
project = 'td3a_cpp'
copyright = '2019, Xavier Dupré'
author = 'Xavier Dupré'
version = __version__
release = __version__
language = 'en'
exclude_patterns = []
pygments_style = 'sphinx'
todo_include_todos = True

import alabaster  # noqa
html_theme = "alabaster"
html_theme_path = [alabaster.get_path()]

html_theme_options = {}
html_static_path = ['_static']
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}

htmlhelp_basename = 'td3a_cppdoc'
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

latex_documents = [
    (master_doc,
     'td3a_cpp.tex',
     'Documentation',
     'Xavier Dupré',
     'manual'),
]

texinfo_documents = [
    (master_doc, 'td3a_cpp', 'td3a_cpp Documentation',
     author, 'td3a_cpp', 'One line description of project.',
     'Miscellaneous'),
]

intersphinx_mapping = {'https://docs.python.org/': None}

sphinx_gallery_conf = {
    # path to your examples scripts
    'examples_dirs': os.path.join(os.path.dirname(__file__), '../examples'),
    # path where to save gallery generated examples
    'gallery_dirs': 'auto_examples'
}

epkg_dictionary = {
    'cython': 'https://cython.org/',
    'numpy': 'https://numpy.org/',
    'openmp': 'https://www.openmp.org/',
    'tqdm': 'https://github.com/tqdm/tqdm',
}