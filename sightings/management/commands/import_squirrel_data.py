import csv
from django.core.management.base import BaseCommand, CommandError
import datetime
from sightings.models import Tracker


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('path')
    #comment 
    def handle(self, *args, **options):
        with open(options['path']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        for item in data:
            t = Tracker(
                x = item['X'],
                y = item['Y'],
                unique_squirrel_id = item['Unique Squirrel ID'],
                shift = item['Shift'],
                date = item['Date'],
                age = item['Age'],
                primary_fur_color = item['Primary Fur Color'],
                location = ['Location'],
                specific_Location = ['Specific Location'],
                running = ['Running'],
                chasing = ['Chasing'],
                climbing = ['Climbing'],
                eating = ['Eating'],
                foraging = ['Foraging'],
                other_activities = ['Other Activities'],
                kuks = ['Kuks'],
                quaas = ['Quaas'],
                moans = ['Moans'],
                tail_flags = ['Tail Flags'],
                tail_twitches = ['Tail Twiches'],
                approaches = ['Approaches'],
                Indifferent = ['Indifferent'],
                runs_from = ['Runs From'],



                )   
            t.save()
