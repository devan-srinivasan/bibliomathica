# Generated by Django 4.0.6 on 2022-07-30 02:29

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, unique=True)),
                ('question', models.CharField(max_length=300)),
                ('answer', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('topic', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
