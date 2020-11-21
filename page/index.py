from common.contants import index_dir, main1_dir
from page.Unified_dataPage.unified_dataPage import Unified_Data
from page.basepage import BasePage
from page.unified_authorization.unified_authorizationPage import Unified_Authorization


class Index(BasePage):
    def goto_unified_data(self):
        '''
        打開統一數據
        '''
        try:
            self.step(index_dir, "goto_unified_data")
            return Unified_Data(self._driver)
        except Exception as e:
            print("登錄認證出問題了！")
            raise e


    def goto_unified_authorization(self):
        '''
        打开统一授权页面
        '''
        self.step(index_dir,"goto_unified_authorization")
        return Unified_Authorization(self._driver)

    def quit(self):
        '''
        推出當前登陸賬號
        :return:
        '''
        self.step(index_dir,"quit")

    def close(self):
        self._driver.quit()

    def close_drawer(self):
        '''
        關閉彈出層
        '''
        try:
            ele = self.step(main1_dir, "close_drawer")
            ele.click()
        except Exception as e:
            pass