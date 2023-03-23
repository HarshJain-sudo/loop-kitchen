import datetime
import uuid
from django.db import models

WEEKDAYS = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)


class Store(models.Model):
    store_id = models.TextField(default=uuid.uuid4)
    timezone = models.TextField(default="America/Chicago")


class StoreBusinessHour(models.Model):
    store_id = models.TextField(default="NA")
    timestamp_utc = models.DateTimeField(default=None)
    status = models.CharField(max_length=255)


class StoreMenuHour(models.Model):
    store_id = models.TextField(default="NA")
    day_of_week = models.IntegerField(choices=WEEKDAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()


class Report(models.Model):
    store_id = models.TextField(default="NA")
    uptime_last_hour = models.FloatField()
    uptime_last_day = models.FloatField()
    uptime_last_week = models.FloatField()
    downtime_last_hour = models.FloatField()
    downtime_last_day = models.FloatField()
    downtime_last_week = models.FloatField()
