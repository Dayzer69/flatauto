from random import sample
from string import ascii_lowercase

from time import sleep

x = ''.join(sample(ascii_lowercase, 10)) + '@test.ru'
print(x)





import re
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://flat-renta.test.madela.dev/")
    page.get_by_text("Регистрация").click()
    page.get_by_placeholder("Электронная почта").fill(x)
    page.get_by_placeholder("Фамилия").fill('familia')

    page.get_by_placeholder("Имя").fill('imya')
    page.get_by_placeholder("Отчество").fill('otchestvo')
    page.locator('//*[@id="user.attributes.birthday"]').type('29101995')
    page.get_by_placeholder("Пароль").fill('44768282')
    page.get_by_placeholder("Подтверждение пароля").fill('44768282')
    page.get_by_role("button", name="Регистрация").click()
    sleep(90000)

    # ---------------------


with sync_playwright() as playwright:
    run(playwright)

