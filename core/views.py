from django.shortcuts import render
from .listview import ListView
from .models import Product


def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'core/index.html', context)


class ProductList(ListView):
    
    model = Product
    template_name = 'core/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(price__gt=20000)
    