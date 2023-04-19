from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from .models import ContactForm
from .serializers import TwoSumSerializer, ContactFormSerializer


class ContactFormModelTest(TestCase):
    def setUp(self):
        self.contact = ContactForm.objects.create(
            first_name='John',
            last_name='Doe',
            phone_number='1234567890',
            email='john.doe@example.com',
            message='Hello, world!'
        )

    def test_contact_form_model(self):
        self.assertEqual(str(self.contact), 'john.doe@example.com')
        self.assertEqual(self.contact.full_name, 'John Doe')


class TwoSumSerializerTest(TestCase):
    def setUp(self):
        self.valid_data = {'num1': 2, 'num2': 3}
        self.invalid_data = {'num1': 2, 'num2': 'a'}

    def test_two_sum_serializer(self):
        serializer = TwoSumSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.get_sum(serializer.validated_data), 5)

        serializer = TwoSumSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())


class ContactFormSerializerTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'phone_number': '1234567890',
            'email': 'john.doe@example.com',
            'message': 'Hello, world!'
        }

    def test_contact_form_serializer(self):
        serializer = ContactFormSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        contact = serializer.save()

        self.assertEqual(contact.first_name, 'John')
        self.assertEqual(contact.last_name, 'Doe')
        self.assertEqual(contact.phone_number, '1234567890')
        self.assertEqual(contact.email, 'john.doe@example.com')
        self.assertEqual(contact.message, 'Hello, world!')


class TwoSumAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_two_sum_api_view(self):
        url = reverse("account:two-sum")
        data = {'num1': 2, 'num2': 3}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'sum': 5})


class ContactCreateAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("account:contact")
        self.valid_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'phone_number': '1234567890',
            'email': 'john.doe@example.com',
            'message': 'Hello, world!'
        }

    def test_contact_create_api_view(self):
        response = self.client.post(self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        contact = ContactForm.objects.get(pk=response.data['id'])
        self.assertEqual(contact.first_name, 'John')
        self.assertEqual(contact.last_name, 'Doe')
        self.assertEqual(contact.phone_number, '1234567890')
        self.assertEqual(contact.email, 'john.doe@example.com')
        self.assertEqual(contact.message, 'Hello, world!')