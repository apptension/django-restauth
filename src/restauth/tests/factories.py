import factory
from django.contrib.auth.hashers import make_password

from .. import models


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.User
        django_get_or_create = ('email',)

    email = factory.Faker('email')
    is_superuser = False

    @classmethod
    def _create(cls, model_class, **kwargs):
        raw_password = kwargs.pop('password', 'secret')
        user = super(UserFactory, cls)._create(model_class,
                                               password=make_password(raw_password),
                                               **kwargs)
        user._password = raw_password
        return user


class UserProfileFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.UserProfile

    user = factory.SubFactory(UserFactory)
    first_name = factory.Faker('name', locale='pl')
