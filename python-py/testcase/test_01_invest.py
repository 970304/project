from testdata.invest_datas import InvestData as it
import pytest


@pytest.mark.usefixtures("user_login")
@pytest.mark.usefixtures("refresh")
class TestInvest():

    @pytest.mark.parametrize("data", it.failed_data_01)
    def test_01_failed(self, data, user_login):
        user_login[1].invest(data['money'], data['pwd'])
        msg = user_login[1].alert_txt()
        user_login[1].alert_acept()
        assert data['check_msg'] == msg

    @pytest.mark.parametrize("data", it.failed_data)
    def test_00_failed(self, data, user_login):
        user_login[1].invest(data['money'], data['pwd'])
        assert data['check_msg'] == user_login[1].get_error_msg()

    def test_02_success(self, user_login):
        invest_after_money = user_login[1].get_money()
        user_login[1].invest(it.success_data['money'], it.success_data['pwd'])
        user_login[1].alert_acept()
        invest_before_money = user_login[1].get_money()
        assert int(it.success_data['money']) == int(float(invest_after_money)-float(invest_before_money))






