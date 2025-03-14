from setuptools import find_packages, setup

setup(
    name="py_utils",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["tqdm"],
    author="Aaron J. Sams",
    description="A collection of utility functions and classes for Python projects.",
    url="https://github.com/ajsams/py_utils",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
