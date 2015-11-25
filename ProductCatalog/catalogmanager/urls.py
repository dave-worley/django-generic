from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<product_id>\d+)/', views.productDetail, name='product'),
]