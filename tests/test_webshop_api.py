import allure
from allure_commons._allure import step
from selene import browser, be
from selene.support.conditions import have
from api.add_item_to_cart import api_call
from utils.data import MAIN_URL


@allure.tag("web")
@allure.label("owner", "Andreev Petr")
@allure.feature("Добавление товара в корзину")
@allure.story("Успешное добавление товара в корзину и удаление")
def test_add_item_cart_api(delete_items_in_cart):
    with step("Add to cart"):
        api_call.add_item_to_cart("/43/1/1")

    with step("Open browser"):
        browser.open(MAIN_URL)

    with step("Verify successful add to cart"):
        browser.element(".cart-qty").should(have.text("(1)"))
        browser.element('#topcartlink').click()
        browser.element(".product-price").should(have.text("100.00"))
        browser.element(".product-name").should(have.text("Smartphone"))


@allure.tag("web")
@allure.label("owner", "Andreev Petr")
@allure.feature("Добавление нескольких товаров в корзину")
@allure.story("Успешное добавление нескольких товаров в корзину и удаление")
def test_add_to_cart_book_api(delete_items_in_cart):
    with step("Add to cart"):
        api_call.add_item_to_cart("/13/1/3")
        api_call.add_item_to_cart("/22/1/2")

    with step("Open browser"):
        browser.open(MAIN_URL)

    with step("Verify successful add to cart"):
        browser.element(".cart-qty").should(have.text("(5)"))
        browser.element('#topcartlink').click()
        browser.element("//a[@class='product-name' and text()='Computing and Internet']").should(be.visible)
        browser.element("//a[@class='product-name' and text()='Health Book']").should(be.visible)
