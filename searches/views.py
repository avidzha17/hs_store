from django.shortcuts import render

from marketapp.models import Card
from .models import SearchQuery


def search_card_view(request):
    query = request.GET.get('q', None)  # q in navbar.html
    user = None
    if request.user.is_authenticated:
        user = request.user
    context = {"query": query}
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        card_list = Card.objects.search_title(query=query)
        context['card_list'] = card_list
    return render(request, 'searches/search_result.html', context)


def filter_search_view(request):
    query_card_set = request.GET.get('q_card_set', None)
    query_hero_class = request.GET.get('q_hero_class', None)
    query_cost = request.GET.get('q_cost', None)
    query_golden = request.GET.get('q_golden', None)
    query_sort = request.GET.get('q_sort', None)

    input_dict = {'card_set': query_card_set, 'hero_class': query_hero_class,
                  'cost': query_cost, 'golden': query_golden, 'sort': query_sort}

    values = input_dict.values()
    if set(values) == {'-', None}:
        context = {'card_list': Card.objects.get_queryset()}
        return render(request, 'marketapp/list.html', context)

    card_set_list = Card.CARD_SET_CHOICES
    hero_class_list = Card.HERO_CLASS_CHOICES

    if input_dict.get('card_set'):
        for tup in card_set_list:
            if query_card_set in tup:
                input_dict.update({'card_set': tup[0]})

    if input_dict.get('hero_class'):
        for tup in hero_class_list:
            if query_hero_class in tup:
                input_dict.update({'hero_class': tup[0]})

    if input_dict.get('golden') == 'on':
        input_dict.update({'golden': True})
    else:
        input_dict.update({'golden': False})

    user = None
    if request.user.is_authenticated:
        user = request.user

    context = {"query": input_dict}
    SearchQuery.objects.create(user=user, query=input_dict)
    card_list = Card.objects.filter_search(query=input_dict)
    context['card_list'] = card_list

    return render(request, 'searches/search_result.html', context)
