# pytest Tests\test_login_page.py


from Pages.mainPage import mainPageHelper, mainPageLocators
from Pages.loginPage import loginPageLocators, loginPageHelper
from Pages.usersPage import usersPageLocators
from Pages.passwordRecoveryPage import passwordRecoveryPageLocators
from Pages.registrationPage import registrationPageLocators
from Pages.basePage import BasePage



def test_success_auth(browser):
    """Корректное заполнение всех полей для авторизации"""
    main_page = mainPageHelper(browser, mainPageLocators.url)
    main_page.open()
    main_page.go_to_sign_in()
    login_page = loginPageHelper(browser, None)
    login_page.fill_field(loginPageLocators.email, loginPageLocators.success_login_data[0])
    login_page.fill_field(loginPageLocators.password, loginPageLocators.success_login_data[1])
    login_page.submit_click()
    user_page = BasePage(browser, None)

    user_page.assert_element(usersPageLocators.user_ico)


def test_unsuccess_auth(browser):
    """Заполение полей для авторизации некорректными данными"""
    main_page = mainPageHelper(browser, mainPageLocators.url)
    main_page.open()
    main_page.go_to_sign_in()
    login_page = loginPageHelper(browser, None)
    login_page.fill_field(loginPageLocators.email, loginPageLocators.negative_login_data[0])
    login_page.fill_field(loginPageLocators.password, loginPageLocators.negative_login_data[1])
    login_page.submit_click()

    login_page.assert_text(loginPageLocators.validation_email_text, ' Неправильное имя пользователя или пароль.')


def test_empty_fields(browser):
    """Авторизация с пустыми полями"""
    main_page = mainPageHelper(browser, mainPageLocators.url)
    main_page.open()
    main_page.go_to_sign_in()
    login_page = loginPageHelper(browser, None)
    login_page.submit_click()

    login_page.assert_text(loginPageLocators.validation_email_text, ' Обязательное поле!')


def test_empty_email_field(browser):
    """Авторизация с пустым полем логина"""
    main_page = mainPageHelper(browser, mainPageLocators.url)
    main_page.open()
    main_page.go_to_sign_in()
    login_page = loginPageHelper(browser, None)
    login_page.fill_field(loginPageLocators.password, loginPageLocators.success_login_data[1])
    login_page.submit_click()

    login_page.assert_text(loginPageLocators.validation_email_text, ' Обязательное поле!')


def test_empty_password_field(browser):
    """Авторизация с пустым полем логина"""
    main_page = mainPageHelper(browser, mainPageLocators.url)
    main_page.open()
    main_page.go_to_sign_in()
    login_page = loginPageHelper(browser, None)
    login_page.fill_field(loginPageLocators.email, loginPageLocators.negative_login_data[0])
    login_page.submit_click()

    login_page.assert_text(loginPageLocators.validation_password_text, ' Обязательное поле!')


def test_uncorrect_email(browser):
    """Авторизация с неправильным логином"""
    main_page = mainPageHelper(browser, mainPageLocators.url)
    main_page.open()
    main_page.go_to_sign_in()
    login_page = loginPageHelper(browser, None)
    login_page.fill_field(loginPageLocators.email, loginPageLocators.negative_login_data[0])
    login_page.fill_field(loginPageLocators.password, loginPageLocators.success_login_data[1])
    login_page.submit_click()

    login_page.assert_text(loginPageLocators.validation_email_text, ' Неправильное имя пользователя или пароль.')


def test_uncorrect_password(browser):
    """Авторизация с неправильным паролем"""
    main_page = mainPageHelper(browser, mainPageLocators.url)
    main_page.open()
    main_page.go_to_sign_in()
    login_page = loginPageHelper(browser, None)
    login_page.fill_field(loginPageLocators.email, loginPageLocators.success_login_data[0])
    login_page.fill_field(loginPageLocators.password, loginPageLocators.negative_login_data[1])
    login_page.submit_click()

    login_page.assert_text(loginPageLocators.validation_email_text, ' Неправильное имя пользователя или пароль.')


def test_redir_to_main(browser):
    """Переход на главную страницу со страницы авторизации"""
    main_page = mainPageHelper(browser, mainPageLocators.url)
    main_page.open()
    main_page.go_to_sign_in()
    login_page = loginPageHelper(browser, None)
    login_page.click(loginPageLocators.goback_btn)

    login_page.assert_element(mainPageLocators.sing_in)


def test_redir_to_passwordrecovery(browser):
    """Переход на страницу восстановления пароля"""
    main_page = mainPageHelper(browser, mainPageLocators.url)
    main_page.open()
    main_page.go_to_sign_in()
    login_page = loginPageHelper(browser, None)
    login_page.fill_field(loginPageLocators.email, loginPageLocators.success_login_data[0])
    login_page.click(loginPageLocators.go_password_rec)
    password_rec_page = BasePage(browser, None)

    password_rec_page.assert_element(passwordRecoveryPageLocators.send_btn)


def test_redir_to_registration(browser):
    """Переход на страницу регистрации"""
    main_page = mainPageHelper(browser, mainPageLocators.url)
    main_page.open()
    main_page.go_to_sign_in()
    login_page = loginPageHelper(browser, None)
    login_page.fill_field(loginPageLocators.email, loginPageLocators.success_login_data[0])
    login_page.click(loginPageLocators.go_registartion)
    registration_page = BasePage(browser, None)

    registration_page.assert_element(registrationPageLocators.password_confirm)


def test_redir_to_support(browser):
    """Переход на страницу восстановления пароля"""
    main_page = mainPageHelper(browser, mainPageLocators.url)
    main_page.open()
    main_page.go_to_sign_in()
    main_page.click(loginPageLocators.go_to_support_btn)
    support_page = BasePage(browser, None)

    support_page.assert_url('https://flat-renta.test.madela.dev//support')


def test_redir_to_about(browser):
    """Переход на страницу восстановления пароля"""
    main_page = mainPageHelper(browser, mainPageLocators.url)
    main_page.open()
    main_page.go_to_sign_in()
    main_page.click(loginPageLocators.go_to_about_btn)
    about_page = BasePage(browser, None)

    about_page.assert_url('https://flat-renta.test.madela.dev//about')