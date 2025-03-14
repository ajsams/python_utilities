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

If you want to install this package into an existing mamba/conda environment, you can use the `environment.yml` file to update that environment. This is useful if you already have an environment set up and want to add the dependencies listed in the `environment.yml` file.

### Steps to Update an Existing Environment

1. **Activate the existing environment**:

   ```bash
   mamba activate <existing_env_name>
   ```

   Replace `<existing_env_name>` with the name of your existing environment.

2. **Update the environment using the `environment.yml` file**:

   ```bash
   mamba env update --name <existing_env_name> --file environment.yml
   ```

   This command will update the specified environment with the dependencies listed in the `environment.yml` file.

   Adding the `--prune` flag to this command will remove any dependencies in the current environment that are not needed to run the `py_utils` library.

3. **Install the local library in editable mode**:

   After updating the environment, you can install the local library in editable mode:

   ```bash
   pip install -e .
   ```

### Example

Assuming you have an existing environment named `myenv`, you can update it as follows:

```bash
mamba activate myenv
mamba env update --name myenv --file environment.yml
pip install -e .
```

This will ensure that your existing environment `myenv` is updated with the dependencies from the `environment.yml` file and that the local library is installed in editable mode.

## Installing the local library with pip editable

After installing and activating the local conda/mamba environment, from the root of the `py_utils` repository run:

```bash
pip install -e .
```
