from .common import *

try:
    from cloudez_settings import *
except ImportError:
    pass

try:
    from .local import *
except ImportError:
    pass
