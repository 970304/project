from testdata.login_datas import LoginData as ld
import pytest


@pytest.mark.usefixtures('open_web')
@pytest.mark.usefixtures('refresh')
class TestLogin():

    @pytest.mark.parametrize("data", ld.fail_data)
    def test_login_00_failed(self, data, open_web):
        open_web[1].login(data['username'], data['pwd'])
        assert data['check_msg'] == open_web[1].get_error_msg()

    def test_login_01_success(self, open_web):
        open_web[1].login(ld.success_data['username'], ld.success_data['pwd'])
        assert open_web[1].user_home_exist()









