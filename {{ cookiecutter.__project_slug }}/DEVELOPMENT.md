# Development guide for {{ cookiecutter.project_name }}

## Tooling

[`uv`][uv] handles the creation of Python virtual environments and management of
package dependencies, including development dependencies.

A [Justfile][just] is provided for convenience to be used as a command runner,
with the following recipes:

- `just lint`: Run the linter in auto-fix mode
- `just format`: Run the auto-formatter in write mode
- `just test`: Run all tests
- `just start`: Launch the main Python program as a script

Without Just, you can 'just' run the commands invoked by these recipes.

### Using the virtual environment

To activate a Python virtual environment in your shell:

```sh
source <venv-location>/bin/activate
```

While the virtual environment is activated, you can use the `python` command as
though you were completely isolated from other Python installations on the
system. When done using the virtual environment, execute `exit` to return your
path to normal.

`uv` automatically creates a Python virtual environment `.venv`; all its
commands operate within the virtual environment regardless of whether it's been
activated. You can use `uv run` for executing local Python scripts and commands
from packages that have been installed in the virtual environment.

### Installing dependencies

Install all dependencies, including dev dependencies, with `uv sync`. Extraneous
packages are removed and the lockfile gets updated as well.

To add external packages as dependencies, run `uv add` in the top-level project
directory. Add the `--dev` flag for development-only dependencies.
{%- if cookiecutter.interface == "gui" %}

In the case where `tkinter` isn't already present in the virtual environment,
delete the `.venv` folder and have `uv` reinstall Python:

```sh
rm -rf .venv
uv python install --reinstall 3.12
```
{% endif %}

If your project is to be packaged into a distribution/wheel, [`uv build`][build]
can be configured to build and publish it. Also change `uv`'s configured
[package mode][uvpkg] in `pyproject.toml`:

```toml
[tool.uv]
package = false # <-- Remove this line
```

### Running project executables

The `just start` recipe runs the module's entry-point script defined in
`__main__.py`. You can run other local scripts in the context of the virtual
environment the same way, via `uv run <...>`

## Testing

### Running tests

To run all the tests in the project, execute the `just test` recipe.

For more detailed results, include the `-v` flag. To run only the tests whose
names match a particular pattern, use the `-k` option.

### Writing tests

1. Every test filename must start with the string "test" and be a valid Python
   module name (e.g. use underscores instead of hyphens).
2. Test methods must start with the string "test" to be discovered by the test
   runner.
{%- if cookiecutter.use_pytest %}
3. Test class names should start with `Test` or be a descendant of the class
`unittest.TestCase` to be collected by default.
4. See the [`pytest` docs][pytest] for details of how to group tests into suites
   and how to use `pytest`'s other features.
{%- else %}
3. Test classes must be a descendant of the class `unittest.TestCase`.
4. To group tests together, create a [test suite][unittest].
{%- endif %}

[uv]: https://docs.astral.sh/uv/reference/cli
[just]: https://just.systems/man/en/quick-start.html
[ruff]: https://docs.astral.sh/ruff/configuration/#full-command-line-interface
[build]: https://docs.astral.sh/uv/concepts/build-backend/#using-the-uv-build-backend
[uvpkg]: https://docs.astral.sh/uv/reference/settings/#package
{%- if cookiecutter.use_pytest %}
[pytest]: https://docs.pytest.org
{%- else %}
[unittest]: https://docs.python.org/3/library/unittest.html#grouping-tests
{%- endif %}
