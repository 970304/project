from selenium.webdriver.common.by import By


class HomePageLocations:

    # 用户链接
    user_home = (By.XPATH, '//*[@id="top"]/div/div[2]/p[1]/a[2]')
    # 首页按钮
    home_page = (By.XPATH, '//*[text()="首页"]')
    # 投资按钮
    select_invest = (By.XPATH, '//*[text()="立即投资"][1]')


