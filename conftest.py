import pytest


@pytest.fixture(scope="class",autouse=True)
def setup(browser):
    if browser == "chrome":
        print("launch Chrome")
    elif browser == "firefox":
        print("launch firefox")
    else:
        print("enter a valid browser")
    yield
    print("logoff")
    print("close browser")
def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture(scope="class",autouse=True)
def browser(request):
    return request.config.getoption("--browser")
