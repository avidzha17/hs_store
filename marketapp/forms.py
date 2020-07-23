from django import forms

from .models import Card


class CardModelForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['name', 'image', 'cost', 'attack', 'health', 'description', 'golden',
                  'rarity', 'card_set', 'hero_class', 'price', 'in_stock', 'slug', ]

    def clean_name(self):
        instance = self.instance
        name = self.cleaned_data.get('name')
        queryset = Card.objects.filter(name__iexact=name)
        if instance is not None:
            queryset = queryset.exclude(pk=instance.pk)
        if queryset.exists():
            raise forms.ValidationError("This name has already been used. Please try again.")
        return name
