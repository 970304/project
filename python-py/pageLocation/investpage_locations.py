from selenium.webdriver.common.by import By


class InvestPageLocations:

    # 投资金额
    invest_money = (By.ID, 'amountPay')
    # 投资密码
    invest_pwd = (By.ID, 'passwordPay')

    invest_but = (By.XPATH, '//*[@value="立即投资"]')
    # 金额
    account_balance =(By.XPATH, '//*[@class="account-balance-value"]')
    # 错误信息
    invest_error_msg = (By.XPATH, '//*[@id="terr"]')




