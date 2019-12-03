# Generated by Django 2.2.6 on 2019-12-03 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0003_adverttemplate'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='template',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='adverts.AdvertTemplate'),
        ),
    ]