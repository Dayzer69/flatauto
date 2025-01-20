# pytest Tests\test_registration_page.py

from Pages.mainPage import mainPageLocators, mainPageHelper
from Pages.registrationPage import registrationPageLocators, registrationPageHelper
from Pages.loginPage import loginPageLocators, loginPageHelper
from time import sleep


def test_successful_registration(browser):
    """Успешная регистрация"""
    main_page = mainPageHelper(browser, mainPageLocators.url)
    main_page.open()
    main_page.go_to_registration()
    registration_page = registrationPageHelper(browser, None)
    email = registration_page.random_email()
    registration_page.fill_field(registrationPageLocators.email, email)
    registration_page.fill_field(registrationPageLocators.surname, 'ТестФам')
    registration_page.fill_field(registrationPageLocators.name, 'ТестИм')
    registration_page.fill_field(registrationPageLocators.patronymic, 'ТестОтч')
    registration_page.fill_dob(registrationPageLocators.dob, '29101995')
    registration_page.fill_field(registrationPageLocators.password1, '00000000')
    registration_page.fill_field(registrationPageLocators.password_confirm, '00000000')
    registration_page.click(registrationPageLocators.registration_btn)

    registration_page.assert_text(registrationPageLocators.verification_page_elements, 'Подтверждение адреса E-mail')


def test_email_isrequired(browser):
    """Поле Email обязательное"""
    main_page = mainPageHelper(browser, mainPageLocators.url)
    main_page.open()
    main_page.go_to_registration()
    registration_page = registrationPageHelper(browser, None)
    registration_page.fill_field(registrationPageLocators.surname, 'ТестФам')
    registration_page.fill_field(registrationPageLocators.name, 'ТестИм')
    registration_page.fill_field(registrationPageLocators.patronymic, 'ТестОтч')
    registration_page.fill_dob(registrationPageLocators.dob, '29101995')
    registration_page.fill_field(registrationPageLocators.password1, '00000000')
    registration_page.fill_field(registrationPageLocators.password_confirm, '00000000')
    registration_page.click(registrationPageLocators.registration_btn)

    registration_page.assert_text(registrationPageLocators.email_validation, 'Обязательное поле!')


def test_surname_isrequired(browser):
    """Поле Фамилия обязательное"""
    main_page = mainPageHelper(browser, mainPageLocators.url)
    main_page.open()
    main_page.go_to_registration()
    registration_page = registrationPageHelper(browser, None)
    email = registration_page.random_email()
    registration_page.fill_field(registrationPageLocators.email, email)
    registration_page.fill_field(registrationPageLocators.name, 'ТестИм')
    registration_page.fill_field(registrationPageLocators.patronymic, 'ТестОтч')
    registration_page.fill_dob(registrationPageLocators.dob, '29101995')
    registration_page.fill_field(registrationPageLocators.password1, '00000000')
    registration_page.fill_field(registrationPageLocators.password_confirm, '00000000')
    registration_page.click(registrationPageLocators.registration_btn)

    registration_page.assert_text(registrationPageLocators.surname_validation, 'Обязательное поле!')


def test_name_isrequired(browser):
    """Поле Имя обязательное"""
    main_page = mainPageHelper(browser, mainPageLocators.url)
    main_page.open()
    main_page.go_to_registration()
    registration_page = registrationPageHelper(browser, None)
    email = registration_page.random_email()
    registration_page.fill_field(registrationPageLocators.email, email)
    registration_page.fill_field(registrationPageLocators.surname, 'ТестФам')
    registration_page.fill_field(registrationPageLocators.patronymic, 'ТестОтч')
    registration_page.fill_dob(registrationPageLocators.dob, '29101995')
    registration_page.fill_field(registrationPageLocators.password1, '00000000')
    registration_page.fill_field(registrationPageLocators.password_confirm, '00000000')
    registration_page.click(registrationPageLocators.registration_btn)

    registration_page.assert_text(registrationPageLocators.name_validation, 'Обязательное поле!')


