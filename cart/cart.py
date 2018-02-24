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