from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product
from .forms import ProductForm

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
    product = Product.objects.get(pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'catalogmanager/product.html', context)


def addProduct(request, product_id=None):
    product = None
    if product_id is not None:
        product = Product.objects.get(pk=product_id)
    if request.method == 'GET':
        form = ProductForm(instance=product)
    else:

        form = ProductForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            product = Product.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                width=form.cleaned_data['width'],
                length=form.cleaned_data['length'],
                height=form.cleaned_data['height'],
                weight=form.cleaned_data['weight'],
                value=form.cleaned_data['value']
            )
            return HttpResponseRedirect(reverse('product', kwargs={'product_id': product.id}))

    return render(request, 'catalogmanager/product_form.html', {
        'form': form,
        'is_editing': True if product else False
    })