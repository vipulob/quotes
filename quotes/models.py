# Created: 05/02/2015   Modified: 05/02/2015

# Author: Vipul Borikar


from django.db import models

class Quote(models.Model):
    quote_text = models.CharField(max_length=500)
    average_rating = models.IntegerField(default=0)
    user_who_uploaded_id = models.IntegerField(default=0)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.quote_text

