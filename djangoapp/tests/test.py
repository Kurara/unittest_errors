from django.test import TestCase
# from unittest import TestCase
from io import StringIO
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.unittest")


class InfojuiceHarvesterTest(TestCase):

    def setUp(self):
        application = get_wsgi_application()

    def test_command_start(self):
        out = StringIO()
        call_command('directord', daemon_action='start', stdout=out)
        self.assertIn('Expected output', out.getvalue())
