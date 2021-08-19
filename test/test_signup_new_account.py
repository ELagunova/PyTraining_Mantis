import random
import string


def random_username(prefix='', maxlen=1):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_signup_new_account(app):
    username = random_username("user_", 10)
    password = 'test'
    email = username + '@localhost'
    app.james.ensure_user_exists(username, password)
    app.signup.new_user(username, password, email)
    assert app.soap.can_login(username, password)