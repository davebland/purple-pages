from django.db import models

class Advert(models.Model):
    """ Data model for adverts """
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title
