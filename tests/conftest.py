import pytest
from selene import browser, be
import allure
from utils.tools import get_auth_cookie, add_auth_cookie


@pytest.fixture(scope='function', autouse=True)
@allure.title('Очищение корзины')
def delete_items_in_cart():
    deleted_items_count = 0
    browser.element('#topcartlink').click()
    if browser.element('td.remove-from-cart input[type=checkbox]').matching(be.clickable):
        with allure.step("Удаление лишнего товара"):
            icon_list = browser.all('td.remove-from-cart input[type=checkbox]')
            for icon in icon_list:
                icon.click()
                deleted_items_count += 1
            browser.element('.update-cart-button').click()
            browser.element('.update-cart-button').matching(be.hidden)
    else:
        with allure.step("Корзина изначально пустая"):
            pass

    allure.attach(f'Количество удаленных товаров из корзины: {str(deleted_items_count)}')


@pytest.fixture(scope='session', autouse=True)
def set_browser():
    with allure.step('Browser config'):
        browser.config.window_width = 1920
        browser.config.window_height = 1080

    with allure.step('Add authorization cookie'):
        get_auth_cookie()
        add_auth_cookie()

    yield browser

    with allure.step('Close browser'):
        browser.quit()
