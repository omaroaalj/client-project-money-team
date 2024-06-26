from django.test import TestCase
from django.urls import reverse
from .models import ContactEntry

# Create your tests here.


# Check if views are there and have a code of 200
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

    def test_retirement(self):
        response = self.client.get(reverse("financeWebsite:retirement"))
        self.assertEqual(response.status_code, 200)

    def test_alt_investments(self):
        response = self.client.get(reverse("financeWebsite:alternativeInvestments"))
        self.assertEqual(response.status_code, 200)

    def test_life_insurance(self):
        response = self.client.get(reverse("financeWebsite:lifeInsurance"))
        self.assertEqual(response.status_code, 200)

    def test_healthcare(self):
        response = self.client.get(reverse("financeWebsite:healthcare"))
        self.assertEqual(response.status_code, 200)

# Check if form handles requests as expected
class FormTests(TestCase):
    def test_name_only(self):
        response = self.client.post(reverse("financeWebsite:submit_contact"), {"name": "TestName"})
        self.assertContains(response, "Contact Me")
        self.assertContains(response, "This field is required.")

    def test_email_only(self):
        response = self.client.post(reverse("financeWebsite:submit_contact"), {"email": "test@test.com"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Contact Me")
        self.assertContains(response, "This field is required.")
        self.assertQuerySetEqual(ContactEntry.objects.all(), [])

    def test_message_only(self):
        response = self.client.post(reverse("financeWebsite:submit_contact"), {"message": "Hello there"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Contact Me")
        self.assertContains(response, "This field is required.")
        self.assertQuerySetEqual(ContactEntry.objects.all(), [])

    def test_valid_form_submission(self):
        post_data = {"name": "Test", "email": "test@test.com", "message": "This is the message."}
        response = self.client.post(reverse("financeWebsite:submit_contact"), post_data)
        self.assertEqual(ContactEntry.objects.count(), 1)
        entry = ContactEntry.objects.get(pk=1)
        self.assertEqual(entry.name, "Test")
        self.assertEqual(entry.email, "test@test.com")
        self.assertEqual(entry.message, "This is the message.")
        self.assertEqual(response.status_code, 302)

    def test_invalid_email(self):
        post_data = {"name": "Test", "email": "InvalidEmail", "message": "This is the message."}
        response = self.client.post(reverse("financeWebsite:submit_contact"), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Contact Me")
        self.assertContains(response, "Enter a valid email address.")
        self.assertQuerySetEqual(ContactEntry.objects.all(), [])

    def test_long_name(self):
        name_length = 101
        long_name = "".join(["a" for _ in range(name_length)])
        post_data = {"name": long_name, "email": "test@test.com", "message": "This is the message"}
        response = self.client.post(reverse("financeWebsite:submit_contact"), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Contact Me")
        self.assertContains(response, "Ensure this value has at most 100 characters (it has " + str(name_length) + ").")
        self.assertQuerySetEqual(ContactEntry.objects.all(), [])
