from .production import *

try:
    from .development import *
except ImportError:
    ENV = 'Production'