def test_dob_isrequired(browser):
    """Поле даты рождения обязательное"""
    main_page = mainPageHelper(browser, mainPageLocators.url)
    main_page.open()
    main_page.go_to_registration()
    registration_page = registrationPageHelper(browser, None)
    email = registration_page.random_email()
    registration_page.fill_field(registrationPageLocators.email, email)
    registration_page.fill_field(registrationPageLocators.surname, 'ТестФам')
    registration_page.fill_field(registrationPageLocators.patronymic, 'ТестОтч')
    registration_page.fill_field(registrationPageLocators.password1, '00000000')
    registration_page.fill_field(registrationPageLocators.password_confirm, '00000000')
    registration_page.click(registrationPageLocators.registration_btn)

    registration_page.assert_text(registrationPageLocators.dob_validation, 'Обязательное поле!')


def test_password_isrequired(browser):
    """Поле Пароль обязательное"""
    main_page = mainPageHelper(browser, mainPageLocators.url)
    main_page.open()
    main_page.go_to_registration()
    registration_page = registrationPageHelper(browser, None)
    email = registration_page.random_email()
    registration_page.fill_field(registrationPageLocators.email, email)
    registration_page.fill_field(registrationPageLocators.surname, 'ТестФам')
    registration_page.fill_field(registrationPageLocators.name, 'ТестИм')
    registration_page.fill_field(registrationPageLocators.patronymic, 'ТестОтч')
    registration_page.fill_dob(registrationPageLocators.dob, '29101995')
    registration_page.fill_field(registrationPageLocators.password_confirm, '00000000')
    registration_page.click(registrationPageLocators.registration_btn)

    registration_page.assert_text(registrationPageLocators.password_validation, 'Обязательное поле!')


def test_password_confirm_isrequired(browser):
    """Поле Подтверждение пароля обязательное"""
    main_page = mainPageHelper(browser, mainPageLocators.url)
    main_page.open()
    main_page.go_to_registration()
    registration_page = registrationPageHelper(browser, None)
    email = registration_page.random_email()
    registration_page.fill_field(registrationPageLocators.email, email)
    registration_page.fill_field(registrationPageLocators.surname, 'ТестФам')
    registration_page.fill_field(registrationPageLocators.name, 'ТестИм')
    registration_page.fill_field(registrationPageLocators.patronymic, 'ТестОтч')
    registration_page.fill_dob(registrationPageLocators.dob, '29101995')
    registration_page.fill_field(registrationPageLocators.password1, '00000000')
    registration_page.click(registrationPageLocators.registration_btn)

    registration_page.assert_text(registrationPageLocators.password_confirm_validation, 'Обязательное поле!')


def test_email_isincorrect(browser):
    """Поле Email не соответствует валидации"""
    main_page = mainPageHelper(browser, mainPageLocators.url)
    main_page.open()
    main_page.go_to_registration()
    registration_page = registrationPageHelper(browser, None)
    registration_page.fill_field(registrationPageLocators.email, 'Здарова, бандиты')
    registration_page.fill_field(registrationPageLocators.surname, 'ТестФам')
    registration_page.fill_field(registrationPageLocators.name, 'ТестИм')
    registration_page.fill_field(registrationPageLocators.patronymic, 'ТестОтч')
    registration_page.fill_dob(registrationPageLocators.dob, '29101995')
    registration_page.fill_field(registrationPageLocators.password1, '00000000')
    registration_page.fill_field(registrationPageLocators.password_confirm, '00000000')
    registration_page.click(registrationPageLocators.registration_btn)
    registration_page.click(registrationPageLocators.registration_btn)

    registration_page.assert_text(registrationPageLocators.email_validation, 'Некорректный email!')


def test_dob_isincorrect(browser):
    """В поле Дата рождения указана дата пользователя младше 14 лет"""
    main_page = mainPageHelper(browser, mainPageLocators.url)
    main_page.open()
    main_page.go_to_registration()
    registration_page = registrationPageHelper(browser, None)
    email = registration_page.random_email()
    registration_page.fill_field(registrationPageLocators.email, email)
    registration_page.fill_field(registrationPageLocators.surname, 'ТестФам')
    registration_page.fill_field(registrationPageLocators.name, 'ТестИм')
    registration_page.fill_field(registrationPageLocators.patronymic, 'ТестОтч')
    registration_page.fill_dob(registrationPageLocators.dob, '29102020')
    registration_page.fill_field(registrationPageLocators.password1, '00000000')
    registration_page.fill_field(registrationPageLocators.password_confirm, '00000000')
    registration_page.click(registrationPageLocators.registration_btn)

    registration_page.assert_text(registrationPageLocators.dob_validation, 'Минимальный возраст 14 лет!')


