import data.urls as urls
from conftest import driver
from data.locators import Locators as Loc
from helpers import macros
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestNavigation:

    def test_go_to_account(self, driver, go_to_login_page):
        #Заполняем форму входа
        macros.fill_login_form(driver)
        # Нажимаем "Войти"
        login_button = driver.find_element(*Loc.LOGIN_BUTTON)
        login_button.click()
        # Дожидаемся появления заголовка "Соберите бургер" на главной странице
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Loc.BUILD_BURGER_TITLE)
        )
        #Находим кнопку перехода в ЛК и кликаем по ней
        account_button = driver.find_element(*Loc.ACCOUNT_BUTTON)
        account_button.click()
        # Дожидаемся когда появится кнопка "История заказов"
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Loc.HISTORY_ORDERS_BUTTON)
        )
        #Проверяем что URL страницы правильный
        assert driver.current_url == urls.ACCOUNT_PAGE


    def test_go_to_constructor_from_account_by_constructor_button(self, driver, go_to_account_page):
        #Находим кнопку "Конструктор" и кликаем по ней
        constructor_button = driver.find_element(*Loc.CONSTRUCTOR_BUTTON)
        constructor_button.click()

        # Дожидаемся появления заголовка "Соберите бургер" на главной странице
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Loc.BUILD_BURGER_TITLE)
        )
        #Проверяем что URL страницы правильный
        assert driver.current_url == urls.BASE_URL


    def test_go_to_constructor_from_account_by_logo(self, driver, go_to_account_page):
        #Находим логотип и кликаем по нему
        logo_button = driver.find_element(*Loc.LOGO)
        logo_button.click()

        # Дожидаемся появления заголовка "Соберите бургер" на главной странице
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Loc.BUILD_BURGER_TITLE)
        )
        #Проверяем что URL страницы правильный
        assert driver.current_url == urls.BASE_URL

    def test_exit_from_account(self, driver, go_to_account_page):
        #Находим кнопку выхода и кликаем по ней
        exit_button = driver.find_element(*Loc.EXIT_BUTTON)
        exit_button.click()

        # Дожидаемся появления кнопки "Войти"
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Loc.LOGIN_BUTTON)
        )
        #Проверяем что URL страницы правильный
        assert driver.current_url == urls.LOGIN_PAGE
