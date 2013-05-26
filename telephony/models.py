from django.db import models

class Asterisk(models.Model):

    name = models.CharField(max_length=100, unique=True)
    bind = models.CharField(max_length=50, unique=True)
    secret = models.CharField(max_length=50, unique=True)
    user = models.CharField(max_length=50, unique=True)

    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    created_at = models.DateField(auto_now=True)


    class Meta:
        db_table = 'asterisk'
#        ordering = ['-created_at']

    def __unicode__(self):
        return self.name




