import logging
from django.conf import settings

__version__ = "1.0.dev3"


if settings.DEBUG:
    logger = logging.getLogger('devel')
else:
    logger = logging.getLogger('base')
