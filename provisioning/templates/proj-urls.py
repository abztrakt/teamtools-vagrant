from django.conf.urls import include, url
from django.contrib import admin
from skilltreeapp import urls as skilltree_urls
from labgeeks_chronos import urls as chronos_urls

urlpatterns = [
    url(r'^', include(skilltree_urls)),
    url(r'^chronos/', include(chronos_urls)),
]
