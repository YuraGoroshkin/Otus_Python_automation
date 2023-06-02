import pytest
import requests
from files.breweries_random_schema import schema
from jsonschema import validate
import re

url = "https://api.openbrewerydb.org/"


def test_status_code():
    response = requests.get(url)
    assert response.status_code == 200
    assert response.status_code not in (300, 400, 500)


def test_json_schema():
    path = 'v1/breweries/random'
    response = requests.get(url + path)
    assert response.status_code == 200
    validate(instance=response.json(), schema=schema)


# Note: Default is 1. Max per page is 50.
@pytest.mark.parametrize('num, expected_num', [
    (3, 3),
    (5, 5),
    (10, 10),
    (49, 49),
    (50, 50),
    (51, 50),
    (100, 50)
])
def test_size(num, expected_num):
    path = "v1/breweries/random?size=" + str(num)
    response = requests.get(url + path)
    assert response.status_code == 200
    assert len(response.json()) == expected_num


@pytest.mark.parametrize('name, conclusion',
                         [("Dog", "valid"), ("Fish", "valid"), ("Robot", "valid")])
def test_name_brew(name, conclusion):
    path = "v1/breweries/autocomplete?query=" + name
    response = requests.get(url + path)
    for list in response.json():
        string = list['name']
        result = re.search(name.lower(), string.lower())
        assert response.status_code == 200
        assert result.group() == name.lower()


@pytest.mark.parametrize('name, conclusion',
                         [("Rushka", "Empty")])
def test_name_brew_empty(name, conclusion):
    path = "v1/breweries/autocomplete?query=" + name
    response = requests.get(url + path)
    test_empty = []
    assert response.status_code == 200
    assert response.json() == test_empty


@pytest.mark.parametrize('name, conclusion',
                         [("None", "- None")])
def test_name_brew_none(name, conclusion):
    path = "v1/breweries/autocomplete?query=" + name
    response = requests.get(url + path)
    for list in response.json():
        string = list['name']
        result = re.search(name.lower(), string.lower())
        assert response.status_code == 200
        assert result is None
