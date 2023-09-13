from selene import browser, have, be

def test_add_new_student_from_requests():
    browser.open('https://preview.edvibe.com/Account/Login')
    browser.element('.form-input [name=Email]').type('misha-marinov@mail.ru')
    browser.element('.form-input [name=Password]').type('liveUT00mPE8CB7Z').press_enter()
    browser.wait_until(browser.element('form > button:nth-child(4)').should(be.visible))
    browser.element('form > button:nth-child(4)').click()
    browser.wait_until(have.url_containing('/TeacherAccount/'))

    # Переход во вкладку Заявки
    browser.element('.tab-item:nth-child(2)').click()
    browser.element('.tabs-container .ui-tab-item:nth-child(3)').click()

    # Нажатие на кнопку Подробнее
    browser.with_(timeout=10).element('.container-box-sizing:nth-child(3) .ui-button-base').click()

    # Изменение имени, выбор языка и часового пояса
    browser.element('.box-label-input:nth-child(2) input').type(' из заявок')
    browser.element('.container-box-sizing:nth-child(6) .ui-select').click()
    browser.element('.container-box-sizing:nth-child(6) .option:nth-child(2)').click()
    browser.element('.container-box-sizing:nth-child(7) .ui-select').click()
    browser.element('.container-box-sizing:nth-child(7) .option:nth-child(16)').click()
    browser.element('.col:nth-child(2) .ui-button-base').click()

    # Проверка, что во втором поп-апе выбранный язык и время отображаются корректно
    browser.element('.container-box-sizing:nth-child(3) .ui-select .no-select-text').should(have.exact_text('English'))
    browser.element('.container-box-sizing:nth-child(4) .ui-select .no-select-text').should(have.text(('(UTC+3)')))
    browser.element('.item-button .ui-button-loading-base').click()

    # Переход во вкладку с учениками и проверка, что ученик из заявок был добавлен
    browser.with_(timeout=10).element('.tabs-container .ui-tab-item:nth-child(1)').click()
    browser.element('.pupil-list-item:nth-child(1) .col .row:nth-child(1) .name-pupil').should(have.text('из заявок'))