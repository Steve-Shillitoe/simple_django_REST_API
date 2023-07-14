"""
Unit tests of functions in view.py and the model in base.models
"""

from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from base.models import Item
from datetime import datetime, timedelta
from django.db import models
from django.utils import timezone

class GetDataTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()


    def test_get_data(self):
        # Create some sample data for testing
        # Assuming `Item` is the model name
        Item.objects.create(name="Item 1")
        Item.objects.create(name="Item 2")

        # Make a GET request
        response = self.client.get('')

        # Assert that the response status code is 200 (HTTP OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the response data is as expected
        self.assertIn("Item 1", response.data[0]['name'])
        self.assertIn("Item 2", response.data[1]['name'])


class AddItemTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_add_item(self):
        data = {"name":"AnItem"}
        response = self.client.post('/add/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #If the data was successfully added, we should be able to GET it
        # Make a GET request
        response = self.client.get('')
        # Assert that the response status code is 200 (HTTP OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assert that the response data is as expected
        self.assertIn("AnItem", response.data[0]['name'])


class ItemTestCase(TestCase):
    def setUp(self):
        pass  # No setup needed for this test case

    def test_item_properties(self):
        item = Item.objects.create(name="Test Item")

        # Assert that the 'id' == 1 
        self.assertEqual(item.id, 1)
 

        # Assert that the 'name' =="Test Item" and has the correct max_length
        self.assertEqual(item.name, "Test Item")
        max_length = item._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)
        
        # Make the current datetime offset-naive
        current_datetime = timezone.now()

        # Assert that the 'created' field is set to the current date/time
        self.assertAlmostEqual(item.created, current_datetime, delta=timedelta(seconds=1))


