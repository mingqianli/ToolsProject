from django.core.management.base import BaseCommand, CommandError
from sightings.models import Tracker
import datetime
import csv



class Command(BaseCommand):
    
    def add_arguments(self,parser):
        parser.add_argument('path')



    def handle(self, *args, **options):
        
        with open (options['path']) as fp:
            fields = ['x','y','unique_squirrel_id','shift','date','age','primary_fur_color','location',
                    'specific_Location','running','chasing','climbing','eating','foraging','other_activities','kuks',
                    'quaas','moans','tail_flags','tail_twitches','approaches','Indifferent','runs_from']

            writer = csv.writer(fp)

            for row in Tracker.objects.all():
                writer.writerow([getattr(row,field) for field in fields])


            fp.close()
