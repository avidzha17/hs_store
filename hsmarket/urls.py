from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from .views import home_page, contacts_page
from marketapp.views import card_create_view
from searches.views import search_card_view, filter_search_view

urlpatterns = [
    path('', home_page),
    path('contacts/', contacts_page),
    path('market/', include('marketapp.urls')),
    path('admin/', admin.site.urls),
    path('new-card/', card_create_view),
    path('search/', search_card_view),
    path('filter-search/', filter_search_view)
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
