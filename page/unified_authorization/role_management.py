from common.contants import role_management_dir
from page.basepage import BasePage
from page.unified_authorization.permission_setting import Permission_Setting


class Role_Management(BasePage):

    def search_role_management(self,role):
        '''
        查询角色管理,並打開該角色的“角色詳情”
        :param role: 要查詢的角色關鍵詞
        '''
        self._params["role"] = role

        try:
            self.step(role_management_dir,"search_role_management")
            return self
        except Exception as e:
            print("查詢角色不存在")
            raise e


    def the_role_permission_setting(self):
        '''
        點擊“權限設置”按鈕，打開權限設置頁面
        '''
        self.step(role_management_dir,"the_role_permission_setting")
        return Permission_Setting(self._driver)