# Developing
## Creating a virtual environment
If one does not exist yet, create a Python virtual environment from the
top-level project directory:

    $ python3 -m venv ./venv

## Using the virtual environment
For easier use of Python and Pip, activate the virtual environment to put it at
the front of your path:

    $ source ./venv/bin/activate

While the virtual environment is activated, you can use the `pip` and `python`
commands as though you were completely isolated from other Python installations
on the system.

When done using the virtual environment, execute `deactivate` to return your
path to normal.

## Installing dependencies
First, make sure the package manager is up-to-date in your virtual environment:

    $ pip install --upgrade pip

To install any missing packages for the current project, execute in the
top-level project directory:

    $ pip install -e .

To specify a new package dependency during development, modify the `setup.py`
list of `install_requires` to include the new package name. Specify the name
only, rather than a particular version.

## Defining app entry points
Once the project has been installed in development mode, command line scripts
will be available from `setup.py`'s entry\_points array under the
"console\_scripts" section. If a command launches a graphical user interface,
it should be listed under the "gui\_scripts" section. To initialize the
database, run the `initdb` command in the virtual environment after installing
the app in editable mode.

# Testing
## Running tests
To run all the tests in the project, execute:

    $ python -m unittest discover tests

For more detailed results when running `unittest`, include the `-v` option.

## Writing tests
1. Every test filename must start with the string "test" and be a valid Python
module name (e.g. use underscores instead of hyphens).
2. Test classes must be a descendant of the class `unittest.TestCase`.
3. Test methods must start with the string "test" to be discovered by the test
runner.
4. To group tests together, create a
[test suite](https://docs.python.org/3/library/unittest.html#grouping-tests).