def test_password_tooshort(browser):
    """Поле Пароль содержит менее восьми символов"""
    main_page = mainPageHelper(browser, mainPageLocators.url)
    main_page.open()
    main_page.go_to_registration()
    registration_page = registrationPageHelper(browser, None)
    email = registration_page.random_email()
    registration_page.fill_field(registrationPageLocators.email, email)
    registration_page.fill_field(registrationPageLocators.surname, 'ТестФам')
    registration_page.fill_field(registrationPageLocators.name, 'ТестИм')
    registration_page.fill_field(registrationPageLocators.patronymic, 'ТестОтч')
    registration_page.fill_dob(registrationPageLocators.dob, '29101995')
    registration_page.fill_field(registrationPageLocators.password1, '0000000')
    registration_page.fill_field(registrationPageLocators.password_confirm, '0000000')
    registration_page.click(registrationPageLocators.registration_btn)

    registration_page.assert_text(registrationPageLocators.password_validation, 'Минимальное количество символов: 8!')


def test_password_toolong(browser):
    """Поле Пароль содержит менее восьми символов"""
    main_page = mainPageHelper(browser, mainPageLocators.url)
    main_page.open()
    main_page.go_to_registration()
    registration_page = registrationPageHelper(browser, None)
    email = registration_page.random_email()
    registration_page.fill_field(registrationPageLocators.email, email)
    registration_page.fill_field(registrationPageLocators.surname, 'ТестФам')
    registration_page.fill_field(registrationPageLocators.name, 'ТестИм')
    registration_page.fill_field(registrationPageLocators.patronymic, 'ТестОтч')
    registration_page.fill_dob(registrationPageLocators.dob, '29101995')
    registration_page.fill_field(registrationPageLocators.password1, '1231231231231231231231231231231')
    registration_page.fill_field(registrationPageLocators.password_confirm, '0000000')
    registration_page.click(registrationPageLocators.registration_btn)

    registration_page.assert_text(registrationPageLocators.password_validation, 'Максимальное количество символов: 30!')


def test_passwords_arent_equal(browser):
    """Поле Пароль содержит менее восьми символов"""
    main_page = mainPageHelper(browser, mainPageLocators.url)
    main_page.open()
    main_page.go_to_registration()
    registration_page = registrationPageHelper(browser, None)
    email = registration_page.random_email()
    registration_page.fill_field(registrationPageLocators.email, email)
    registration_page.fill_field(registrationPageLocators.surname, 'ТестФам')
    registration_page.fill_field(registrationPageLocators.name, 'ТестИм')
    registration_page.fill_field(registrationPageLocators.patronymic, 'ТестОтч')
    registration_page.fill_dob(registrationPageLocators.dob, '29101995')
    registration_page.fill_field(registrationPageLocators.password1, '0000000')
    registration_page.fill_field(registrationPageLocators.password_confirm, '0000001')
    registration_page.click(registrationPageLocators.registration_btn)

    registration_page.assert_text(registrationPageLocators.password_confirm_validation,
                                  'Пароли должны совпадать!')


def test_registration_goback_btn(browser):
    """Кнопка "назад" возвращает на главную"""
    main_page = mainPageHelper(browser, mainPageLocators.url)
    main_page.open()
    main_page.go_to_registration()
    registration_page = registrationPageHelper(browser, None)
    registration_page.click(registrationPageLocators.go_back_btn)

    main_page.assert_element(mainPageLocators.sing_in)


def test_redir_to_signin(browser):
    """Кнопка "назад" возвращает на главную"""
    main_page = mainPageHelper(browser, mainPageLocators.url)
    main_page.open()
    main_page.go_to_registration()
    registration_page = registrationPageHelper(browser, None)
    registration_page.click(registrationPageLocators.go_to_auth_btn)
    login_page = loginPageHelper(browser, None)

    login_page.assert_element(loginPageLocators.submit)

