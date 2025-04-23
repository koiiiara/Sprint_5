from conftest import *
from data.locators import Locators as Loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSwitchMenu:
    def test_switch_from_default_to_sauce(self, driver):
        # Переходим на главную страницу
        driver.get(urls.BASE_URL)

        #Находим нажатую по дефолту кнопку "Булки"
        buns_tab_button = driver.find_element(*Loc.ACTIVE_BUNS_BUTTON)

        # Находим не нажатую кнопку "Соусы" и кликаем по ней
        sauce_tab_button = driver.find_element(*Loc.INACTIVE_SAUCE_BUTTON)
        sauce_tab_button.click()

        #Проверяем, что кнопка "Соусы" стала нажатой, а кнопка "булки" не нажатой
        #Проверку совершаем по наличию класса "type_current", который присутствует только у нажатой кнопки
        assert ("type_current" in sauce_tab_button.get_attribute("class") and
                "type_current" not in buns_tab_button.get_attribute("class"))

    def test_switch_from_default_to_topping(self, driver):
        # Переходим на главную страницу
        driver.get(urls.BASE_URL)

        #Находим нажатую по дефолту кнопку "Булки"
        buns_tab_button = driver.find_element(*Loc.ACTIVE_BUNS_BUTTON)

        # Находим не нажатую кнопку "Начинки" и кликаем по ней
        topping_tab_button = driver.find_element(*Loc.INACTIVE_SAUCE_BUTTON)
        topping_tab_button.click()

        #Проверяем, что кнопка "Начинки" стала нажатой, а кнопка "булки" не нажатой
        #Проверку совершаем по наличию класса "type_current", который присутствует только у нажатой кнопки
        assert ("type_current" in topping_tab_button.get_attribute("class") and
                "type_current" not in buns_tab_button.get_attribute("class"))

    def test_switch_from_sauce_to_buns(self, driver):
        # Переходим на главную страницу
        driver.get(urls.BASE_URL)

        # Находим не нажатую кнопку "Соусы" и кликаем по ней
        sauce_tab_button = driver.find_element(*Loc.INACTIVE_SAUCE_BUTTON)
        sauce_tab_button.click()

        #Дожидаемся появления не нажатой кнопки "Булки" и кликаем по ней
        buns_tab_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Loc.INACTIVE_BUNS_BUTTON)
        )
        buns_tab_button.click()

        # Проверяем, что кнопка "Булки" стала нажатой, а кнопка "Соусы" не нажатой
        # Проверку совершаем по наличию класса "type_current", который присутствует только у нажатой кнопки
        assert ("type_current" not in sauce_tab_button.get_attribute("class") and
                "type_current" in buns_tab_button.get_attribute("class"))