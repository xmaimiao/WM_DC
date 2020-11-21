from common.contants import platform_for_academia_service_dir
from page.basepage import BasePage
from page.unified_authorization.examPC import ExamPC


class Platform_For_Academia_Service(BasePage):
    def goto_examPC(self,application):
        '''
        打開考試PC端的權限
        '''
        self._params["application"] = application
        self.step(platform_for_academia_service_dir,"goto_examPC")
        return ExamPC(self._driver)
