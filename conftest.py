import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language_changer = Options()
    language_changer.add_experimental_option('prefs', {'intl.accept_languages': f"{request.config.getoption('language')}"})
    browser = webdriver.Chrome(options=language_changer)
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()
