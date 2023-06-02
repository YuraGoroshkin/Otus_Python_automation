import pytest
import requests
from files.jsonplaceholder_schema import schema
from jsonschema import validate
from typing import Union
from pydantic import BaseModel

url = "https://jsonplaceholder.typicode.com/"


def test_status_code():
    response = requests.get(url)
    assert response.status_code == 200
    assert response.status_code not in (300, 400, 500)


class ServerResp(BaseModel):
    data: Union[str, int, bool]

    def to_payload(self):
        return {"data": self.data}


@pytest.mark.parametrize('expected_data', [
    ServerResp(data="test"),
    ServerResp(data=123),
    ServerResp(data=False)
])
def test_response_data(expected_data):
    response = requests.post(f'{url}posts', data=expected_data.to_payload())
    assert response.status_code == 201
    data_from_server = ServerResp(**response.json())
    assert expected_data == data_from_server


def test_delete():
    path = "posts/1"
    response = requests.delete(url + path)
    assert response.status_code == 200


@pytest.mark.parametrize('path, tally',
                         [("posts", 100), ("comments", 500), ("albums", 100), ("photos", 5000), ("todos", 200),
                          ("users", 10)])
def test_users(path, tally):
    response = requests.get(url + path)
    assert response.status_code == 200
    assert len(response.json()) == tally


def test_schema():
    path = 'posts/1'
    response = requests.get(url + path)
    assert response.status_code == 200
    validate(instance=response.json(), schema=schema)
