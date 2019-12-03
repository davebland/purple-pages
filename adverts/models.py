from django.db import models
from django.contrib.auth.models import User
from django.template.loader import render_to_string

import os
from django.conf import settings

from boards.models import Board

class AdvertTemplate(models.Model):
    """ Data model for an advert template """
    name = models.CharField(max_length=30)
    template_file = models.FilePathField(path=os.path.join(settings.BASE_DIR, "adverts/templates"),match="ad_template_*")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Advert(models.Model):
    """ Data model for adverts """
    title = models.CharField(max_length=30)
    textContent = models.TextField(default="")
    impression_counter = models.IntegerField(default=0)
    template = models.ForeignKey(AdvertTemplate, on_delete=models.PROTECT, default=1)
    
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    on_boards = models.ManyToManyField(Board)

    def __str__(self):
        return self.title

    def to_html(self):
        """ Rended the advert to a html string using the relevant template """
        return render_to_string(self.template.template_file, {'advert':self})

    def board_list(self):
        """ Return a query set of boards this Advert appears on """
        board_list = self.on_boards.all()
        return board_list

    def add_impression(self):
        """ Increase the impression counter by 1 for this advert """
        try:
            self.impression_counter += 1
            self.save(update_fields=['impression_counter'])
        except:
            self.impression_counter = 0