from selenium.webdriver.common.by import By


class LoginPageLocation:

    login = (By.XPATH, '//*[text()="登录"]')

    username = (By.ID, 'username')

    pwd = (By.ID, 'password')

    login_but = (By.ID, 'login')

    error_msg = (By.XPATH, '//*[@id="errs"]')






