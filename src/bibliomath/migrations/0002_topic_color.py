# Generated by Django 4.0.6 on 2022-08-09 17:59

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bibliomath', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='color',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None),
        ),
    ]