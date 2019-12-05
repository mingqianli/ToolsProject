import csv
from django.core.management.base import BaseCommand





from sighitngs.models import Tracker


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('pathe')
    #comment 
    def handle(self, *args, **options):
        with open(options['pathe']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        for item in data:
            t = Tracker(
                x = item['X'],
                y = item['Y'],
                ID = item['Unique Squirrel ID'],
                shift = item['Shiftx'],
                date = item['Date']
                age = item['Age']
                primary_fur_colo = item['Primary Fur Color']
                location = ['Location']
                specific location = ['Specific Location']
                running = ['Running']
                chasing = ['Chasing']
                climbing = ['Climbing']
                eating = ['Eating']
                foraging = ['Foraging']
                other_activities = ['Other Activities']
                kuks = ['Kuks']
                quaas = ['Quaas']
                moans = ['Moans']
                tail_flags = ['Tail Flags']
                tail_twitches = ['Tail Twiches']
                approaches = ['Approaches']
                indifferent ['Indifferent']
                runs_from = ['Runs From']



            )
            t.save()
