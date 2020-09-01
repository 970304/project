from common.basepage import BasePage
from pageLocation.loginpage_locations import LoginPageLocation as lpl
from pageLocation.homepage_locations import HomePageLocations as hpl


class LoginPage(BasePage):

    def login(self, username, pwd):
        doc = "登录界面——登录"
        self.wait_ele_view(lpl.username, doc=doc)
        self.input_text(lpl.username, username, doc=doc)
        self.input_text(lpl.pwd, pwd, doc)
        self.ele_click(lpl.login_but, doc)

    def get_error_msg(self):
        doc = '登陆界面_获取错误信息'
        self.wait_ele_view(lpl.error_msg, doc=doc)
        return self.get_ele_text(lpl.error_msg, doc=doc)

    def user_home_exist(self):
        doc = '登陆界面_获取错误信息'
        return self.wait_ele_exist(hpl.user_home, doc=doc)














