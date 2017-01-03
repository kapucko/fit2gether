from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from .abstract import Fit2getherModel, FromToModel

USER = settings.AUTH_USER_MODEL
# Create your models here.



#group of users
class Team(Fit2getherModel):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True)
    description = models.TextField(blank=True)
    editors = models.ManyToManyField(USER, blank=True, related_name='team_editors')
    members = models.ManyToManyField(USER, blank=True, related_name='team_members')


#defines occurence of regular event
class EventOccurence(FromToModel):
    MONDAY = 'Mon'
    TUESDAY = 'Tues'
    WEDNESDAY = 'Wed'
    THURSDAY = 'Thurs'
    FRIDAY = 'Fri'
    SATURDAY = 'Sat'
    SUNDAY = 'Sun'

    DAY_CHOICES = (
        (MONDAY, _('Monday')),
        (TUESDAY, _('Tuesday')),
        (WEDNESDAY, _('Wednesday')),
        (THURSDAY, _('Thursday')),
        (FRIDAY, _('Friday')),
        (SATURDAY, _('Saturday')),
        (SUNDAY, _('Sunday')),
    )

    day = models.CharField(max_length=20, choices=DAY_CHOICES)
    period_start = models.DateTimeField()
    period_end = models.DateTimeField()
    event_start = models.DateTimeField()
    event_end = models.DateTimeField()
    event = models.ForeignKey('Event', related_name='event_occurence', on_delete=models.CASCADE)

# TODO: set relationship between event and team/owner
#spawns events
class ReqularEvent(models.Model):
    name = models.CharField(max_length=128)
    location = models.ForeignKey('Location', related_name='reg_event_location', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    min_capacity = models.IntegerField(blank=True)
    max_capacity = models.IntegerField(blank=True)



#single event
class Event(models.Model):

    DRAFT = 'draft'
    PUBLISHED = 'published'
    PRIVATE = 'private'
    EXPIRED = 'expired'

    EVENT_STATUS_CHOICES = (
        (DRAFT, _('Draft')),
        (PUBLISHED, _('Published')),
        (PRIVATE, _('Private')),
        (EXPIRED, _('Expired')),
    )

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.ForeignKey('Location', related_name='event_location', on_delete=models.CASCADE)
    min_capacity = models.IntegerField(blank=True)
    max_capacity = models.IntegerField(blank=True)
    invited = models.ManyToManyField(USER, blank=True, related_name='event_invited')
    going = models.ManyToManyField(USER, blank=True, related_name='event_going')
    not_going = models.ManyToManyField(USER, blank=True, related_name='event_not_going')
    category = models.ForeignKey('EventCategory', related_name='event_category', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=EVENT_STATUS_CHOICES)


class Location(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True)
    address = models.CharField(max_length=128)
    gps_coord_x = models.FloatField(blank=True, null=True)
    gps_coord_y = models.FloatField(blank=True, null=True)
    url = models.CharField(max_length=128, blank=True)
    admin = models.ForeignKey(USER, related_name='location_admin')
    editors = models.ManyToManyField(USER, blank=True, related_name='location_editors')


class EventCategory(models.Model):
    name = models.CharField(max_length=128)
    display_name = models.CharField(max_length=128)

