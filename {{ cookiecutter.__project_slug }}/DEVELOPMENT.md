# Developing
[Pipenv](https://pipenv.pypa.io/en/latest/advanced/#pipfile-vs-setuppy) handles
the creation of virtual environments and management of package dependencies,
including development dependencies.

## Using the virtual environment
For easier execution of Python, open a shell in Pipenv's virtual environment:
```bash
pipenv shell
```
While the virtual environment is activated, you can use the `python` command as
though you were completely isolated from other Python installations on the
system.

When done using the virtual environment, execute `exit` to return your path to
normal.

## Installing dependencies
To install any missing packages for the current project, or to add packages as
development dependencies, run `pipenv install` in the top-level project
directory. Add the `--dev` flag for development-only dependencies. The Pipfile
will be updated automatically.

To specify new build dependencies for your package, modify the `setup.py` list
of `install_requires` to include the new package name. Specify the name only,
rather than a particular version. Then run `pipenv install -e .` to install your
application in development mode.
[Read more](https://pipenv.pypa.io/en/latest/advanced/#pipfile-vs-setuppy)
about the difference between `Pipfile` and `setup.py`.

## Defining app entry points
{%- if cookiecutter.interface == "cli" %}
Once the project has been installed in development mode, command line scripts
will be available from `setup.py`'s entry\_points array under the
"console\_scripts" section.
{%- elif cookiecutter.interface == "gui" %}
Once the project has been installed in development mode, the script to launch
the application will be available from `setup.py`'s entry\_points array under
the "gui\_scripts" section. Add any command-line scripts that should ship with
the package to the "console\_scripts" section.
{%- endif %}

# Testing
## Running tests
To run all the tests in the project, execute:
```bash
pipenv run test
```
For more detailed results, include the `-v` flag. To run only the tests whose
names match a particular pattern, use the `-k` option.

## Writing tests
1. Every test filename must start with the string "test" and be a valid Python
module name (e.g. use underscores instead of hyphens).
2. Test methods must start with the string "test" to be discovered by the test
runner.
{%- if cookiecutter.use_pytest|lower == "y" %}
3. Test class names should start with `Test` or be a descendant of the class
`unittest.TestCase` to be collected by default.
4. See the [`pytest` docs](https://docs.pytest.org) for details of how to group
tests into suites and how to use `pytest`'s other features.
{%- else %}
3. Test classes must be a descendant of the class `unittest.TestCase`.
4. To group tests together, create a
[test suite](https://docs.python.org/3/library/unittest.html#grouping-tests).
{%- endif %}

