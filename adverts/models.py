from django.db import models
from django.template.loader import render_to_string

from relativefilepathfield.fields import RelativeFilePathField

import os
from django.conf import settings

class AdvertTemplate(models.Model):
    """ Data model for an advert template """
    name = models.CharField(max_length=30)
    template_file = RelativeFilePathField(path=os.path.join(settings.BASE_DIR, "adverts", "templates"),match="ad_template_*")
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Advert(models.Model):
    """ Data model for adverts """

    IMAGE_UPLOAD_PATH = "adverts/"

    # Advert content
    title = models.CharField(max_length=50)
    strapline = models.CharField(max_length=100, blank=True)
    text_content = models.TextField(blank=True)
    image = models.ImageField(upload_to=IMAGE_UPLOAD_PATH, height_field="image_height", width_field="image_width", blank=True)
    image_height = models.IntegerField(default=0)
    image_width = models.IntegerField(default=0)
    link_url = models.URLField(blank=True)
    link_text = models.CharField(max_length=30, blank=True)
    
    # Advert meta
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    view_counter = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    #pp_user = models.ForeignKey(User, on_delete=models.PROTECT)
    #on_boards = models.ManyToManyField(Board)
    template = models.ForeignKey(AdvertTemplate, on_delete=models.PROTECT, default=1)
    
    def __str__(self):
        return self.title

    def increase_view_count(self):
        """ Increase the view counter by 1 for this advert """
        try:
            self.view_counter += 1
            self.save(update_fields=['view_counter'])
        except:
            raise Exception("Unable to increase view count for advert {}".format(self.pk))

    def render(self):
        """ Render the advert to a html string using the relevant template and increase view count """
        self.increase_view_count()
        return render_to_string(self.template.template_file, {'advert':self})