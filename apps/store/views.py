from django.core import paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


from .models import Product, Category
    
def product_list(request):
    object_list = Product.objects.filter().order_by('?')

    paginator = Paginator(object_list, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'object_list': page_obj,
        'page_obj': page_obj,
        'paginator': paginator
    }

    return render(request, 'product_list.html', context)

def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product
    }

    return render(request, 'product_detail.html', context)

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    object_list = category.products.all()

    paginator = Paginator(object_list, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'category': category,
        'object_list': page_obj,
        'page_obj': page_obj,
        'paginator': paginator
    }
    
    return render(request, 'product_list_by_category.html', context)

def search(request):
    query = request.GET.get('query')
    products = Product.objects.filter(Q(title__icontains=query))

    paginator = Paginator(products, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'query': query,
        'object_list': page_obj,
        'page_obj': page_obj,
        'paginator': paginator
    }

    return render(request, 'search.html', context)