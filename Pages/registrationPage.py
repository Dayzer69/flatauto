from Pages.basePage import BasePage
from Pages.mainPage import mainPageLocators
from random import sample
from string import ascii_lowercase

class registrationPageLocators:
    email = '#email'
    email_validation = '//*[@id="kc-register-form"]/div[1]/div[2]/div'
    surname = '#lastName'
    surname_validation = '//*[@id="kc-register-form"]/div[2]/div[2]/div'
    name = "#firstName"
    name_validation = '//*[@id="kc-register-form"]/div[3]/div[2]/div'
    patronymic = '//*[@id="user.attributes.middleName"]'
    patronymic_validation = ''
    dob = '//*[@id="user.attributes.birthday"]'
    dob_validation = '//*[@id="kc-register-form"]/div[5]/div[2]/div'
    password1 = '#password'
    password_validation = '//*[@id="kc-register-form"]/div[6]/div[2]/div'
    password_confirm = '#password-confirm'
    password_confirm_validation = '//*[@id="kc-register-form"]/div[7]/div[2]/div'
    registration_btn = '//*[@id="kc-form-buttons"]/input'
    go_to_auth_btn = '//*[@id="kc-form-options"]/div/span/a'
    verification_page_elements = '//html/body/div[3]/div'
    go_back_btn = '//html/body/div[3]/div/div[1]'


class registrationPageHelper(BasePage):
    def go_to_registration(self):
        return self.page.locator(mainPageLocators.registration).click()

    def random_email(self):
        return ''.join(sample(ascii_lowercase, 10)) + '@test.ru'


    def fill_dob(self, element, date):
        field = self.page.locator(element)
        field.click()
        field.type(date)
        return





