from Pages.basePage import BasePage
from playwright.sync_api import Playwright

class mainPageLocators:
    sing_in = ('//*[@id="root"]/div/div/div[1]/div[1]/div[2]/p[1]')
    registration = ('//*[@id="root"]/div/div/div[1]/div[1]/div[2]/p[2]')
    location = ('//*[@id="root"]/div/div/div[1]/div[1]/div[1]/div/p')

    url = 'https://flat-renta.test.madela.dev/'


class mainPageHelper(BasePage):
    def go_to_sign_in(self):
        return self.page.locator(mainPageLocators.sing_in).click()

    def go_to_registration(self):
        return self.page.locator(mainPageLocators.registration).click()

    def user_location(self):
        return self.page.locator(mainPageLocators.location).toContainText()