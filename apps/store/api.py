import json
import stripe

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect

from apps.cart.cart import Cart
from apps.order.models import Order


from apps.order.utils import checkout

from .models import Product

# def api_add_to_cart(request):
#     data = json.loads(request.body)
#     jsonresponse = {'success': True}
#     product_id = data['product_id']
#     update = data['update']
#     quantity = data['quantity']

#     print(data)
#     print(data['product_id'])

#     cart = Cart(request)
    
#     product = get_object_or_404(Product, pk=product_id)

#     if not update:
#         cart.add(product=product, quantity=1, update_quantity=False)
#     else:
#         cart.add(product=product, quantity=quantity, update_quantity=True)

#     cart.total_cost = cart.get_total_cost()

#     return JsonResponse(jsonresponse)

def api_add_to_cart(request):
    cart = Cart(request)
    jsonresponse = {'success': True}

    product_id = request.GET.get('product_id')
    count = request.GET.get('count')

    product = get_object_or_404(Product, id=product_id)
    
    cart.add(product=product, quantity=count)

    return JsonResponse(jsonresponse)

def api_cart_get_total_length(request):
    cart = Cart(request)
    total_length = cart.get_total_length()
    return JsonResponse({'success':True, 'total_length': total_length})

def api_increment_quantity(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    product_id = data['product_id']

    cart = Cart(request)
    
def api_remove_from_cart(request):
    jsonresponse = {'success': True}
    product_id = request.GET.get('product_id')

    cart = Cart(request)
    cart.remove(product_id)

    return JsonResponse(jsonresponse)