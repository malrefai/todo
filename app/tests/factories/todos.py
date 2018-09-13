from factory import DjangoModelFactory, Faker

from app.models import Todo


class TodoFactory(DjangoModelFactory):
    """
    Defines todo factory
    """

    class Meta:
        model = Todo

    title = Faker('sentence', nb_words=2)
    owner = Faker('sentence', nb_words=1)