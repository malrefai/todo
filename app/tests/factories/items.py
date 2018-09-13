from factory import DjangoModelFactory, Faker

from app.models import Item


class ItemFactory(DjangoModelFactory):
    """
    Defines item factory
    """

    class Meta:
        model = Item

    name = Faker('sentence', nb_words=3)
    done = Faker('boolean')
