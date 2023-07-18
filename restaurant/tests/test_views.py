from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK

from ..models import MenuItem


class MenuViewTest(APITestCase):
    def setUp(self):
        self.menu1 = MenuItem.objects.create(title="Pizza", price=100.00, inventory=50)
        self.menu2 = MenuItem.objects.create(title="Burger", price=80.00, inventory=100)
        self.menu3 = MenuItem.objects.create(title="Fries", price=50.00, inventory=200)

    def test_getall(self):
        url = reverse("menu-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, HTTP_200_OK)
        serialized_data = [
            {
                "id": self.menu1.id,
                "title": self.menu1.title,
                "price": f"{self.menu1.price:.2f}",
                "inventory": self.menu1.inventory,
            },
            {
                "id": self.menu2.id,
                "title": self.menu2.title,
                "price": f"{self.menu2.price:.2f}",
                "inventory": self.menu2.inventory,
            },
            {
                "id": self.menu3.id,
                "title": self.menu3.title,
                "price": f"{self.menu3.price:.2f}",
                "inventory": self.menu3.inventory,
            },
        ]
        self.assertEqual(response.data, serialized_data)
