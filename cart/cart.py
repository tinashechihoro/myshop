from decimal import decimal
from django.conf import settings
from shop.models import Product


class Cart(object):
    """
    Cart class
    """
    def __init__(self,request):
        """
        Initialize the  cart
        """

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            #Save an empty cart in session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart  

    def add(self,product,quantity=1,updated_quantity=False):
        """
        Add a product to the cart or update its quantity
        """  
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0,
                                     'price':str(product.price)}
        if updated_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()                                       