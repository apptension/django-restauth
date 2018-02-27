import pytest
from rest_framework.test import APIClient
import pytest_factoryboy

from . import factories


@pytest.fixture
def api_client():
    return APIClient()

pytest_factoryboy.register(factories.UserFactory)