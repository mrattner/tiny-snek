import re
import sys


MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
module_name = "{{ cookiecutter.module_name }}"

if not re.match(MODULE_REGEX, module_name):
    print("ERROR: (%s) is not a valid Python module name." % module_name)
    print("Only alphanumerics and underscores are allowed.")

    #Exit to cancel project
    sys.exit(1)
