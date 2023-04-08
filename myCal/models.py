from django.db import models
from django.urls import reverse


class Event(models.Model):
    # define fields for the event model
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    # ...

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event_detail', args=[str(self.id)])
