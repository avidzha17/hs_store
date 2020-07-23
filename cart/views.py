from django.shortcuts import render, redirect
from marketapp.models import Card
from cart.cart import Cart
from .forms import CartCheckoutForm
from .context_processor import cart_total_amount


def cart_add(request, id):
    cart = Cart(request)
    product = Card.objects.get(id=id)
    cart.add(product=product)
    return redirect("/cart")


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


def item_remove(request, id):
    cart = Cart(request)
    product = Card.objects.get(id=id)
    cart.remove(product=product)
    return redirect("cart_detail")


def cart_detail(request):
    return render(request, 'cart/cart_detail.html')


def to_checkout(request):
    cart = Cart(request)

    cart_items = []
    for item in list(cart.cart.values()):
        temp_dict = dict(item)
        dict_item = {temp_dict.get('name'): {'quantity': temp_dict.get('quantity'), 'price': temp_dict.get('price')}}
        cart_items.append(dict_item)
    cart_items.append(cart_total_amount(request))

    if request.method == 'POST':
        form = CartCheckoutForm(request.POST)
        if form.is_valid():
            form.save()
            cart.clear()
            return redirect('/market/')
    else:
        form = CartCheckoutForm()
    return render(request, 'cart/checkout_form.html', {'form': form, 'cart_items': cart_items})
