from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/', views.addProduct, name='addproduct'),
    url(r'^edit/(?P<product_id>\d+)/', views.addProduct, name='editproduct'),
    url(r'^remove/(?P<product_id>\d+)/', views.removeProduct, name='removeproduct'),
    url(r'^(?P<product_id>\d+)/', views.productDetail, name='product'),
]