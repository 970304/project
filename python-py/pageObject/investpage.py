from common.basepage import BasePage
from pageLocation.investpage_locations import InvestPageLocations as ipl
from pageLocation.homepage_locations import HomePageLocations as hpl


class InvestPage(BasePage):

    def invest(self, money, pwd):
        doc = "投资_投资"
        self.wait_ele_view(ipl.invest_money, doc=doc)
        self.input_text(ipl.invest_money, money, doc)
        self.input_text(ipl.invest_pwd, pwd, doc)
        self.ele_click(ipl.invest_but, doc)

    def get_money(self):
        doc = "获取金额"
        self.wait_ele_view(ipl.account_balance, doc=doc)
        return self.get_ele_text(ipl.account_balance, doc)

    def home_page(self):
        doc = "投资_首页"
        self.wait_ele_view(hpl.home_page, doc=doc)
        self.ele_click(hpl.home_page, doc)
        self.ele_click(hpl.select_invest, doc)

    def get_error_msg(self):
        doc = '首页_投资'
        self.wait_ele_view(ipl.invest_error_msg, doc=doc)
        return self.get_ele_text(ipl.invest_error_msg, doc)





