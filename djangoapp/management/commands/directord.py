from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    """Implements basic daemon functionalities: status, start, stop,
    restart.

    """
    def _init_daemon(self):
        pass

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        pass
