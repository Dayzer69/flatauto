from playwright.sync_api import Page
from Pages.basePage import BasePage
from time import sleep


class loginPageLocators:
    email = '#email'
    password = '#password'
    submit = '#kc-login'
    goback_btn = '.back-button'
    go_password_rec = '//*[@id="kc-form"]/div[2]/span/a'
    go_registartion = '#kc-registration'
    go_to_support_btn = '//html/body/div[2]/a[1]'
    go_to_about_btn = '//html/body/div[2]/a[2]'

    validation_email_text = '//*[@id="kc-form-login"]/div[1]'
    validation_password_text = '//*[@id="kc-form-login"]/div[2]'

    success_login_data = ['tischin.anton2011@yandex.ru', 'Password69']
    negative_login_data = ['somemail00@test.ru', 'someword69']


class loginPageHelper(BasePage):
    def fill_field(self, locator_info, data):
        self.page.locator(locator_info).fill(data)

    def submit_click(self):
        return self.page.locator(loginPageLocators.submit).click()

    def login_text(self):
        return self.page.locator(loginPageLocators.validation_email_text).text()

    def password_text(self):
        return self.page.locator(loginPageLocators.validation_password_text).text()




