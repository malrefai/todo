from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.utils.json import dumps

from factory import Faker
from random import randint

from app.tests.factories.todos import TodoFactory
from app.tests.support.assertions import asert_valid_schema
from app.models.todo import Todo


class TestSetUP(TestCase):
    """
    This class defines the setup for todo test suite.
    """

    def initList(self):
        self._todos = TodoFactory.create_batch(randint(1, 5))

    def initDetailDestroy(self):
        self.initList()
        self._todo_id = self.todos[0].id

    def initCreateUpdate(self):
        self.initDetailDestroy()
        todo = TodoFactory.build()
        self._title = todo.title
        self._owner = todo.owner

    @property
    def todos(self):
        return self._todos

    @property
    def old_todos_count(self):
        return len(self._todos)

    @property
    def todo_id(self):
        return self._todo_id

    @todo_id.setter
    def todo_id(self, value):
        self._todo_id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value


class TodoDetailViewTest(TestSetUP):
    """
    This class defines the test suite for the todo detail view.
    """

    @property
    def params(self):
        return {"pk": self.todo_id}

    def setUp(self):
        self.initDetailDestroy()

    # Valid request
    # def test_content_type(self):
    #     response = self.client.get(
    #         reverse("todo-detail", kwargs=self.params),
    #         content_type="application/json")
    #     self.assertEqual(response.content_type, "application/json")

    def test_response_status(self):
        response = self.client.get(
            reverse("todo-detail", kwargs=self.params),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_schema_match(self):
        response = self.client.get(
            reverse("todo-detail", kwargs=self.params),
            content_type="application/json"
        )
        asert_valid_schema(response.data, "todos_api/detail.json")

    # Invalid request
    # def test_invalid_todo_parameter_content_type(self):
    #     self.todo_id = "invalid_todo_id"
    #     response = self.client.get(
    #         reverse("todo-detail", kwargs=self.params),
    #         content_type="application/json"
    #     )
    #     self.assertEqual(response.content_type, "application/json")

    def test_invalid_todo_parameter_status(self):
        self.todo_id = "invalid_todo_id"
        response = self.client.get(
            reverse("todo-detail", kwargs=self.params),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_error_schema_match(self):
        self.todo_id = "invalid_todo_id"
        response = self.client.get(
            reverse("todo-detail", kwargs=self.params),
            content_type="application/json"
        )
        asert_valid_schema(response.data, "errors/detail.json")

    def test_error_message(self):
        self.todo_id = "invalid_todo_id"
        response = self.client.get(
            reverse("todo-detail", kwargs=self.params),
            content_type="application/json"
        )
        self.assertEqual(response.data["detail"], NotFound.default_detail)


class TodoListViewTest(TestSetUP):
    """
    This class defines the test suite for the todo list view.
    """

    def setUp(self):
        self.initList()

    # Valid request
    # def test_content_type(self):
    #     response = self.client.get(
    #         reverse("todo-list"),
    #         content_type="application/json"
    #     )
    #     self.assertEqual(response.content_type, "application/json")

    def test_response_status(self):
        response = self.client.get(
            reverse("todo-list"),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_schema_match(self):
        response = self.client.get(
            reverse("todo-list"),
            content_type="application/json"
        )
        asert_valid_schema(response.data, "todos_api/list.json")

    def test_return_all_todo(self):
        response = self.client.get(
            reverse("todo-list"),
            content_type="application/json"
        )
        self.assertEqual(len(response.data), self.old_todos_count)

    # Invalid request


class TodoCreateViewTest(TestSetUP):
    """
    This class defines the test suite for the todo create view.
    """

    @property
    def data(self):
        return {"title": self.title, "owner": self.owner}

    def setUp(self):
        self.initCreateUpdate()

    # Valid request
    # def test_content_type(self):
    #     response = self.client.post(
    #         reverse("todo-list"),
    #         content_type="application/json"
    #     )
    #     self.assertEqual(response.content_type, "application/json")

    def test_response_status(self):
        response = self.client.post(
            reverse("todo-list"),
            data=dumps(self.data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_schema_match(self):
        response = self.client.post(
            reverse("todo-list"),
            data=dumps(self.data),
            content_type="application/json"
        )
        asert_valid_schema(response.data, "todos_api/create.json")

    def test_create_object_in_database(self):
        self.client.post(
            reverse("todo-list"),
            data=dumps(self.data),
            content_type="application/json"
        )
        self.assertEqual(len(Todo.objects.all()), self.old_todos_count + 1)

    # Invalid request
    # def test_invalid_todo_parameter_content_type(self):
    #     self.title = None
    #     response = self.client.post(
    #         reverse("todo-list"),
    #         data=dumps(self.data),
    #         content_type="application/json"
    #     )
    #     self.assertEqual(response.content_type, "application/json")

    def test_invalid_title_parameter_status(self):
        self.title = None
        response = self.client.post(
            reverse("todo-list"),
            data=dumps(self.data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TodoUpdateViewTest(TestSetUP):
    """
    This class defines the test suite for the todo create view.
    """

    @property
    def params(self):
        return {"pk": self.todo_id}

    @property
    def data(self):
        return {"title": self.title, "owner": self.owner}

    def setUp(self):
        self.initCreateUpdate()

    # Valid request
    # def test_content_type(self):
    #     response = self.client.post(
    #         reverse("todo-detail", kwargs=self.params),
    #         content_type="application/json"
    #     )
    #     self.assertEqual(response.content_type, "application/json")

    def test_invalid_todo_parameter_status(self):
        self.todo_id = "invalid_todo_id"
        response = self.client.put(
            reverse("todo-detail", kwargs=self.params),
            data=dumps(self.data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_error_schema_match(self):
        self.todo_id = "invalid_todo_id"
        response = self.client.put(
            reverse("todo-detail", kwargs=self.params),
            data=dumps(self.data),
            content_type="application/json"
        )
        asert_valid_schema(response.data, "errors/detail.json")

    def test_error_message(self):
        self.todo_id = "invalid_todo_id"
        response = self.client.put(
            reverse("todo-detail", kwargs=self.params),
            data=dumps(self.data),
            content_type="application/json"
        )
        self.assertEqual(response.data["detail"], NotFound.default_detail)

    def test_response_status(self):
        response = self.client.put(
            reverse("todo-detail", kwargs=self.params),
            data=dumps(self.data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_schema_match(self):
        response = self.client.put(
            reverse("todo-detail", kwargs=self.params),
            data=dumps(self.data),
            content_type="application/json"
        )
        asert_valid_schema(response.data, "todos_api/update.json")

    # Invalid request
    # def test_invalid_todo_parameter_content_type(self):
    #     self.title = None
    #     response = self.client.put(
    #         reverse("todo-detail", kwargs=self.params),
    #         data=dumps(self.data),
    #         content_type="application/json"
    #     )
    #     self.assertEqual(response.content_type, "application/json")

    def test_invalid_title_parameter_status(self):
        self.title = None
        response = self.client.put(
            reverse("todo-detail", kwargs=self.params),
            data=dumps(self.data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TodoDestroyViewTest(TestSetUP):
    """
    This class defines the test suite for the todo destroy view.
    """

    @property
    def params(self):
        return {"pk": self.todo_id}

    def setUp(self):
        self.initDetailDestroy()

    # Valid request
    # def test_content_type(self):
    #     response = self.client.delete(
    #         reverse("todo-detail", kwargs=self.params),
    #         content_type="application/json"
    #     )
    #     self.assertEqual(response.content_type, "application/json")

    def test_response_status(self):
        response = self.client.delete(
            reverse("todo-detail", kwargs=self.params),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_object_in_database(self):
        self.client.delete(
            reverse("todo-detail", kwargs=self.params),
            content_type="application/json"
        )
        self.assertEqual(len(Todo.objects.all()), self.old_todos_count - 1)

    # Invalid request
    # def test_invalid_todo_parameter_content_type(self):
    #     self.title = None
    #     response = self.client.put(
    #         reverse("todo-detail", kwargs=self.params),
    #         data=dumps(self.data),
    #         content_type="application/json"
    #     )
    #     self.assertEqual(response.content_type, "application/json")

    def test_invalid_todo_parameter_status(self):
        self.todo_id = "invalid_todo_id"
        response = self.client.delete(
            reverse("todo-detail", kwargs=self.params),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_error_schema_match(self):
        self.todo_id = "invalid_todo_id"
        response = self.client.delete(
            reverse("todo-detail", kwargs=self.params),
            content_type="application/json"
        )
        asert_valid_schema(response.data, "errors/detail.json")

    def test_error_message(self):
        self.todo_id = "invalid_todo_id"
        response = self.client.delete(
            reverse("todo-detail", kwargs=self.params),
            content_type="application/json"
        )
        self.assertEqual(response.data["detail"], NotFound.default_detail)
