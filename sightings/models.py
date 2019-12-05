
from django.db import models
from django.utils.translation import gettext as _

class Tracker(models.Model):
    x = models.FloatField (  
        help_text = ('Longitude'),
         )
    y = models.FloatField(
        help_text = ('Latitude'),
         )
    ID = models.CharField(
        help_text = ('Unique Squirrel Id'),
        max_length = 50,
         )
    PM = 'PM'
    AM = 'AM'

    SHIFT_CHOICES = (
        (PM,'PM'),
        (AM,'AM'),
        )
    shift = models.CharField(
        help_text = ('shift'),
        max_length = 50,
        choices = SHIFT_CHOICES,
        )
    date = models.CharField(
        help_text = ('date'),
        max_length = 50,
        )
    ADULT='Adult'
    JUVENILE='Juvenile'

    AGE_CHOICES = (
        (ADULT,'Adult'),
        (JUVENILE,'Juvenile'),
        )

    age = models.CharField(
        help_text = ('Age'),
        max_length = 50,
        choices = AGE_CHOICES,
        null = True,
        )
    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'

    FUR_COLOR_CHOICES = (
        (GRAY,'Gray'),
        (CINNAMON,'Cinnamon'),
        (BLACK,'Black'),
        )

    primary_fur_color = models.CharField(
        help_text = ('Primary Fur Color'),
        max_length = 50,
        choices = FUR_COLOR_CHOICES,
        null = True,
        )
    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'

    LOCATION_CHOICES = (
        (GROUND_PLANE,'Ground Plane'),
        (ABOVE_GROUND,'Above Ground'),
        )
    location = models.CharField(
        help_text = ('Location'),
        max_length = 50,
        choices = LOCATION_CHOICES,
        null = True,
        )
    specific_Location = models.CharField(
        help_text = ('Specific Location'),
        max_length = 50,
        null = True,
        )
    running = models.CharField(
        help_text = ('Running?'),
        max_length = 50,)
    chasing = models.CharField(
        help_text = ('Chasing?'),
        max_length = 50,)
    climbing = models.CharField(
        help_text = ('Climbing?'),
        max_length =50,)
    eating = models.CharField(
        help_text = ('Eating?'),
        max_length = 50,)
    foraging = models.CharField(
        help_text = ('Foraging?'),
        max_length = 50,)
    other_activities = models.CharField(
        help_text = ('Other Activities'),
        max_length = 50,
        null = True,
        )
    kuks = models.CharField(
        help_text = ('Kuks?'),
        max_length=50,)
    quaas = models.CharField(
        help_text = ('Quaas?'),
        max_length = 50,)
    tail_flags = models.CharField(
        help_text = ('Tail Flags?'),
        max_length =50,)
    tail_twitches = models.CharField(
        help_text = ('Tail Twitches?'),
        max_length = 50,)
    approaches = models.CharField(
        help_text = ('Approaches?'),
        max_length = 50,)
    indifferent = models.CharField(
        help_text = ('Indifferent?'),
        max_length = 50,)
    runs_from = models.CharField(
        help_text = ('Runs From?'),
        max_length = 50,)
    other_interactions = models.CharField(
        help_text = ('Others Interactions'),
        max_length = 50,
        null = True,)
    hectare = models.CharField(
        help_text = ('Hectare'),
        max_length = 50,)
    hectare_squirrel_Number = models.CharField(
        help_text = ('Squirrel Number'),
        max_length = 50,)
    latlong = models.CharField(
        help_text = ('LatLong Point'),
        max_length = 50,
        )
    highlight_fur_color = models.CharField(
        help_text = ('Highlight Fur Color'),
        max_length = 50,
        )
    color_note = models.CharField(
        help_text = ('Color Note'),
        max_length = 50,)
    combination_of_primary_and_highlight_color = models.CharField(
        help_text = ('Combination of Primary and Highlight'),
        max_length = 50,)
    above_ground_sighter_measurement = models.CharField(
            help_text = ('Above Ground Sighter Measurement'),
            max_length = 50,
            null = True,
            )
    moans = models.CharField(
            help_text='Moans',
            max_length = 50,)
    
    def __str__(self):
        return self.ID

