# Generated by Django 3.0.7 on 2020-07-02 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketapp', '0011_auto_20200702_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='golden',
            field=models.BooleanField(default=False),
        ),
    ]
