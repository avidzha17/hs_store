# Generated by Django 3.0.7 on 2020-07-19 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketapp', '0015_auto_20200718_1337'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CardBack',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.DeleteModel(
            name='Hero',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
