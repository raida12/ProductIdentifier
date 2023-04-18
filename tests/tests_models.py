from django.test import TestCase, Client
from django.contrib.auth.models import User , Group
from home.model.models import Customer, Product

class TestModels(TestCase):
    
    def setUp(self):
        
        self.user2 = User.objects.create_user('anik2','smnavinnayeranik@gmail.com','1234')
        
        self.customer2 = Customer.objects.create(
            user = self.user2,
            name = 'anik2',
            phone = '01710899896',
            email = 'anik5758@gmail.com'
        )
        
    
    def test_customer_model_creation(self):
        self.assertEquals(self.customer2.user.username,'anik2')
        
    def test_product_model_creation(self):
        
        product = Product.objects.create(
            customer = self.customer2,
            name = 'new product',
        )
        self.assertEquals(product.name,'new product')
        self.assertEquals(product.customer.name,'anik2')