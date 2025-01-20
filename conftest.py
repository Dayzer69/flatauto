import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope="session", autouse=True)
def browser_context_args(browser_context_args):
    return {

        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }



@pytest.fixture(scope="function")
def browser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(
        geolocation={"latitude": 55.7558, "longitude": 37.6173},
        permissions=["geolocation"]
    )
    yield context.new_page()
    context.close()
    browser.close()

@pytest.fixture(scope='function')
def api_request_context(playwright: Playwright):
    request_context = playwright.request.new_context()
    yield request_context
    request_context.dispose()
