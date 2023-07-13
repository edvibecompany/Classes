from selene import browser, have, be, query


def test_delete_last_student():
    browser.open('https://preview.edvibe.com/Account/Login')
    browser.element('.form-input [name=Email]').type('misha-marinov@mail.ru')
    browser.element('.form-input [name=Password]').type('liveUT00mPE8CB7Z').press_enter()
    browser.wait_until(browser.element('form > button:nth-child(4)').should(be.visible))
    browser.element('form > button:nth-child(4)').click()
    browser.wait_until(have.url_containing('/TeacherAccount/'))

    # Переход во вкладку с учениками
    browser.element('.tab-item:nth-child(2)').click()
    browser.element('.pupil-list-item:nth-child(1) .col-auto:nth-child(4) .ui-button-base').click()
    email = browser.element('.box-text .word-more-email').get(query.text)
    browser.element('.col-auto .ui-button-base').click()
    browser.element('.col .ui-button-base.red').click()
    browser.element('.item-button:nth-child(1) .ui-button-base').click()

    # Проверка, что ученик удален
    browser.should(have.url_containing('/learning/pupils'))
    browser.element('.ui-search > input').set_value(email)
    browser.element('div.ui-stopper').should(be.visible)