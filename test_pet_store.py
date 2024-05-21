import requests
import pytest
import json
from utils import log_message


class TestPetStoreAPI:

    def test_get_pet_by_id(self, base_url, headers):
        pet_id = 1
        url = f"{base_url}/pet/{pet_id}"
        response = requests.get(url, headers=headers)

        log_message(f"GET {url} - Status Code: {response.status_code}")

        try:
            response.raise_for_status()
            pet = response.json()
            log_message(f"Pet details: {pet}")
            assert 'id' in pet, "Response JSON should contain 'id'"
            assert pet['id'] == pet_id, f"Expected pet ID {pet_id}, but got {pet['id']}"
        except requests.exceptions.HTTPError as err:
            log_message(f"HTTP error occurred: {err}")
            pytest.fail(f"HTTP error occurred: {err}")
        except Exception as err:
            log_message(f"Other error occurred: {err}")
            pytest.fail(f"Other error occurred: {err}")

    def test_add_new_pet(self, base_url, headers, new_pet):
        url = f"{base_url}/pet"
        response = requests.post(url, json=new_pet, headers=headers)

        log_message(f"POST {url} - Status Code: {response.status_code}")

        try:
            response.raise_for_status()
            created_pet = response.json()
            log_message(f"Created pet details: {created_pet}")
            assert created_pet['id'] == new_pet['id'], "The created pet ID should match the input pet ID"
        except requests.exceptions.HTTPError as err:
            log_message(f"HTTP error occurred: {err}, Response body: {response.text}")
            pytest.fail(f"HTTP error occurred: {err}")
        except Exception as err:
            log_message(f"Other error occurred: {err}")
            pytest.fail(f"Other error occurred: {err}")

