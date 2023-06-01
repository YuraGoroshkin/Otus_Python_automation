import requests


# можно ли как-то ввиде параметров передать url и status?
def test_status_code(param_fixture):
    response = requests.get(param_fixture[0])
    assert response.status_code == param_fixture[1]
