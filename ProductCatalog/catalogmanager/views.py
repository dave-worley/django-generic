import csv
from io import TextIOWrapper
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product
from .forms import ProductForm
from .forms import ProductsUploadForm

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
        'products': products,
        'message': request.session.get('message')
    }
    request.session['message'] = None
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


def removeProduct(request, product_id):
    product = Product.objects.get(pk=product_id)
    name = product.name
    product.delete()
    request.session['message'] = 'Product {} was successfully deleted.'.format(name)
    return HttpResponseRedirect(reverse('home'))


def handle_products_csv(csv_file):
    f = TextIOWrapper(csv_file.file, encoding='ascii')
    reader = csv.reader(f)
    products = []
    for row in reader:
        product = Product.objects.create(
            name=row[0],
            description=row[1],
            width=row[2],
            length=row[3],
            height=row[4],
            weight=row[5],
            value=row[6]
        )
        products.append(product)
    return products


def uploadProducts(request):
    products = None
    if request.method == 'GET':
        form = ProductsUploadForm()
    else:
        form = ProductsUploadForm(request.POST, request.FILES)
        if form.is_valid():
            products = handle_products_csv(request.FILES['file'])
    return render(request, 'catalogmanager/products_upload.html', {
        'form': form,
        'products': products
    })
