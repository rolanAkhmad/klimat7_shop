from django.shortcuts import render, redirect

from .cart import Cart

from apps.order.models import Order, OrderItem


def cart(request):
    cart = Cart(request)
    productsstring = ''

    for item in cart:
        product = item['product']
        b = "{'id': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s', 'total_price': '%s', 'image': '%s', 'get_absolute_url': '%s'}," % (product.id, product.title, product.price, item['quantity'], item['total_price'], product.get_main_image, product.get_absolute_url)
        productsstring += b

    context = {
        'cart': cart,
        'productsstring': productsstring,
    }

    return render(request, 'cart.html', context)

def checkout(request):
    cart = Cart(request)
    productsstring = ''

    for item in cart:
        product = item['product']
        b = "{'id': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s', 'total_price': '%s'}," % (product.id, product.title, product.price, item['quantity'], item['total_price'])
        productsstring += b

    context = {
        'cart': cart,
        'productsstring': productsstring,
    }
    
    if request.method == 'POST':
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            city = ''
            street = ''
            try:
                city = request.POST['city']
                street = request.POST['street']
            except:
                print('except: city | stret')
                city = ''
                street = ''
            phone = request.POST['phone']
            email = request.POST['email']
            description = ''
            try:
                description = request.POST['description']
            except:
                print('except: description')
                description = ''
            
            print("Формирую заказ")

            print('first_name:', first_name, 'last_name:', last_name, 'email:', email, 'city:', city, 'street:', street, 'phone:', phone, 'description:', description)

            order = Order.objects.create(first_name=first_name,
                                last_name=last_name,
                                email=email,
                                city=city,
                                street=street,
                                phone=phone,
                                description=description,
                                total_price=0)

            print("Заказ сформирован")

            print("Формирую order item'ы")
            try:
                for item in cart:
                    OrderItem.objects.create(order=order, product=item['product'], quantity=item['quantity'], price=item['total_price'])
                cart.clear()
            except:
                print('item except')

            return redirect('checkout_success')
        except:
            print('except: all post')

    return render(request, 'checkout.html', context)

def checkout_success(request):
    return render(request, 'success.html')