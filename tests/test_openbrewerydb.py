import pytest
import requests
from files.breweries_random_schema import schema
from jsonschema import validate

url = "https://api.openbrewerydb.org/"


# @pytest.mark.parametrize('status', [200, 300, 400, 500])
# def test_status_code(status):
#     response = requests.get(url)
#     if status == 200:
#         assert response.status_code == 200
#     else:
#         assert response.status_code != status


# def test_json_schema():
#     path = 'v1/breweries/random'
#     response = requests.get(url + path)
#     validate(instance=response.json(), schema=schema)

# Note: Default is 1. Max per page is 50.
# @pytest.mark.parametrize('num, conclusion',
#                          [(3, "valid"), (49, "valid"), (50, "valid"), (51, "no_valid"), (100, "no_valid")])
# def test_size(num, conclusion):
#     path = "v1/breweries/random?size=" + str(num)
#     response = requests.get(url + path)
#     if num > len(response.json()):
#         assert len(response.json()) != num
#     else:
#         assert len(response.json()) == num

@pytest.mark.parametrize('name', ["Dog", "Robot", "Fish"])
def test_name_brew(name):
    path = "v1/breweries/autocomplete?query=" + name
    response = requests.get(url + path)
    t = response.json()
    print(response.json())