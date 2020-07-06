# Generated by Django 3.0.7 on 2020-06-22 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('marketapp', '0002_auto_20200622_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='card_set',
            field=models.CharField(choices=[('HLF', 'Hall Of Fame'), ('NAX', 'Naxxramas'), ('GVG', 'Goblins VS Gnomes'), ('BRM', 'Blackrock Mountain'), ('TGT', 'The Grand Tournament'), ('LOE', 'The League of Explorers'), ('OGO', 'Old Gods'), ('KAR', 'Karazhan'), ('GAD', 'Gadgetzan'), ('UNG', 'Un Goro'), ('FRT', 'Frozen Throne')], default='', max_length=3),
        ),
        migrations.AddField(
            model_name='card',
            name='hero_class',
            field=models.CharField(choices=[('DR', 'Druid'), ('HU', 'Hunter'), ('MA', 'Mage'), ('PA', 'Paladin'), ('PR', 'Priest'), ('RO', 'Rogue'), ('SH', 'Shaman'), ('WL', 'Warlock'), ('WA', 'Warrior')], default='', max_length=2),
        ),
        migrations.AddField(
            model_name='card',
            name='in_stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='card',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='card',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='card',
            name='attack',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='card',
            name='cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='card',
            name='health',
            field=models.IntegerField(default=0),
        ),
    ]
