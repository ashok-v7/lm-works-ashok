from setuptools import find_packages, setup

setup(
    name = "QAGen  Proj",
    version= '0.0.0',
    author="asok",
    author_email="bdracks12@gmail.com",
    packages= find_packages(),
    install_requires = []
)


# It makes Python project that is meant to be packaged and distributed. It defines metadata, dependencies, and installation instructions for the project
# Using find_packages(), it automatically detects sub-packages and modules in the project.
# -e . to run setup.py