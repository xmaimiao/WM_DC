import yaml

from common.contants import main1_dir, basepage_dir
from page.Unified_dataPage.unified_dataPage import Unified_Data
from page.basepage import BasePage, _get_working
# from page.loginpage import Login
from page.loginpage import Login
from page.unified_authorization.unified_authorizationPage import Unified_Authorization


class Main(BasePage):
    '''
    首頁面po
    '''
    _working = _get_working()

    with open(basepage_dir, encoding="utf-8") as f:
        env = yaml.safe_load(f)
        if _working != "port":
            _base_url = env["docker_env"][env["default"]]

    def goto_login(self):
        '''
        進去登錄頁面
        '''
        return Login(self._driver)

    def goto_unified_data(self):
        '''
        打開統一數據
        '''
        self.step(main1_dir,"goto_unified_data")
        return Unified_Data(self._driver)

    def close_adduser_pop(self):
        '''
        添加成员成功的确认框，在main提供关闭的入口
        '''
        self.step(main1_dir,"close_adduser_pop")
        return self

    def goto_unified_authorization(self):
        '''
        打开统一授权页面
        '''
        self.step(main1_dir,"goto_unified_authorization")
        return Unified_Authorization(self._driver)

    def close_drawer(self):
        '''
        關閉彈出層
        '''
        try:
            ele = self.step(main1_dir, "close_drawer")
            ele.click()
        except Exception as e:
            pass


