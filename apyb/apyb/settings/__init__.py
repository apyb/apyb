from .common import *  # noqa

try:
    from cloudez_settings import *  # noqa
except ImportError:
    pass

try:
    from .local import *  # noqa
except ImportError:
    pass

try:
    from .test import *  # noqa
except ImportError:
    pass
