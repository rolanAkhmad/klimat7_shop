from .cart import Cart

def cart(request):
    cart = Cart(request)
    productsstring = ''

    for item in cart:
        product = item['product']
        b = "{'id': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s', 'total_price': '%s'}," % (product.id, product.title, product.price, item['quantity'], item['total_price'])
        productsstring += b

    return {'cart': Cart(request), 'productsstring': productsstring}