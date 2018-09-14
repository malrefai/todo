from factory import DjangoModelFactory, Faker, SubFactory

from app.models import Item
from app.tests.factories.todos import TodoFactory


class ItemFactory(DjangoModelFactory):
    """
    Defines item factory
    """

    class Meta:
        model = Item

    name = Faker('sentence', nb_words=3)
    done = Faker('boolean')
    todo = SubFactory(TodoFactory)
