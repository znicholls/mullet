import versioneer
from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand

PACKAGE_NAME = "mullet"
AUTHOR = "Zebedee Nicholls"
EMAIL = "zebedee.nicholls@climate-energy-college.org"
URL = "https://github.com/znicholls/mullet"

DESCRIPTION = (
    "Model for the evalUation of sea-LeveL risE and Temperature (MULLET), "
    "currently a playground for exploring simple climate model setups."
)
README = "README.rst"

SOURCE_DIR = "src"

REQUIREMENTS = ["numpy", "scipy"]
REQUIREMENTS_NOTEBOOKS = [
    "ipywidgets",
    "notebook",
    "pandas",
    "seaborn",
    "tqdm",
]
REQUIREMENTS_TESTS = ["codecov", "coverage", "nbval", "pytest-cov", "pytest>=4.0"]
REQUIREMENTS_DOCS = ["sphinx>=1.4", "sphinx_rtd_theme"]
REQUIREMENTS_DEPLOY = ["twine>=1.11.0", "setuptools>=38.6.0", "wheel>=0.31.0"]

REQUIREMENTS_DEV = [
    *["bandit", "black", "flake8", "isort", "mypy", "pydocstyle", "pylint>=2.4.4"],
    *REQUIREMENTS_DEPLOY,
    *REQUIREMENTS_DOCS,
    *REQUIREMENTS_NOTEBOOKS,
    *REQUIREMENTS_TESTS,
]

REQUIREMENTS_EXTRAS = {
    "deploy": REQUIREMENTS_DEPLOY,
    "dev": REQUIREMENTS_DEV,
    "docs": REQUIREMENTS_DOCS,
    "notebooks": REQUIREMENTS_NOTEBOOKS,
    "tests": REQUIREMENTS_TESTS,
}

with open(README, "r") as readme_file:
    README_TEXT = readme_file.read()


class Mullet(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        pytest.main(self.test_args)


cmdclass = versioneer.get_cmdclass()
cmdclass.update({"test": Mullet})

setup(
    name=PACKAGE_NAME,
    version=versioneer.get_version(),
    description=DESCRIPTION,
    long_description=README_TEXT,
    long_description_content_type="text/x-rst",
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    license="3-Clause BSD License",
    classifiers=[  # full list at https://pypi.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords=["mullet", "python", "fortran", "simple", "climate", "model"],
    packages=find_packages(SOURCE_DIR),  # no exclude as only searching in `src`
    package_dir={"": SOURCE_DIR},
    # include_package_data=True,
    install_requires=REQUIREMENTS,
    extras_require=REQUIREMENTS_EXTRAS,
    cmdclass=cmdclass,
    # entry_points={
    #     "console_scripts": [
    #         "mullet=mullet.cli:run",
    #     ]
    # },
)
