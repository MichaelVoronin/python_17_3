import pytest
from selenium import webdriver
from selene import browser


@pytest.fixture
def size_browser():
    browser.config.window_width = 1024
    browser.config.window_height = 768
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.open('https://google.com')
    browser.config.timeout = 20


    yield

    browser.quit()
