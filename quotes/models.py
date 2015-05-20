# Created: 05/02/2015   Modified: 05/20/2015

# Author: Vipul Borikar


from django.db import models
from django.utils import timezone

class Quote(models.Model):
    quote_text = models.CharField(max_length=500)
    average_rating = models.IntegerField(default=0)
    user_who_uploaded = models.CharField(max_length=100)
    submission_date = models.DateTimeField(default=timezone.now())
    quote_author = models.CharField(default="anonymous",max_length=50)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.quote_text

