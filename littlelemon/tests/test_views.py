from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        item = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        item2 = Menu.objects.create(Title="IceCream2", Price=50, Inventory=80)
    def test_getall(self):
        items = Menu.objects.all()
        self.assertEqual(str(items[0]), "IceCream : 80.00")
        self.assertEqual(str(items[1]), "IceCream2 : 50.00")
