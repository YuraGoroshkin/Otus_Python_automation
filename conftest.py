import pytest


@pytest.fixture()
def param_fixture(request):
    url = request.config.getoption("--url")
    status_code = int(request.config.getoption("--status_code"))
    return url, status_code


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://ya.ru/")
    parser.addoption("--status_code", action="store", default="200")
