from selene import browser, have, be

def test_add_new_student():
    browser.open('https://preview.edvibe.com/Account/Login')
    browser.element('.form-input [name=Email]').type('misha-marinov@mail.ru')
    browser.element('.form-input [name=Password]').type('liveUT00mPE8CB7Z').press_enter()
    browser.wait_until(browser.element('form > button:nth-child(4)').should(be.visible))
    browser.element('form > button:nth-child(4)').click()
    browser.wait_until(have.url_containing('/TeacherAccount/'))

    # Заполение всех полей и добавление ученика
    browser.element('.tab-item:nth-child(2)').click()
    browser.element('.ui-tab-item .button-box').click()
    browser.element('.row:nth-child(1) .container-box-sizing:nth-child(1) .form-control').type('New student')
    browser.element('.row:nth-child(1) .container-box-sizing:nth-child(2) .form-control').type('newstudent@test.iu')
    browser.element('.container-box-sizing:nth-child(3) .ui-select').click()
    browser.element('.container-box-sizing:nth-child(3) .option:nth-child(2)').click()
    browser.element('.container-box-sizing:nth-child(4) .ui-select').click()
    browser.element('.container-box-sizing:nth-child(4) .option:nth-child(15)').click()
    browser.element('.item-button .ui-button-loading-base').click()
    browser.element('.item-button .ui-button-base').click()

    # Проверка, что ученик был добавлен с данным именем и почтой
    browser.element('.box-text .word-more-name').should(have.exact_text('New student'))
    browser.element('.box-text .word-more-email').should(have.exact_text('newstudent@test.iu'))
    browser.element('.col-auto .ui-button-base').click()
    browser.element('.container-box-sizing:nth-child(5) .ui-select .no-select-text').should(have.exact_text('English'))
    browser.element('.container-box-sizing:nth-child(7) .ui-select .no-select-text').should(have.text('(UTC+2)'))
    browser.element('.header.disabled-border .bnt-close').click()

    # Поиск нового ученика
    browser.element('.student-detail .button-back').click()
    browser.element('.ui-search > input').set_value('newstudent@test.iu')
    browser.element('.col .row:nth-child(1) .name-pupil').should(have.exact_text('New student'))
    browser.element('.col .row:nth-child(2) .name-pupil').should(have.exact_text('newstudent@test.iu'))

    # Удаление ученика
    browser.element('.col-auto:nth-child(4) .ui-button-base').click()
    browser.element('.col-auto .ui-button-base').click()
    browser.element('.col .ui-button-base.red').click()
    browser.element('.item-button:nth-child(1) .ui-button-base').click()

    # Проверка, что ученик удален
    browser.element('.ui-search > input').set_value('newstudent@test.iu')
    browser.element('div.ui-stopper').should(be.visible)