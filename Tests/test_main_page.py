from Pages.mainPage import mainPageHelper, mainPageLocators
from Pages.loginPage import loginPageLocators
from Pages.registrationPage import registrationPageLocators


def test_go_to_sign_in(browser):
    main_page = mainPageHelper(browser, mainPageLocators.url)
    main_page.open()
    main_page.go_to_sign_in()

    main_page.assert_element(loginPageLocators.submit)


def test_go_to_registration(browser):
    main_page = mainPageHelper(browser, mainPageLocators.url)
    main_page.open()
    main_page.go_to_registration()

    main_page.assert_element(registrationPageLocators.registration_btn)




