import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup():
    s = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    return driver
