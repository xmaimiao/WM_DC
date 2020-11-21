from common.contants import unified_authorizationPage_dir
from page.basepage import BasePage
from page.unified_authorization.role_management import Role_Management


class Unified_Authorization(BasePage):

    def goto_role_management(self):
        '''
        打開角色管理頁面
        :return:
        '''
        self.step(unified_authorizationPage_dir,"goto_role_management")
        return Role_Management(self._driver)


