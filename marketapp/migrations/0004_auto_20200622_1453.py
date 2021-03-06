# Generated by Django 3.0.7 on 2020-06-22 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketapp', '0003_auto_20200622_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='card_set',
            field=models.CharField(choices=[('HLF', 'Hall Of Fame'), ('NAX', 'Naxxramas'), ('GVG', 'Goblins VS Gnomes'), ('BRM', 'Blackrock Mountain'), ('TGT', 'The Grand Tournament'), ('LOE', 'The League of Explorers'), ('OGO', 'Old Gods'), ('KAR', 'Karazhan'), ('GAD', 'Gadgetzan'), ('UNG', 'Un Goro'), ('FRT', 'Frozen Throne'), ('CLA', 'Classic')], default='', max_length=3),
        ),
    ]
