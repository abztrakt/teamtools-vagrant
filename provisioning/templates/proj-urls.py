from django.conf.urls import include, url
from django.contrib import admin
from skilltreeapp import urls as skilltree_urls
from labgeeks_chronos import urls as chronos_urls
from punchclock import urls as punchclock_urls

urlpatterns = [
    url(r'^', include(skilltree_urls)),
    url(r'^chronos/', include(chronos_urls)),
    url(r'^punchclock/', include(punchclock_urls)),
    url(r'^accounts/login/$', 'skilltreeapp.views.pages.tools_login'),
    url(r'^accounts/logout/', 'skilltreeapp.views.pages.tools_logout'),
    url(r'^admin/', include(admin.site.urls)),
]
