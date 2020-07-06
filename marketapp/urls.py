from django.urls import path

from .views import (
    card_list_view,
    card_detail_view,
    card_update_view,
    card_delete_view
)

urlpatterns = [
    path('', card_list_view),
    path('<str:slug>/', card_detail_view),
    path('<str:slug>/edit/', card_update_view),
    path('<str:slug>/delete/', card_delete_view)
]
