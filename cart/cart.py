from decimal import Decimal
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

    def save(self):
        """
        #Update the session cart
        """ 
        self.session[settings.CART_SESSION_ID] = self.cart
        #make the session as "modified" to make site it is saved
        self.session.modified = True

    def remove(self,product):
        """
        Remove a product from the cart
        """  
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save() 

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """  
        product_ids = self.cart.keys()
        #get the products objects and add them to the  cart
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product_id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item  

    def __len__(self):
        """
        Count all items in cart
        """ 
        return sum(item['quantity'] for item in self.cart.values())                
