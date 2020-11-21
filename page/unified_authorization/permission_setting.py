from common.contants import permission_setting_dir
from page.basepage import BasePage
from page.unified_authorization.platform_for_academia_service import Platform_For_Academia_Service


class Permission_Setting(BasePage):
    def goto_Platform_For_Academia_Service(self):
        '''
        打開教學服務平臺
        '''
        self.step(permission_setting_dir,"goto_Platform_For_Academia_Service")
        return Platform_For_Academia_Service(self._driver)

    # def goto_Platform_For_Surport_Service(self):
    #     '''
    #     打開支援服務平臺
    #     '''
    #     self.step(permission_setting_dir,"goto_Platform_For_Surport_Service")
    #     return Platform_For_Surport_Service(self._driver)