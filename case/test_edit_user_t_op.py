import pytest
import yaml
from common.contants import test_edit_user_t_dir, basepage_dir
from page.basepage import _get_working
from page.main import Main

def get_env():
    '''
    获取环境变量：uat、dev、mo正式站
    '''
    with open(basepage_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        wm_env = datas["default"]
        setup_datas = datas[wm_env]
        return setup_datas

class Test_Edit_User_T:
    with open(test_edit_user_t_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        test_edit_post_user_t_datas = datas["test_edit_post_user_t"]
        test_edit_leave_type_user_t_datas = datas["test_edit_leave_type_user_t"]
        test_edit_leave_info_user_t_datas = datas["test_edit_leave_info_user_t"]
        test_edit_password_user_t_datas = datas["test_edit_password_user_t"]
        test_edit_email_t_datas = datas["test_edit_email_t"]
        test_get_email_t_datas = datas["test_get_email_t"]
        test_get_post_t_datas = datas["test_get_post_t"]
    _setup_datas = get_env()
    _working = _get_working()
    if _working == "port":
        def setup(self):
            '''
            開啓調試端口啓用
            '''
            self.main = Main()
    else:
        def setup_class(self):
            '''
            非調試端口用
            '''
            self.main = Main().goto_login(). \
                username(self._setup_datas["username"]).password(self._setup_datas["password"]).save()

        def teardown_class(self):
            '''
            非調試端口啓用
            '''
            self.main.close()

    @pytest.mark.parametrize("data", test_edit_post_user_t_datas)
    def test_edit_post_user_t(self, data):
        '''
        DC设置岗位,注意uat更改崗位前要等待>=5s，dev等待1s
        '''
        result = self.main.goto_unified_data().\
            goto_user().goto_teacher().\
            search_user_t(data["user_t"]).\
            edit_the_first_user_t(data["user_t"]).wait_sleep(5).\
            edit_post(data["post_id"],data["post"]).\
            click_save().get_the_first_user_t_post(data["user_t"])
        assert  data["post"] in result


    @pytest.mark.parametrize("data", test_edit_leave_type_user_t_datas)
    def test_edit_leave_type_user_t(self, data):
        '''
        DC设置休假类型(最好請假應用中設置，若存在包含關係則DC會設置出錯)
        '''
        result = self.main.goto_unified_data(). \
            goto_user().goto_teacher(). \
            search_user_t(data["user_t"]). \
            edit_the_first_user_t(data["user_t"]). \
            edit_leave_type(data["leave_type"]).\
            click_save().get_the_first_user_t_post(data["user_t"])
        assert data["expect"] in result


    @pytest.mark.parametrize("data", test_edit_leave_info_user_t_datas)
    def test_edit_leave_info_user_t(self, data):
        '''
        DC设置岗位、入职日期，合同期
        '''
        result = self.main.goto_unified_data(). \
            goto_user().goto_teacher(). \
            search_user_t(data["user_t"]). \
            edit_the_first_user_t(data["user_t"]). \
            edit_post(data["post_id"], data["post"]). \
            edit_date_of_entry(data["entrydate"]).\
            edit_contract_start_date(data["contract_start_date"]).\
            edit_contract_end_date(data["contract_end_date"]).\
            click_save().get_the_first_user_t_post(data["user_t"])
        assert data["expect"] in result


    @pytest.mark.parametrize("data", test_edit_password_user_t_datas)
    def test_edit_password_user_t(self, data):
        '''
        DC修改登錄密碼
        '''
        result = self.main.goto_unified_data(). \
            goto_user().goto_teacher(). \
            search_user_t(data["user_t"]). \
            edit_the_first_user_t(data["user_t"]). \
            edit_password(data["reset_psd"]).\
            click_save().get_the_first_user_t_user(data["user_t"])
        assert data["expect"] == result

    @pytest.mark.parametrize("data", test_edit_email_t_datas)
    def test_edit_email_t(self, data):
        '''
        DC修改系统邮箱
        '''
        result = self.main.goto_unified_data(). \
            goto_user().goto_teacher(). \
            search_user_t(data["user_t"]). \
            edit_the_first_user_t(data["user_t"]). \
            edit_email(data["email"]).\
            click_save().get_the_first_user_t_user(data["user_t"])
        assert data["user_t"] in result

    @pytest.mark.parametrize("data", test_get_email_t_datas)
    def test_get_email_t(self, data):
        '''
        DC获取系统邮箱
        '''
        result = self.main.goto_unified_data(). \
            goto_user().goto_teacher(). \
            search_user_t(data["user_t"]). \
            view_the_first_user_t(data["user_t"]). \
            get_email(). \
            close_page().get_the_first_user_t_user(data["user_t"])
        assert data["user_t"] in result

    @pytest.mark.parametrize("data", test_get_post_t_datas)
    def test_get_post_t(self, data):
        '''
        DC获取系统邮箱
        '''
        result = self.main.goto_unified_data(). \
            goto_user().goto_teacher(). \
            search_user_t(data["user_t"]). \
            get_the_first_user_t_post(data["user_t"])
        assert data["expect"] in result