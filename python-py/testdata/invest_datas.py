class InvestData:

    success_data = {"money":"1000", "pwd":"123456", "check_msg":""}

    failed_data = [{"money":"", "pwd":"", "check_msg":"请填写投资金额"},
                   {"money":"100", "pwd":"", "check_msg":"请填写交易密码"}]

    failed_data_01 = [{"money":"10", "pwd":"123", "check_msg":"你输入的小于起投金额"},
                    {"money":"1000", "pwd":"123", "check_msg":"您输入的交易密码错误"}
                   ]



