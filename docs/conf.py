import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

project = "test_pages"
language = "ja"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "myst_parser",
]

source_suffix = {
    ".md": "markdown",
}

autosummary_generate = True

html_theme = "sphinx_rtd_theme"