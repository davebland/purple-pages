from django.db import models
from django.contrib.auth.models import User
from django.template.loader import render_to_string

from boards.models import Board

class Advert(models.Model):
    """ Data model for adverts """
    title = models.CharField(max_length=30)
    textContent = models.TextField(default="")
    
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    on_boards = models.ManyToManyField(Board)

    def __str__(self):
        return self.title

    def to_html(self):
        """ Rended the advert to a html string using the relevant template """
        return render_to_string('ad_template_1.html', {'advert':self})