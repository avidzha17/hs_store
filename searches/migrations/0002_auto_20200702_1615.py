# Generated by Django 3.0.7 on 2020-07-02 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchquery',
            name='query',
            field=models.CharField(max_length=100),
        ),
    ]
