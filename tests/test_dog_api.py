import pytest
import requests
from files.schema_dog_list_all import schema
from jsonschema import validate

url = "https://dog.ceo/"


@pytest.mark.parametrize('status', [200, 300, 400, 500])
def test_status_code(status):
    path = 'dog-api/'
    response = requests.get(url + path)
    assert response.status_code == 200
    assert response.status_code not in (300, 400, 500)


def test_json_schema():
    path = 'api/breeds/list/all'
    response = requests.get(url + path)
    assert response.status_code == 200
    validate(instance=response.json(), schema=schema)


def test_header_json():
    path = 'api/breeds/list/all'
    response = requests.get(url + path)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"


# запрос не может вернуть более 50 объектов по документации
@pytest.mark.parametrize('num, expected_num', [
    (3, 3),
    (5, 5),
    (10, 10),
    (49, 49),
    (50, 50),
    (51, 50),
    (100, 50)
])
def test_num_fotos(num, expected_num):
    response = requests.get(f'{url}api/breeds/image/random/{num}')
    assert response.status_code == 200
    assert len(response.json()["message"]) == expected_num


def test_jpg_foto():
    path = "api/breeds/image/random/"
    response = requests.get(url + path)
    assert response.status_code == 200
    assert str(response.json()["message"]).find(".jpg") != -1
