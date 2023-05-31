import pytest
import requests
from files.jsonplaceholder_schema import schema
from jsonschema import validate

url = "https://jsonplaceholder.typicode.com/"


@pytest.mark.parametrize('status', [200, 300, 400, 500])
def test_status_code(status):
    response = requests.get(url)
    if status == 200:
        assert response.status_code == 200
    else:
        assert response.status_code != status

# не понимаю как можно передать и получить булевое значение, цифру вместо строчки
@pytest.mark.parametrize('data', [({"test": "test"}), ({"num": "1"}), ({"bool": "bool(False)"})])
def test_response_data(data):
    path = 'posts'
    response = requests.post(url + path, data=data)
    dict = response.json()
    dict.pop('id', None)
    assert data == dict


def test_delete():
    path = "posts/1"
    response = requests.delete(url + path)
    assert response.status_code == 200


@pytest.mark.parametrize('path, tally', [("posts", 100), ("comments", 500), ("albums", 100), ("photos", 5000), ("todos", 200), ("users", 10)])
def test_users(path, tally):
    response = requests.get(url + path)
    assert len(response.json()) == tally

def test_schema():
    path = 'posts/1'
    response = requests.get(url + path)
    validate(instance=response.json(), schema=schema)
