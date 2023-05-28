import re

import pytest
import requests
from files.schema_dog_list_all import schema
from jsonschema import validate
import random

url = "https://dog.ceo/"


def test_status_code():
    path = 'dog-api/'
    response = requests.get(url + path)
    assert response.status_code == 200


def test_json_schema():
    path = 'api/breeds/list/all'
    response = requests.get(url + path)
    validate(instance=response.json(), schema=schema)


def test_header_json():
    path = 'api/breeds/list/all'
    response = requests.get(url + path)
    assert response.headers["Content-Type"] == "application/json"


def test_num_fotos():
    num = random.randint(0, 30)
    path = "api/breeds/image/random/" + str(num)
    response = requests.get(url + path)
    assert len(response.json()["message"]) == num


def test_jpg_foto():
    path = "api/breeds/image/random/"
    response = requests.get(url + path)
    assert str(response.json()["message"]).find(".jpg") != -1
