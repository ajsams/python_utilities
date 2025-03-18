# python_utilities

Custom python utilities and context managers.

## `py_utils` Package Summary

- `logger.py` - A wrapper for the python standard library `logging` module. Provides a custom `logger.Logger()` class, a `@log_function` decorator to add consistent decoration to functions in a project, and a single instance of the `Logger` class (`logger.logger`).
- `timer.py` - A context manager to time blocks of code with the python standard library `time` module. Includes optional functionality to add a custom logger for logging time context. Also includes an optional timer bar using `tqdm`.

## Adding `py_utils` to a Fresh Mamba/Conda Environment

### Install [Miniforge](https://github.com/conda-forge/miniforge).

If you have no active install of conda.

```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
```

### Create and Configure [Conda](https://conda.io/projects/conda/en/latest/user-guide/index.html) Env with [Mamba](https://mamba.readthedocs.io/en/latest/)

(see [Managing environments](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#) in Conda docs)

```bash
mamba env create --name py_utils --file environment.yml

mamba activate py_utils
```

If you need to update the environment after making changes to the `environment.yml` file.

```bash
mamba env update --name py_utils --file environment.yml --prune
```

Using `--name` here explicitly to ensure we are creating and updating the same environment, but this should be unnecessary if the name is correct within the `environment.yml` file.

`--prune` will uninstall dependencies that were removed from the previous version of this environment.

## Adding `py_utils` to an Existing Mamba/Conda Environment

If you want to add this package to an existing conda environment, you have several options, two are highlighted here:

### Add the package as non-editable directly from the repository

First, add this line to the pip section of your `environment.yml` file. This will download and install the package as-is directly from the repository.

```yaml
pip:
  - git+https://github.com/ajsams/python_utilities#egg=py_utils
```

Second, update your conda environment from the `environment.yml` file.

```bash
conda env update --file environment.yml --prune
```

### Download the package and install as editable

This option is useful if you wish to update the code in this repository to use in your project.

First, clone the repository.

```bash
git clone https://github.com/ajsams/python_utilities
```

Second, modify the `environment.yml` file to install the package as editable. Add this line:

```yaml
pip: -e /path/to/local/python_utilities
```

Finally, update your environment:

```bash
conda env update --file environment.yml --prune
```

NOTE - This list is not exhaustive, and there are other ways you may prefer to add this code to your project.

### Verify the install

You may want to verify that py_utils was successfully installed to your environment.

```bash
python -c "import py_utils; print(py_utils.__version__)"
```
