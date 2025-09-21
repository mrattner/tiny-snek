import re
import sys


MODULE_REGEX = r"^[_a-z][_a-z\d]+$"
module_name = "{{ cookiecutter.module_name }}"

PROJECT_REGEX = r"(^[a-z\d]$)|(^[a-z\d][a-z\d\.\-_]*[a-z\d])"
project_name = "{{ cookiecutter.__project_slug }}"

if not re.match(PROJECT_REGEX, project_name):
    print("ERROR: (%s) is not a valid uv package name." % project_name)
    print("Names must start and end with a letter or digit and may only contain -, _, ., and alphanumeric characters.")
    sys.exit(1)

if not re.match(MODULE_REGEX, module_name):
    print("ERROR: (%s) is not a valid Python module name." % module_name)
    print("Only alphanumerics and underscores are allowed.")
    sys.exit(1)
