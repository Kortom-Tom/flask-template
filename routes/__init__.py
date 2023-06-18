#https://gitlab.com/saxion.nl/42/lms42/-/blob/master/lms42/routes/__init__.py

from os.path import dirname, basename, isfile, join
import glob
modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]