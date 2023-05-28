import pytest
import requests
from files.schema_dog_list_all import schema
from jsonschema import validate

url = "https://dog.ceo/"


@pytest.mark.parametrize('status', [200, 300, 400, 500])
def test_status_code(status):
    path = 'dog-api/'
    response = requests.get(url + path)
    if status == 200:
        assert response.status_code == 200
    else:
        assert response.status_code != status


def test_json_schema():
    path = 'api/breeds/list/all'
    response = requests.get(url + path)
    validate(instance=response.json(), schema=schema)


def test_header_json():
    path = 'api/breeds/list/all'
    response = requests.get(url + path)
    assert response.headers["Content-Type"] == "application/json"


# запрос не может вернуть более 50 объектов по документации
@pytest.mark.parametrize('num', [3, 5, 10, 49, 50, 51, 100])
def test_num_fotos(num):
    path = "api/breeds/image/random/" + str(num)
    response = requests.get(url + path)
    if num > len(response.json()["message"]):
        assert len(response.json()["message"]) != num
    else:
        assert len(response.json()["message"]) == num


def test_jpg_foto():
    path = "api/breeds/image/random/"
    response = requests.get(url + path)
    assert str(response.json()["message"]).find(".jpg") != -1
