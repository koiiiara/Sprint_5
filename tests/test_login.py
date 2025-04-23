from conftest import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from data.locators import Locators as Loc
from helpers.macros import fill_login_form


class TestLogin:
    def test_login_from_account_button(self, driver):
        # Переходим на главную страницу
        driver.get(urls.BASE_URL)
        # Дожидаемся когда кнопка входа в ЛК станет кликабельной и кликаем по ней
        account_button = (WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Loc.ACCOUNT_BUTTON)
        ))
        account_button.click()
        # Дожидаемся пока кнопка "Войти" появится и станет кликабельной
        login_button = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Loc.LOGIN_BUTTON)
        )
        #Заполняем форму входа
        fill_login_form(driver)
        #Нажимаем "Войти"
        login_button.click()
        #Дожидаемся появления заголовка "Соберите бургер"
        WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(Loc.BUILD_BURGER_TITLE)
        )
        assert driver.current_url == urls.BASE_URL

    def test_login_from_home_page(self, driver):
        # Переходим на главную страницу
        driver.get(urls.BASE_URL)
        # Дожидаемся когда кнопка "Войти в аккаунт" станет кликабельной и кликаем по ней
        enter_account_button = (WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Loc.ACCOUNT_BUTTON)
        ))
        enter_account_button.click()
        # Дожидаемся пока кнопка "Войти" станет кликабельной
        login_button = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Loc.LOGIN_BUTTON)
        )
        # Заполняем форму входа
        fill_login_form(driver)
        # Нажимаем "Войти"
        login_button.click()
        # Дожидаемся появления заголовка "Соберите бургер"
        WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(Loc.BUILD_BURGER_TITLE)
        )
        assert driver.current_url == urls.BASE_URL

    def test_login_from_register_page(self, driver, go_to_register_page):
        #Дожидаемся появления кнопки ссылки на страницу входа и кликаем по ней
        enter_account_button = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Loc.ENTER_ACCOUNT_LINK_BUTTON)
        )
        enter_account_button.click()

        # Дожидаемся пока кнопка "Войти" станет кликабельной
        login_button = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Loc.LOGIN_BUTTON)
        )
        # Заполняем форму входа
        fill_login_form(driver)
        # Нажимаем "Войти"
        login_button.click()
        # Дожидаемся появления заголовка "Соберите бургер"
        WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(Loc.BUILD_BURGER_TITLE)
        )
        assert driver.current_url == urls.BASE_URL

    def test_login_from_recover_pass_page(self, driver, go_to_login_page):
        #Дожидаемся когда появится кнопка "Восстановить пароль" и кликаем по ней
        recover_pass_button = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Loc.RECOVER_PASS_BUTTON)
        )
        recover_pass_button.click()

        # Дожидаемся появления кнопки ссылки да страницу входа и кликаем по ней
        enter_account_button = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Loc.ENTER_ACCOUNT_LINK_BUTTON)
        )
        enter_account_button.click()

        # Дожидаемся пока кнопка "Войти" станет кликабельной
        login_button = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Loc.LOGIN_BUTTON)
        )
        # Заполняем форму входа
        fill_login_form(driver)
        # Нажимаем "Войти"
        login_button.click()
        # Дожидаемся появления заголовка "Соберите бургер"
        WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(Loc.BUILD_BURGER_TITLE)
        )
        assert driver.current_url == urls.BASE_URL

