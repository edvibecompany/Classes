from selene import browser, have, be, query
from random import randint
import os.path

def test_new_individual_class():
    browser.open('https://preview.edvibe.com/Account/Login')
    browser.element('.form-input [name=Email]').type('misha-marinov@mail.ru')
    browser.element('.form-input [name=Password]').type('liveUT00mPE8CB7Z').press_enter()
    browser.wait_until(browser.element('form > button:nth-child(4)').should(be.visible))
    browser.element('form > button:nth-child(4)').click()
    browser.wait_until(have.url_containing('/TeacherAccount/'))

    # Поиск ученика и переход к нему в профиль
    browser.element('.tab-item:nth-child(2)').click()
    browser.element('.ui-search > input').set_value('vurtagalto@gufum.com')
    browser.element('.box-text:nth-child(2) .name-pupil').should(have.exact_text('vurtagalto@gufum.com'))
    browser.element('.col-auto:nth-child(4) .ui-button-base').click()

    # Добавление класса ученику
    browser.element('.ui-tab-item.isDisabled').click()

    browser.element('[type=file]').type(
        os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'resources/foto2.jpg')
        )
    )
    browser.element('.button-container:nth-child(2) .ui-button-base').click()
    browser.element('.crop-image-preview .cr-image').should(have.tag('img'))

    a = randint(1, 9)
    browser.element('[type=text].form-control').type(" ").type(a)

    browser.element('.body .ui-button-loading-base').click()
    browser.with_(timeout=15).should(have.url_containing('/lesson?isNewClass=true'))