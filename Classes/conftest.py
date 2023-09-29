import pytest
from selene import browser, be


@pytest.fixture()
def login():
    browser.open('https://stage.progressme.ru/login')
    browser.element('[type=text]').type('misha-marinov@mail.ru')
    browser.element('[type=password]').type('testGYvbueca0lf6')
    browser.element('.blue').click()
    browser.element('button:nth-child(1)').click()
    browser.wait_until(browser.element('.edvibe3-shedule').should(be.visible))
