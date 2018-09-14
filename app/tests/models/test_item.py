from django.test import TestCase
from django.db import models

from app.tests.factories.items import ItemFactory


class ItemModelTest(TestCase):
    """
    This class defines the test suite for the item model.
    """

    item = None

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        ItemModelTest.item = ItemFactory.build()

    def test_name_field(self):
        field = ItemModelTest.item._meta.get_field("name")
        self.assertIsInstance(field, models.CharField)
        self.assertEqual(field.max_length, 100)
        self.assertFalse(field.blank)

    def test_done_field(self):
        field = ItemModelTest.item._meta.get_field("done")
        self.assertIsInstance(field, models.BooleanField)
        self.assertFalse(field.default)
        self.assertFalse(field.blank)

    def test_created_field(self):
        field = ItemModelTest.item._meta.get_field("created")
        self.assertIsInstance(field, models.DateTimeField)
        self.assertTrue(field.auto_now_add)

    def test_modified_field(self):
        field = ItemModelTest.item._meta.get_field("modified")
        self.assertIsInstance(field, models.DateTimeField)
        self.assertTrue(field.auto_now)

    def test_todo_field(self):
        field = ItemModelTest.item._meta.get_field("todo")
        self.assertIsInstance(field, models.ForeignKey)

    def test_model_returns_readable_representation(self):
        """Test a readable string is returned for the model instance."""
        self.assertEqual(str(ItemModelTest.item), ItemModelTest.item.name)

