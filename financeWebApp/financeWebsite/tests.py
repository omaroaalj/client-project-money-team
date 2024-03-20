from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class ViewTests(TestCase):

    def test_index(self):
        response = self.client.get(reverse("financeWebsite:index"))
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        response = self.client.get(reverse("financeWebsite:about"))
        self.assertEqual(response.status_code, 200)

    def test_services(self):
        response = self.client.get(reverse("financeWebsite:services"))
        self.assertEqual(response.status_code, 200)

    def test_contact(self):
        response = self.client.get(reverse("financeWebsite:contact"))
        self.assertEqual(response.status_code, 200)

    def test_portfolio(self):
        response = self.client.get(reverse("financeWebsite:portfolio"))
        self.assertEqual(response.status_code, 200)
