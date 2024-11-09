# Author: Dencyuman <takotakocyuman@gmail.com>
# Copyright (c) 2024 Dencyuman
# License: MIT License

from setuptools import setup
import dash_id_manager

DESCRIPTION = "Efficient id manager for Plotly Dash."
LONG_DESCRIPTION = "Efficient id manager for Plotly Dash."
NAME = 'dash-id-manager'
AUTHOR = 'Dencyuman'
AUTHOR_EMAIL = 'takotakocyuman@gmail.com'
URL = 'https://github.com/Dencyuman/dash-id-manager'
LICENSE = 'MIT License'
DOWNLOAD_URL = 'https://github.com/Dencyuman/dash-id-manager'
VERSION = dash_id_manager.__version__
PYTHON_REQUIRES = ">=3.7"

INSTALL_REQUIRES = []

EXTRAS_REQUIRE = {}

PACKAGES = [
    'dash_id_manager',
]

CLASSIFIERS = []

setup(name=NAME,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=AUTHOR,
      maintainer_email=AUTHOR_EMAIL,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      license=LICENSE,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      python_requires=PYTHON_REQUIRES,
      install_requires=INSTALL_REQUIRES,
      extras_require=EXTRAS_REQUIRE,
      packages=PACKAGES,
      classifiers=CLASSIFIERS
)
