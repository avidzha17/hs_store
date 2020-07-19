from django.shortcuts import render, redirect
from marketapp.models import Card
from cart.cart import Cart


def cart_add(request, id):
    cart = Cart(request)
    product = Card.objects.get(id=id)
    cart.add(product=product)
    return redirect("/market")


def item_clear(request, id):
    cart = Cart(request)
    product = Card.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


def item_increment(request, id):
    cart = Cart(request)
    product = Card.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


def item_decrement(request, id):
    cart = Cart(request)
    product = Card.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


def cart_detail(request):
    return render(request, 'cart/cart_detail.html')
