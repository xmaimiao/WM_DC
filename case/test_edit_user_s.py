import pytest
import yaml
from common.contants import test_edit_user_s_dir, basepage_dir
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

class Test_Edit_User_S:
    with open(test_edit_user_s_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        test_edit_password_user_s_datas = datas["test_edit_password_user_s"]
        test_edit_other_msg_s_datas = datas["test_edit_other_msg_s"]
        test_search_student_username_datas = datas["test_search_student_username"]
        test_edit_post_and_faculy_datas = datas["test_edit_post_and_faculy"]
        test_edit_user_and_staffNo_datas = datas["test_edit_user_and_staffNo"]
        test_edit_user_datas = datas["test_edit_user"]


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
            判斷，若抽屜沒關閉，則先關閉抽屜在進行下一個用例，否則會導致後續用例失敗
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

    @pytest.mark.parametrize("data", test_edit_password_user_s_datas)
    def test_edit_password_user_s(self, data):
        '''
        DC修改登錄密碼
        '''
        result = self.main.goto_unified_data(). \
            goto_user().goto_student(). \
            search_user_s(data["user_s"]). \
            edit_she_first_user_s(data["user_s"]). \
            edit_password(self._setup_datas["password"]).\
            edit_sortOrder(data["sortorder"]).\
            click_save().get_add_ele()
        assert data["expect"] == result

    @pytest.mark.parametrize("data", test_edit_post_and_faculy_datas)
    def test_edit_post_and_faculy(self, data):
        '''
        DC修改崗位和學院
        '''
        result = self.main.goto_unified_data(). \
            goto_user().goto_student(). \
            search_user_s(data["user_s"]). \
            edit_she_first_user_s(data["user_s"]).edit_post_s(data["post_id"]).\
            edit_faculy(data["faculy_id"]).click_save().get_add_ele()
        assert data["expect"] == result

    @pytest.mark.parametrize("data", test_search_student_username_datas)
    def test_search_student_username(self, data):
        '''
        查找學生數量，驗證賬號存在
        '''
        result = self.main.goto_unified_data(). \
            goto_user().goto_student(). \
            search_user_s(data["user_s"]). \
            get_the_first_staffNo(data["user_s"])
        assert data["user_s"] == result

    @pytest.mark.parametrize("data", test_edit_user_and_staffNo_datas)
    def test_edit_user_and_staffNo(self, data):
        '''
        DC修改賬號和學號
        '''
        result = self.main.goto_unified_data(). \
            goto_user().goto_student(). \
            search_user_s(data["user_s"]). \
            edit_she_first_user_s(data["user_s"]).edit_post_s(data["post_id"]). \
            edit_faculy(data["faculy_id"]).edit_name(data["name"]).edit_enname(data["enname"]). \
            edit_user(data["user"]).edit_password(data["psd"]).edit_sortOrder(data["sortOrder"]). \
            edit_staffNo(data["staffNo"]).edit_type_of_accommodation(). \
            edit_program(data["program"]).edit_programCode(data["programCode"]).\
            edit_entrance_term(data["entrance_term"]).edit_entrance_date(data["entrance_date"]).\
            click_save().get_not_data_text(data["user"])
        return result == data["expect"]

    @pytest.mark.parametrize("data", test_edit_user_datas)
    def test_edit_user(self, data):
        '''
        DC修改
        '''
        result = self.main.goto_unified_data(). \
            goto_user().goto_student(). \
            search_user_s(data["user_s"]). \
            edit_she_first_user_s(data["user_s"]).edit_post_s(data["post_id"]). \
            edit_faculy(data["faculy_id"]).edit_password(data["psd"]).edit_sortOrder(data["sortOrder"]). \
            edit_type_of_accommodation(). \
            edit_program(data["program"]).edit_programCode(data["programCode"]).\
            edit_entrance_term(data["entrance_term"]).edit_entrance_date(data["entrance_date"]).\
            click_save().get_the_first_username(data["user_s"])
        return result == data["expect"]





