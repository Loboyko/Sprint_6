import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()