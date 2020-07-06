from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CardModelForm
from .models import Card


def card_list_view(request):
    query_set = Card.objects.get_queryset()
    context = {'card_list': query_set}
    return render(request, 'marketapp/list.html', context)


@staff_member_required()
def card_create_view(request):
    if request.method == 'POST':
        form = CardModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/market/')
    else:
        form = CardModelForm()
    return render(request, 'marketapp/form.html', {'form': form})


def card_detail_view(request, slug):
    obj = get_object_or_404(Card, slug=slug)
    context = {'card': obj}
    return render(request, 'marketapp/detail.html', context)


@staff_member_required()
def card_update_view(request, slug):
    obj = get_object_or_404(Card, slug=slug)
    if request.method == 'POST':
        form = CardModelForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/market')
    else:
        form = CardModelForm()
    return render(request, 'marketapp/form.html',
                  {'form': form, 'title': f"Update {obj.title}"})


@staff_member_required()
def card_delete_view(request, slug):
    obj = get_object_or_404(Card, slug=slug)
    if request.method == "POST":
        obj.delete()
        return redirect("/market")
    return render(request, 'marketapp/delete.html', {'card': obj})
