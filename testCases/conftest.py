import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utilities.readProperties import readConf


@pytest.fixture(params=["chrome"], scope="function")
def setup_method(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(readConf.get_url())
        driver.implicitly_wait(10)
    elif request.param == 'firefox':
        driver = webdriver.Firefox(GeckoDriverManager().install())
        driver.maximize_window()
        driver.get(readConf.get_url())
        driver.implicitly_wait(10)
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(readConf.get_url())
        driver.implicitly_wait(10)
    return driver


### HTML Report ###

def pytest_configure(config):
    config._metadata['Project Name'] = 'VISMA - Technical Test'
    config._metadata['Portal Under Test'] = 'My Store'
    config._metadata['Portal Link'] = 'http://automationpractice.com/'
    config._metadata['Tester Name'] = 'Anshul Gupta'
