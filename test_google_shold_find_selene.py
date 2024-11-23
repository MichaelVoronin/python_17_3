import pytest
from selene import browser, be, have


@pytest.fixture
def size_browser():
    browser.config.window_width = 1024
    browser.config.window_height = 768

def test_positive(size_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_negative(size_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('1223ненайдёшь%^#dfg').press_enter()
    browser.element('[id="search"]').should(have.text('опоимн!!&798hjf'))
