# (2) How does Python know where to search for modules and packages?
# Python searches directories listed in `sys.path`, which includes:
# - The script's directory (or current directory in interactive mode)
# - Directories from the PYTHONPATH environment variable
# - Standard library and site-packages directories
# Python looks for `module.py` or a package directory with `__init__.py`. View with: `import sys; print(sys.path)`