from django.shortcuts import render_to_response
from .models import Product

# Create your views here.
def index(request):
    context = {
        'products': Product.objects.all()[:10]
    }
    return render_to_response('catalogmanager/index.html', context)