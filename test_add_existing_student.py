from selene import browser, have, be

def test_student_already_exist():
    browser.open('https://preview.edvibe.com/Account/Login')
    browser.element('.form-input [name=Email]').type('misha-marinov@mail.ru')
    browser.element('.form-input [name=Password]').type('liveUT00mPE8CB7Z').press_enter()
    browser.wait_until(browser.element('form > button:nth-child(4)').should(be.visible))
    browser.element('form > button:nth-child(4)').click()
    browser.wait_until(have.url_containing('/TeacherAccount/'))

    # Заполение полей Имя, Почта и добавление ученика, проверка, что появилась ошибка
    browser.element('.tab-item:nth-child(2)').click()
    browser.element('.ui-tab-item .button-box').click()
    browser.element('.row:nth-child(1) .container-box-sizing:nth-child(1) .form-control').type('New student')
    browser.element('.row:nth-child(1) .container-box-sizing:nth-child(2) .form-control').type('vurtagalto@gufum.com')
    browser.element('.item-button .ui-button-loading-base').click()
    browser.element('.row .ui-error').should(be.visible)