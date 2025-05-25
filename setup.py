from setuptools import setup, find_packages

setup(
    name="dependatea",
    version="1.0.0",
    packages=find_packages(include=['py*']),
    package_dir={'': '.'},
    install_requires=[
        "requests==2.31.0",
        "pytest==7.4.0"
    ],
    python_requires=">=3.10",
)
