from utils.driver_setup import get_driver
from pages.login_page import LoginPage
import pytest


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")

    message = login_page.get_message()

    assert "You logged into a secure area!" in message


def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("tomsmith", "WrongPassword")

    message = login_page.get_message()

    assert "Your password is invalid!" in message