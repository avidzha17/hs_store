from django import forms

from .models import Card


class CardModelForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['name', 'image', 'cost', 'attack', 'health', 'description', 'golden',
                  'rarity', 'card_set', 'hero_class', 'price', 'in_stock', 'slug', ]

    def clean_title(self):
        instance = self.instance
        title = self.cleaned_data.get('title')
        queryset = Card.objects.filter(title__iexact=title)
        if instance is not None:
            queryset = queryset.exclude(pk=instance.pk)
        if queryset.exists():
            raise forms.ValidationError("This title has already been used. Please try again.")
        return title
