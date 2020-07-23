from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:id>/', views.cart_add, name='cart_add'),
    path('item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('item_remove/<int:id>/',
         views.item_remove, name='item_remove'),
    path('item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart_clear/', views.cart_clear, name='cart_clear'),
    path('checkout/', views.to_checkout, name='to_checkout'),
    path('', views.cart_detail, name='cart_detail'),
]
