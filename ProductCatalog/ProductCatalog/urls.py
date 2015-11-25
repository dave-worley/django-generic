from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^product/', include('catalogmanager.urls')),
    url(r'^$', 'catalogmanager.views.index', name='home'),
]
