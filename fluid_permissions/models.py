from django.db import models
from django.contrib.auth.models import Group


class ViewGroup(models.Model):
    view_name = models.CharField(
        max_length=255.
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "View {} linked to group {}".format(
            self.view_name,
            self.group,
        )
