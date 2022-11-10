from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Hello_World_first_pkg_GL",
    version="0.0.1",
    author="Gabriel_Lima",
    author_email="gabriel_plima@hotmail.com",
    description="Learning how to create my first package and print: Hello World",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GaPinheiro/simple-package-template.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)