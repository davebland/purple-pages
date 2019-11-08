from django.db import models

class PostCodeDistrict(models.Model):
    """ Data model for postcodedistrict database """
    postcode = models.CharField(max_length=4)

class Board(models.Model):
    """ Data model for notice boards """
    postCodeDistrict = models.OneToOneField(PostCodeDistrict, on_delete=models.PROTECT)
    name = models.CharField(max_length=30)    
    dateActive = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.postCodeDistrict.postcode