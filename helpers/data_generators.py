from random import randint

def gen_username():
    return f'Test_user_{str(randint(1000, 9999))}'

def gen_password():
    return f'testpass{str(randint(1000, 9999))}'

def gen_email(username):
    return f'{username}@yandex.ru'

def generate_user():
    username = gen_username()
    return {'username': username,
            'password': gen_password(),
            'email': gen_email(username)}