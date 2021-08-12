import pathlib

from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="latextable",
    version="0.2.1",
    py_modules=['latextable'],
    install_requires=["texttable"],
    description="An extension to the texttable library that exports tables directly to Latex.",
    keywords="table texttable latex",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/JAEarly/latextable",
    author="Joseph Early",
    author_email="joseph.early.ai@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    include_package_data=False,
)
