# In case of running without anything configured, Django will import
# `settings`, which will then import this file; since all our configuration is
# in the base file, this will work.

# Also, we could split the production settings into their own settings and
# then import them here, just to make things easier to deploy (although it
# would be safer if we forced exporting DJANGO_SETTINGS_MODULE to the proper
# module).

from apyb.settings.base import *    # noqa
