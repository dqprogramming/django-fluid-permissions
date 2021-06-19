from django.db import models
from django.contrib.auth.models import Group


class ViewGroup(models.Model):
    view_name = models.CharField(
        max_length=255,
    )
    groups = models.ManyToManyField(
        Group,
        blank=True,
    )

    def __str__(self):
        return "Group permissions for {}".format(
            self.view_name,
        )
