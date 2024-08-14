from selene import browser
import requests
from utils.data import MAIN_URL, AUTH_DATA


def get_auth_cookie():
    response = requests.post(MAIN_URL + '/login', data=AUTH_DATA, allow_redirects=False)
    cookie = response.cookies.get('NOPCOMMERCE.AUTH')
    return cookie


def add_auth_cookie():
    browser.open(MAIN_URL)
    browser.driver.add_cookie({'name': "NOPCOMMERCE.AUTH", 'value': get_auth_cookie()})
    browser.open(MAIN_URL)
