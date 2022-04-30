import pytest

def pytest_addoption(parser):
    parser.addoption("--network", action="store", help="Network to test")

@pytest.fixture
def get_network(request):
  _network = request.config.getoption("--network")
  return _network    