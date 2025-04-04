import pytest
from selenium import webdriver
import data.urls as urls
from data.locators import Locators as Loc
from helpers.macros import fill_login_form
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def go_to_login_page(driver):
    # Переходим на главную страницу
    driver.get(urls.BASE_URL)
    # Дожидаемся когда кнопка входа в ЛК появится и станет кликабельной и кликаем по ней
    account_button = (WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Loc.ACCOUNT_BUTTON)
    ))
    account_button.click()
    #Дожидаемся пока кнопка "Войти" станет кликабельной
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Loc.LOGIN_BUTTON)
    )

@pytest.fixture(scope="function")
def go_to_register_page(driver, go_to_login_page):
    # Дожидаемся когда кнопка перехода на страницу регистрации станет кликабельно и кликаем по ней
    register_link_button = (WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Loc.GO_TO_REGISTER_BUTTON)
    ))
    register_link_button.click()

    # Дожидаемся когда кнопка "Зарегистрироваться" в форме регистрации станет кликабельной
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Loc.REGISTER_BUTTON)
    )

@pytest.fixture(scope="function")
def go_to_account_page(driver, go_to_login_page):
    # Заполняем форму входа
    fill_login_form(driver)
    # Нажимаем "Войти"
    login_button = driver.find_element(*Loc.LOGIN_BUTTON)
    login_button.click()
    # Дожидаемся появления заголовка "Соберите бургер" на главной странице
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(Loc.BUILD_BURGER_TITLE)
    )
    # Находим кнопку перехода в ЛК и кликаем по ней
    account_button = driver.find_element(*Loc.ACCOUNT_BUTTON)
    account_button.click()
    # Дожидаемся когда появится кнопка "История заказов"
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(Loc.HISTORY_ORDERS_BUTTON)
    )
