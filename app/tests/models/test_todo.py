from django.test import TestCase
from django.db import models

from app.tests.factories.todos import TodoFactory


class TodoModelTest(TestCase):
    """
    This class defines the test suite for the todo model.
    """

    todo = None

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        TodoModelTest.todo = TodoFactory.build()

    def test_title_field(self):
        field = TodoModelTest.todo._meta.get_field("title")
        self.assertIsInstance(field, models.CharField)
        self.assertEqual(field.max_length, 100)
        self.assertFalse(field.blank)

    def test_owner_field(self):
        field = TodoModelTest.todo._meta.get_field("owner")
        self.assertIsInstance(field, models.CharField)
        self.assertEqual(field.max_length, 100)
        self.assertTrue(field.blank)
        self.assertTrue(field.null)

    def test_created_field(self):
        field = TodoModelTest.todo._meta.get_field("created")
        self.assertIsInstance(field, models.DateTimeField)
        self.assertTrue(field.auto_now_add)

    def test_modified_field(self):
        field = TodoModelTest.todo._meta.get_field("modified")
        self.assertIsInstance(field, models.DateTimeField)
        self.assertTrue(field.auto_now)

    def test_model_returns_readable_representation(self):
        """Test a readable string is returned for the model instance."""
        self.assertEqual(str(TodoModelTest.todo), TodoModelTest.todo.title)
