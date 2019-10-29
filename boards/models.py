from django.db import models

class Board(models.Model):
    """ Data model for notice boards """
    postCodeDistrict = models.CharField(max_length=4)
    name = models.CharField(max_length=30)    
    dateActive = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.postCodeDistrict