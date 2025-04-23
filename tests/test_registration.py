import data.urls as urls
from conftest import *
from data.locators import Locators as Loc
from helpers.data_generators import generate_user
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestRegistration:

    def test_registration_with_valid_data(self, driver, go_to_register_page):
        user_cred = generate_user()

        #Дожидаемся появление полей для регистрации и сохраняем их в переменные
        name_field = WebDriverWait(driver, 3).until(
            ec.element_to_be_clickable(Loc.REGISTER_NAME_FIELD)
        )
        email_field = WebDriverWait(driver, 3).until(
            ec.element_to_be_clickable(Loc.REGISTER_EMAIL_FIELD)
        )
        pass_field = WebDriverWait(driver, 3).until(
            ec.element_to_be_clickable(Loc.REGISTER_PASS_FIELD)
        )

        #Заполняем поля и нажимаем кнопку "Зарегистрироваться"
        name_field.send_keys(user_cred['username'])
        email_field.send_keys(user_cred['email'])
        pass_field.send_keys(user_cred['password'])

        #Находим кнопку "Зарегистрироваться" и кликаем по ней
        register_button = driver.find_element(*Loc.REGISTER_BUTTON)
        register_button.click()
        #Джем пока не появится кнопка входа
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable(Loc.LOGIN_BUTTON))
        #Проверяем, что URL текущей страницы это /login
        assert driver.current_url == urls.LOGIN_PAGE

    def test_registration_with_empty_name(self, driver, go_to_register_page):
        user_cred = generate_user()
        #Проверяем, что текущая страница - страница регистрации
        assert driver.current_url == urls.REGISTER_PAGE

        #Дожидаемся появление полей для регистрации и сохраняем их в переменные
        name_field = WebDriverWait(driver, 3).until(
            ec.element_to_be_clickable(Loc.REGISTER_NAME_FIELD)
        )
        email_field = WebDriverWait(driver, 3).until(
            ec.element_to_be_clickable(Loc.REGISTER_EMAIL_FIELD)
        )
        pass_field = WebDriverWait(driver, 3).until(
            ec.element_to_be_clickable(Loc.REGISTER_PASS_FIELD)
        )

        #Заполняем поля и нажимаем кнопку "Зарегистрироваться"
        name_field.send_keys("")
        email_field.send_keys(user_cred['email'])
        pass_field.send_keys(user_cred['password'])

        # Находим кнопку "Зарегистрироваться" и кликаем по ней
        register_button = driver.find_element(*Loc.REGISTER_BUTTON)
        register_button.click()

        #Проверяем, что регистрация не произошла и URL текущей страницы это /register
        assert driver.current_url == urls.REGISTER_PAGE

    def test_registration_with_invalid_email(self, driver, go_to_register_page):
        user_cred = generate_user()
        # Проверяем, что текущая страница - страница регистрации
        assert driver.current_url == urls.REGISTER_PAGE

        # Дожидаемся появление полей для регистрации и сохраняем их в переменные
        name_field = WebDriverWait(driver, 3).until(
            ec.element_to_be_clickable(Loc.REGISTER_NAME_FIELD)
        )
        email_field = WebDriverWait(driver, 3).until(
            ec.element_to_be_clickable(Loc.REGISTER_EMAIL_FIELD)
        )
        pass_field = WebDriverWait(driver, 3).until(
            ec.element_to_be_clickable(Loc.REGISTER_PASS_FIELD)
        )

        # Заполняем поля и нажимаем кнопку "Зарегистрироваться"
        name_field.send_keys(user_cred['username'])
        email_field.send_keys('test_invalid_email@')
        pass_field.send_keys(user_cred['password'])

        # Находим кнопку "Зарегистрироваться" и кликаем по ней
        register_button = driver.find_element(*Loc.REGISTER_BUTTON)
        register_button.click()

        #Проверяем, что регистрация не произошла и URL текущей страницы это /register
        assert driver.current_url == urls.REGISTER_PAGE

    def test_registration_with_invalid_pass(self, driver, go_to_register_page):
        user_cred = generate_user()
        # Проверяем, что текущая страница - страница регистрации
        assert driver.current_url == urls.REGISTER_PAGE

        # Дожидаемся появление полей для регистрации и сохраняем их в переменные
        name_field = WebDriverWait(driver, 3).until(
            ec.element_to_be_clickable(Loc.REGISTER_NAME_FIELD)
        )
        email_field = WebDriverWait(driver, 3).until(
            ec.element_to_be_clickable(Loc.REGISTER_EMAIL_FIELD)
        )
        pass_field = WebDriverWait(driver, 3).until(
            ec.element_to_be_clickable(Loc.REGISTER_PASS_FIELD)
        )

        # Заполняем поля и нажимаем кнопку "Зарегистрироваться"
        name_field.send_keys(user_cred['username'])
        email_field.send_keys(user_cred['email'])
        pass_field.send_keys('abcd')

        # Находим кнопку "Зарегистрироваться" и кликаем по ней
        register_button = driver.find_element(*Loc.REGISTER_BUTTON)
        register_button.click()

        #Дожидаемся появления ошибки "Некорректный пароль"
        invalid_pass_error = WebDriverWait(driver, 3).until(
            ec.visibility_of_element_located(Loc.INVALID_PASS_ERROR)
        )

        assert  invalid_pass_error.text == "Некорректный пароль"

