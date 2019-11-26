from django.db import models
from django.contrib.auth.models import User
from django.template.loader import render_to_string

from boards.models import Board

class Advert(models.Model):
    """ Data model for adverts """
    title = models.CharField(max_length=30)
    textContent = models.TextField(default="")
    impression_counter = models.IntegerField(default=0)
    
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    on_boards = models.ManyToManyField(Board)

    def __str__(self):
        return self.title

    def to_html(self):
        """ Rended the advert to a html string using the relevant template """
        return render_to_string('ad_template_1.html', {'advert':self})

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