# Manual import of postcode districts

import csv

from .models import PostCodeDistrict

def import_post_codes(csv_file_name):
    """ Take a csv file and import first column as postcode districts """

    with open(csv_file_name, newline='') as postcode_csv:
        districts = csv.reader(postcode_csv, delimiter=',', quotechar='"')
        pcode_objs = []        
        for row in districts:
            pcode_objs.append(PostCodeDistrict(post_code=row[0]))

    # Remove the field name
    pcode_objs.pop(0) 

    # DELETE ALL OBJECTS AND CREATE NEW
    if (input("Delete {} districts? y/n:".format(PostCodeDistrict.objects.count()))) == "y":
        PostCodeDistrict.objects.all().delete()
    if (input("Create {} districts? y/n:".format(len(pcode_objs)))) == "y":
        PostCodeDistrict.objects.bulk_create(pcode_objs)