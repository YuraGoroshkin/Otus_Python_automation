import pytest
import requests
from files.breweries_random_schema import schema
from jsonschema import validate
import re

url = "https://api.openbrewerydb.org/"


@pytest.mark.parametrize('status', [200, 300, 400, 500])
def test_status_code(status):
    response = requests.get(url)
    if status == 200:
        assert response.status_code == 200
    else:
        assert response.status_code != status


def test_json_schema():
    path = 'v1/breweries/random'
    response = requests.get(url + path)
    validate(instance=response.json(), schema=schema)


# Note: Default is 1. Max per page is 50.
@pytest.mark.parametrize('num, conclusion',
                         [(3, "valid"), (49, "valid"), (50, "valid"), (51, "no_valid"), (100, "no_valid")])
def test_size(num, conclusion):
    path = "v1/breweries/random?size=" + str(num)
    response = requests.get(url + path)
    if num > len(response.json()):
        assert len(response.json()) != num
    else:
        assert len(response.json()) == num


# Возможно лучше разделить этот тест на 3 (минимум) разных
@pytest.mark.parametrize('name, conclusion',
                         [("Dog", "valid"), ("Fish", "valid"), ("Robot", "valid"), ("Rushka", "Empty"),
                          ("None", "- None")])
def test_name_brew(name, conclusion):
    path = "v1/breweries/autocomplete?query=" + name
    response = requests.get(url + path)
    for list in response.json():
        test_empty = []
        string = list['name']
        result = re.search(name.lower(), string.lower())
        if result is None:
            assert result is None
        if len(response.json()) == 0:
            assert response.json() == test_empty
        if result is not None:
            if result.group() == name.lower():
                assert result.group() == name.lower()
