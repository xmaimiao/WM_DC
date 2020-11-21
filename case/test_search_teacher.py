import shelve

import pytest
import yaml
from common.contants import basepage_dir, username_dir
from common.do_excel import Do_Excel
from page.basepage import _get_working
from page.main import Main

#获取环境变量
def get_env():
    '''
    获取环境变量：uat、dev、mo正式站
    '''
    with open(basepage_dir, encoding="utf-8") as f:
        datas =  yaml.safe_load(f)
        wm_env =  datas["default"]
        setup_datas = datas[wm_env]
        return setup_datas

class Test_Search_Teacher:

    _do_excel = Do_Excel(username_dir, 'user_t')
    _cases = _do_excel.read_excel()
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
            try:
                self.main.close_drawer()
            except Exception as e:
                pass

        def teardown_class(self):
            '''
            非調試端口啓用
            '''
            self.main.close()

    @pytest.mark.parametrize("data", _cases)
    def test_search_teacher_username(self, data):
        '''
        查找老師數量，驗證賬號存在
        '''
        result = self.main.goto_unified_data(). \
            goto_user().goto_teacher(). \
            search_user_t(data.username).\
            get_the_fir_row_text(data.username)

        assert True == result

    @pytest.mark.parametrize("data", _cases)
    def test_get_post_for_search_username(self, data):
        '''
        查找老師賬號，返回老師崗位
        '''
        try:
            result = self.main.goto_unified_data(). \
                goto_user().goto_teacher(). \
                search_user_t(data.username).get_the_first_user_t_post(data.username)
            db = shelve.open("post_t")
            self._do_excel.write_excel(data.id + 1, 3, db["post_t"])
            db.close()
            assert "崗位" in result
        except AssertionError as e:
            self._do_excel.write_excel(data.id + 1, 3,'None')
            raise e

    @pytest.mark.parametrize("data", _cases)
    def test_get_emali_for_search_username(self, data):
        '''
        查找老師賬號，返回老師崗位
        注意：uat打開抽屜定位到元素需要等待5s以上，若在獲取郵箱前等待，則獲取郵箱后無需等待
        '''
        try:
            result = self.main.goto_unified_data(). \
                goto_user().goto_teacher(). \
                search_user_t(data.username).view_the_first_user_t(data.username).\
                wait_sleep(5).get_email().close_page().get_the_first_user_t_user(data.username)
            db = shelve.open("email_t")
            self._do_excel.write_excel(data.id + 1, 4, db["email_t"])
            db.close()
            assert data.username in result
        except AssertionError as e:
            self._do_excel.write_excel(data.id + 1, 4, 'None')
            raise e