from django.db import models
from django.urls import reverse


class events(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    manager = models.CharField(max_length=60)
    event_date = models.DateField()
    venue = models.CharField(max_length=120)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    name = models.TextField(max_length=120 )
    description = models.TextField(blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("myapp_events_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("myapp_events_update", args=(self.pk,))
