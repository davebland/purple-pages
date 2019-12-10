from django.db import models
from django.contrib.auth.models import User
from django.template.loader import render_to_string

from relativefilepathfield.fields import RelativeFilePathField

import os
from django.conf import settings

from boards.models import Board

class AdvertTemplate(models.Model):
    """ Data model for an advert template """
    name = models.CharField(max_length=30)
    template_file = RelativeFilePathField(path=os.path.join(settings.BASE_DIR, "adverts", "templates"),match="ad_template_*")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Advert(models.Model):
    """ Data model for adverts """

    IMAGE_UPLOAD_PATH = "images/adverts/"

    # Advert content attributes
    title = models.CharField(max_length=30)
    strapline = models.CharField(max_length=30, blank=True)
    textContent = models.TextField(blank=True)
    image = models.ImageField(upload_to=IMAGE_UPLOAD_PATH, blank=True)
    link_text = models.CharField(max_length=30, blank=True)
    link_url = models.URLField(blank=True)
    
    # Advert meta
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    impression_counter = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    on_boards = models.ManyToManyField(Board)
    template = models.ForeignKey(AdvertTemplate, on_delete=models.PROTECT, default=1)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def to_html(self):
        """ Render the advert to a html string using the relevant template """
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