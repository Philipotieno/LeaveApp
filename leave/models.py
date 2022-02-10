import numpy as np
from dateutil.parser import *
from django.db import models


class Leave(models.Model):

    LEAVE_TYPE = (("Normal leave", "Normal leave"), ("Sick leave", "Sick leave"))

    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    leave_type = models.CharField(
        max_length=20, choices=LEAVE_TYPE, default="Normal leave"
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "leave"

    @property
    def timediff(self):
        res = np.busday_count(self.start_date, self.end_date)
        return res
