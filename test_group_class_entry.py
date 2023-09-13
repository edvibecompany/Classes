from selene import browser, have, be

def test_entrance_to_group_class():
    browser.open('https://preview.edvibe.com/Account/Login')
    browser.element('.form-input [name=Email]').type('misha-marinov@mail.ru')
    browser.element('.form-input [name=Password]').type('liveUT00mPE8CB7Z').press_enter()
    browser.wait_until(browser.element('form > button:nth-child(4)').should(be.visible))
    browser.element('form > button:nth-child(4)').click()
    browser.wait_until(have.url_containing('/TeacherAccount/'))

    # Переход во вкладку с группами
    browser.element('.tab-item:nth-child(2)').click()
    browser.element('.ui-tab-item:nth-child(2) .hover').click()

    # Поиск группы и вход в виртуальный класс
    browser.element('.ui-search > input').type('Cat').press_enter()
    if browser.element('.box-text .name-class ').should(have.exact_text('Cat')):
        browser.element('.mr-5 .ui-button-base').click()
    browser.should(have.url_containing('/class/429076/lesson/section/14576566'))

    # Выход из класса и проверка, что вышли во вкладку с группами
    browser.element('.header-container .header-right-menu-exit').click()
    browser.element('.item-button:nth-child(1) .ui-button-base').click()
    browser.should(have.url_containing('/learning/groups'))