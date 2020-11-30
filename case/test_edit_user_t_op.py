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
        test_edit_post_name_user_t_datas = datas["test_edit_post_name_user_t"]
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
        def teardown(self):
            '''
            開啓調試端口啓用
            '''
            try:
                self.main.close_drawer()
            except Exception as e:
                pass
    else:
        def setup_class(self):
            '''
            非調試端口用
            '''
            self.main = Main().goto_login(). \
                username(self._setup_datas["username"]).password(self._setup_datas["password"]).save()


        def teardown(self):
            '''
            關閉抽屜
            :return:
            '''
            try:
                self.main.close_drawer()
            except Exception as e:
                pass

        def teardown_class(self):
            '''
            非調試端口啓用
            '''
            self.main.close()

    @pytest.mark.parametrize("data", test_edit_post_user_t_datas)
    def test_edit_post_user_t(self, data):
        '''
        DC设置岗位,注意uat更改崗位前要等待>=9s，dev等待1s,传参是岗位id
        '''
        result = self.main.goto_unified_data().\
            goto_user().goto_teacher().\
            search_user_t(data["user_t"]).\
            edit_the_first_user_t(data["user_t"]).wait_sleep(9).\
            edit_post(data["post_id"],data["post"]).\
            click_save().get_the_first_user_t_post(data["user_t"])
        assert  data["post"] in result

    @pytest.mark.parametrize("data", test_edit_post_name_user_t_datas)
    def test_edit_post_name_user_t(self, data):
        '''
        DC设置岗位,注意uat更改崗位前要等待>=9s，dev等待1s,传参是岗位名称
        '''
        result = self.main.goto_unified_data().\
            goto_user().goto_teacher().\
            search_user_t(data["user_t"]).\
            edit_the_first_user_t(data["user_t"]).wait_sleep(10).\
            edit_post_name(data["post_name"]).\
            click_save().get_the_first_user_t_post(data["user_t"])
        for post in data["post_name"]:
            assert  post not in result


    @pytest.mark.parametrize("data", test_edit_leave_type_user_t_datas)
    def test_edit_leave_type_user_t(self, data):
        '''
        DC设置休假类型
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
        DC修改登錄密碼,uat打開編輯頁面等待元素出現需要>8s
        '''
        result = self.main.goto_unified_data(). \
            goto_user().goto_teacher(). \
            search_user_t(data["user_t"]). \
            edit_the_first_user_t(data["user_t"]). \
            wait_sleep(10).edit_password(self._setup_datas["password"]). \
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
        注意：uat打開抽屜定位到元素需要等待5s以上，若在獲取郵箱前等待，則獲取郵箱后無需等待
        '''
        result = self.main.goto_unified_data(). \
            goto_user().goto_teacher(). \
            search_user_t(data["user_t"]). \
            view_the_first_user_t(data["user_t"]). \
            wait_sleep(8).get_email(). \
            close_page().get_the_first_user_t_user(data["user_t"])
        assert data["user_t"] in result


    @pytest.mark.parametrize("data", test_get_post_t_datas)
    def test_get_post_t(self, data):
        '''
        DC獲取人員崗位
        '''
        result = self.main.goto_unified_data(). \
            goto_user().goto_teacher(). \
            search_user_t(data["user_t"]). \
            get_the_first_user_t_post(data["user_t"])
        assert data["expect"] in result