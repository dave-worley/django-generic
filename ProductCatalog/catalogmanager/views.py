from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product

# Create your views here.
def index(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 9)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {
        'products': products
    }
    return render(request, 'catalogmanager/index.html', context)

def productDetail(request, product_id):
    product = Product.objects.get(id = product_id)
    context = {
        'product': product
    }
    return render(request, 'catalogmanager/product.html', context)