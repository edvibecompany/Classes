import os.path
from selene import browser, have, be
from random import randint

def test_add_new_group():
    browser.open('https://preview.edvibe.com/Account/Login')
    browser.element('.form-input [name=Email]').type('misha-marinov@mail.ru')
    browser.element('.form-input [name=Password]').type('liveUT00mPE8CB7Z').press_enter()
    browser.wait_until(browser.element('form > button:nth-child(4)').should(be.visible))
    browser.element('form > button:nth-child(4)').click()
    browser.wait_until(have.url_containing('/TeacherAccount/'))

    # Создание нового класса
    browser.element('.tab-item:nth-child(2)').click()
    browser.element('.tabs-container:nth-child(1) .ui-tab-item:nth-child(2)').click()
    browser.element('.row:nth-child(3) .button-box').click()

    # Загрузка фото
    browser.element('[type=file]').type(
        os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'resources/foto.png')
        )
    )
    browser.element('.button-container:nth-child(2) .ui-button-base').click()
    browser.element('.crop-image-preview .cr-image').should(have.tag('img'))

    #Добавление рандомного значения от 1 до 9 в название группы
    a = randint(1, 9)
    browser.element('.control-input > input').type(a)
    browser.element('.item-button .ui-button-loading-base').click()

    # Проверка, что открылся виртуальный класс группы, и выход из класса
    browser.with_(timeout=15).should(have.url_containing('/lesson?isNewClass=true'))
    #browser.should(have.url_containing('/lesson?isNewClass=true'))
    browser.element('.header-container .header-right-menu-exit').click()
    browser.element('.item-button:nth-child(1) .ui-button-base').click()

    # Добавление ученика в новую группу и проверка, что нужный ученик был добавлен
    browser.element('.classes-list-item:nth-child(1) .col-auto:nth-child(4) .ui-button-base').click()
    browser.element('.classes-list-stopper .ui-button-base').click()
    browser.element('.row:nth-child(3) .row:nth-child(3)').click()
    browser.element('.ui-search > input').type('aboba@aboba.ba')
    browser.element('.box-text.email').should(have.exact_text('aboba@aboba.ba'))
    browser.element('.scroll-content .circle').click()
    browser.element('.body .ui-button-base').click()
    browser.element('#blank-modal .modal-window.show').should(be.visible)
    browser.element('.item-button .ui-button-base').click()
    browser.element('.box-text:nth-child(2) .point-text-end').should(have.exact_text('aboba@aboba.ba'))