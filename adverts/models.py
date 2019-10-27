from django.db import models

class Advert(models.Model):
    """ Data model for adverts """
    title = models.CharField(max_length=30)
    textContent = models.TextField(default="")

    def __str__(self):
        return self.title
