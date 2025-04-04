from data.locators import Locators as Loc
from data import account_data as ad

def fill_login_form(driver):
    # Сохраняем поля email и пароль в переменные
    email_field = driver.find_element(*Loc.LOGIN_EMAIL_FIELD)
    pass_field = driver.find_element(*Loc.LOGIN_PASS_FIELD)
    # Заполняем поля и нажимаем "Войти"
    email_field.send_keys(ad.EMAIL)
    pass_field.send_keys(ad.PASSWORD)