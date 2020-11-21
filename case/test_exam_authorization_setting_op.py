import pytest
import yaml
from common.contants import test_exam_authorization_setting_dir
from page.main import Main

class Test_Authorization_Setting:

    with open(test_exam_authorization_setting_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        setup_datas = datas["setup_datas"]
        test_exam_authorization_setting_datas = datas["test_exam_authorization_setting"]


    # def setup_class(self):
    #     '''
    #     非調試端口用
    #     '''
    #     self.main = Main().goto_login(). \
    #         username(self.setup_datas["username).password(self.setup_datas["password).save(). \
    #         goto_application(). \
    #         goto_classtimetable(self.setup_datas["application)
    #
    # def teardown_class(self):
    #     '''
    #     非調試端口啓用
    #     '''
    #     self.main.close()

    def setup(self):
        '''
        開啓調試端口啓用
        '''
        self.main = Main()

    # def teardown(self):
    #     '''
    #     開啓調試端口啓用
    #     '''
    #     self.main = Main()

    @pytest.mark.parametrize("data",test_exam_authorization_setting_datas)
    def test_exam_authorization_setting(self, data):
        '''
        '''
        result = self.main.goto_unified_authorization().\
            goto_role_management().\
            search_role_management(data["role"]).\
            the_role_permission_setting().\
            goto_Platform_For_Academia_Service().\
            goto_examPC(data["application"]).\
            give_exam_exam_plan(data["memu"]).\
            click_save(data["role"])
        assert result == data["expect"]

    