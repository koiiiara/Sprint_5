# Sprint_5 

## Структура проекта

- ```tests/``` - Папка с тестами
  - ```test_login.py``` - тесты страницы входа и авторизации
  - ```test_navigation.py``` - тесты переходов по страницам
  - ```test_registration.py``` - тесты страницы регисрации
  - ```test_constructor.py``` - тесты переключения вкладок на странице "Конструктор"


- ```data/``` - Папка с переменными и локаторами
  - ```account_data.py``` - реквизиты тестового аккаунта
  - ```locators.py``` - локаторы и их описания


- ```helpers/``` - Папка с вспомогательными функциями
  - ```data_generators.py``` - генератор тестовых учетных записей
  - ```macros.py``` - вспомогательные функции


- ```conftest.py``` - файл конфигурации PyTest
