from .prod import *

try:
    from .dev import *
except ImportError:
    ENV = 'Production'
