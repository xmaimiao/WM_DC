from common.contants import unified_dataPage_dir
from page.Unified_dataPage.userPage import User
from page.basepage import BasePage


class Unified_Data(BasePage):
    def goto_user(self):
        '''
        打開用戶管理
        '''
        self.step(unified_dataPage_dir,"goto_user")
        return User(self._driver)