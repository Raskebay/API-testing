import pytest
import requests

from configurations import SERVICE_URL


@pytest.fixture
def get_posts():
    response = requests.get(SERVICE_URL)
    return response
