from django.core.management.base import BaseCommand, CommandError

from app.watt.tasks import import_csv

class Command(BaseCommand):
    help = 'Import data from CSV'

    def add_arguments(self, parser):
        parser.add_argument('filename')

    def handle(self, *args, **options):
        files_created_count = import_csv(options['filename'])
        self.stdout.write(self.style.SUCCESS("Importation of %s items successful" % files_created_count))
