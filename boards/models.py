from django.db import models

class PostCodeDistrict(models.Model):
    """ Data model for a postcodedistrict """

    post_code = models.CharField(max_length=4)

    def __str__(self):
        return self.post_code

class Board(models.Model):
    """ Data model for notice boards """
    
    name = models.CharField(max_length=30)    
    date_active = models.DateField(auto_now_add=True)
    post_code = models.OneToOneField(PostCodeDistrict, on_delete=models.PROTECT)

    def __str__(self):
        return self.postCodeDistrict.postcode