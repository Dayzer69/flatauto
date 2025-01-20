from playwright.sync_api import Page, expect, sync_playwright

class BasePage:
    def __init__(self, page, url):
        self.page = page
        self.url = url


    def open(self):
        self.page.goto(self.url)

    def assert_element(self, element):
        expect(self.page.locator(element)).to_be_visible()

    def assert_text(self, element, text):
        expect(self.page.locator(element)).to_contain_text(text)

    def assert_url(self, url):
        expect(self.page).to_have_url(url)

    def click(self, element):
        return self.page.locator(element).click()

    def fill_field(self, element, data):
        return self.page.locator(element).fill(data)





