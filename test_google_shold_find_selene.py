from selene import browser, be, have


def test_positive(size_browser):
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene'))
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative(size_browser):
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('опволпаг213743124khfgbn').press_enter()
    browser.element('#center_col').should(have.text('did not match any documents'))
