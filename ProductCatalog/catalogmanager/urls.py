from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/', views.addProduct, name='addproduct'),
    url(r'^(?P<product_id>\d+)/', views.productDetail, name='product'),
]