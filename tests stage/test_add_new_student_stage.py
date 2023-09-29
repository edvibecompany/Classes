from selene import browser, have, be, query
from random import randint


def test_add_new_student(login):
    # Переход во вкладку обучение и нажатие на кнопку Добавить нового ученика
    browser.element('.sidebar_section_list .iconedv-School').click()
    browser.element('section > .f > button').click()

    # Заполение полей Имя, Почта, Телефон
    a = str(randint(1, 100))
    browser.element('.tir-label:nth-child(1) input').type('Student' + ' ' + a)
    browser.element('.tir-label:nth-child(2) input').type('newstudent' + a + '@test.iu')
    browser.element('.tir-label:nth-child(3) input').type('89008007060')

    # Выбор языка и часового пояса
    browser.element('.tir-label:nth-child(4) .tir-dropdown').click()
    browser.element('.tir-option:nth-child(2)').click()
    browser.element('.tir-label:nth-child(5) .tir-dropdown').click()
    browser.element('.tir-option:nth-child(16)').click()

    # Нажатие на кнопку Создать
    browser.element('.tir-button-wrapper .blue').click()

    # Проверка, что почта корректная в окне с данными для входа
    browser.element('.tir-label:nth-child(2) .field').should(have.text('newstudent'))
    email1 = browser.element('.tir-label:nth-child(2) .field').get(query.text)
    browser.element('.footer .blue').click()

    # Проверка, что новый ученик отображается первым в списке и есть тег new
    browser.element('.student-li:nth-child(1) .fw-medium').should(have.text('Student'))
    email2 = browser.element('.student-li:nth-child(1) .fs-small_p span').get(query.text)
    assert email1 == email2
    browser.element('.student-li:nth-child(1) .student-li-new-status').should(be.visible)

    # Поиск нового ученика
    browser.element('.search-input input').type(email1)
    assert email1 == email2
