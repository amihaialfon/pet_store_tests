import pytest
from utils import setup_logging
from config import Config

@pytest.fixture(scope="module", autouse=True)
def setup_logging_fixture():
    setup_logging()

@pytest.fixture(scope="module")
def base_url():
    return Config.BASE_URL

@pytest.fixture(scope="module")
def headers():
    return Config.HEADERS

@pytest.fixture(scope="module")
def new_pet():
    return Config.NEW_PET
