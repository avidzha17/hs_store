from django.conf import settings
from django.db import models
from django.db.models import Q

User = settings.AUTH_USER_MODEL


class CardQuerySet(models.QuerySet):
    def find_by_title(self, query):
        lookup = (
            Q(title__icontains=query)
        )
        return self.filter(lookup)

    def fields_filter(self, query):

        if query.get('cost') != '-':
            if query.get('cost') == '7+':
                self = self.filter(cost__gte=7)
            else:
                self = self.filter(cost__exact=query.get('cost'))

        if query.get('card_set') != '-':
            self = self.filter(card_set__exact=query.get('card_set'))
        if query.get('hero_class') != '-':
            self = self.filter(hero_class__exact=query.get('hero_class'))
        if query.get('golden') is True:
            self = self.filter(golden__exact=query.get('golden'))
        return self

    def order_by_title(self):
        return self.order_by('title')


class CardManager(models.Manager):
    def get_queryset(self):
        return CardQuerySet(self.model, using=self._db)

    def search_title(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().find_by_title(query)

    def filter_search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().fields_filter(query)


class Card(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='image/')
    cost = models.IntegerField(default=0)  # mana cost
    attack = models.IntegerField(default=0)
    health = models.IntegerField(default=0)
    description = models.CharField(max_length=200, null=True, blank=True)
    golden = models.BooleanField(default=False)

    FREE = 'FR'
    COMMON = 'CO'
    RARE = 'RA'
    EPIC = 'EP'
    LEGENDARY = 'LE'

    RARITY_CHOICES = [
        (FREE, 'Free'),
        (COMMON, 'Common'),
        (RARE, 'Rare'),
        (EPIC, 'Epic'),
        (LEGENDARY, 'Legendary')
    ]
    rarity = models.CharField(choices=RARITY_CHOICES, max_length=2, default='')

    HALL_OF_FAME = 'HLF'
    NAXXRAMAS = 'NAX'
    GOBLINS_VS_GNOMES = 'GVG'
    BLACKROCK_MOUNTAIN = 'BRM'
    THE_GRAND_TOURNAMENT = 'TGT'
    THE_LEAGUE_OF_EXPLORERS = 'LOE'
    OLD_GODS = 'OGO'
    KARAZHAN = 'KAR'
    GADGETZAN = 'GAD'
    UN_GORO = 'UNG'
    FROZEN_THRONE = 'FRT'
    CLASSIC = 'CLA'

    CARD_SET_CHOICES = [
        (HALL_OF_FAME, 'Hall Of Fame'),
        (NAXXRAMAS, 'Naxxramas'),
        (GOBLINS_VS_GNOMES, 'Goblins VS Gnomes'),
        (BLACKROCK_MOUNTAIN, 'Blackrock Mountain'),
        (THE_GRAND_TOURNAMENT, 'The Grand Tournament'),
        (THE_LEAGUE_OF_EXPLORERS, 'The League of Explorers'),
        (OLD_GODS, 'Old Gods'),
        (KARAZHAN, 'Karazhan'),
        (GADGETZAN, 'Gadgetzan'),
        (UN_GORO, 'Un Goro'),
        (FROZEN_THRONE, 'Frozen Throne'),
        (CLASSIC, 'Classic')
    ]
    card_set = models.CharField(choices=CARD_SET_CHOICES, max_length=3, default='')

    DRUID = 'DR'
    HUNTER = 'HU'
    MAGE = 'MA'
    PALADIN = 'PA'
    PRIEST = 'PR'
    ROGUE = 'RO'
    SHAMAN = 'SH'
    WARLOCK = 'WL'
    WARRIOR = 'WA'
    COMMON_CLASS = 'CC'

    HERO_CLASS_CHOICES = [
        (DRUID, 'Druid'),
        (HUNTER, 'Hunter'),
        (MAGE, 'Mage'),
        (PALADIN, 'Paladin'),
        (PRIEST, 'Priest'),
        (ROGUE, 'Rogue'),
        (SHAMAN, 'Shaman'),
        (WARLOCK, 'Warlock'),
        (WARRIOR, 'Warrior'),
        (COMMON_CLASS, 'Common')
    ]

    hero_class = models.CharField(choices=HERO_CLASS_CHOICES, max_length=2, default='')

    price = models.IntegerField(default=0)
    in_stock = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    objects = CardManager()

    def get_absolute_url(self):
        return f"/market/{self.slug}"

    def get_edit_url(self):
        return f"/market/{self.slug}/edit"

    def get_delete_url(self):
        return f"/market/{self.slug}/delete"


class CardBack(models.Model):
    pass


class Hero(models.Model):
    pass
