import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(autouse=True)
def set_up_browser(request, browser, url):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == 'edge':
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption('--browser')
    parser.addoption('--url')


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption('--browser')


@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption('--url')

