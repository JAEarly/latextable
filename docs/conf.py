# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath('../'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'latextable'
copyright = '2023, Joseph Early'
author = 'Joseph Early'
release = '2023'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc']
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
autodoc_member_order = 'bysource'


# Register hook to run when build is complete
def setup(app):
    app.connect('build-finished', on_build_finished)


# Hook implementation
def on_build_finished(app, exception):
    add_single_param_bullets("_build/html/index.html")


# Function to actually add the bullet points by overwriting the given HTML file
def add_single_param_bullets(file_path):
    print('Add single parameter bullets in {:s}'.format(file_path))
    if not os.path.exists(file_path):
        print('  File not found, skipping...')
        return
    lines_enc = []
    with open(file_path, 'rb') as f:
        for l in f.readlines():
            # Check for html that indicates single parameter function
            if b'<dd class="field-odd"><p><strong>' in l:
                # Work out the encoding if not defined
                enc = None
                if enc is None:
                    import chardet
                    enc = chardet.detect(l)['encoding']
                # Decode html and get the parameter information that needs adding
                l_dec = l.decode(enc)
                l_insert = l_dec.replace('<dd class="field-odd">', '').replace('\r\n', '')
                # Add new encoded lines to output
                lines_enc.append('<dd class="field-odd"><ul class="simple">'.encode('utf=8'))
                lines_enc.append('<li>{:s}</li>'.format(l_insert).encode(enc))
                lines_enc.append('</ul>'.encode('utf=8'))
            else:
                lines_enc.append(l)
    # Overwrite the original file with the new changes
    with open(file_path, 'wb') as f:
        for l in lines_enc:
            f.write(l)


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
