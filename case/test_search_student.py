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

class Test_Search_Student:

    _do_excel = Do_Excel(username_dir, 'user_s')
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
    def test_search_student_username(self, data):
        '''
        查找學生數量，驗證賬號存在
        '''
        result = self.main.goto_unified_data(). \
            goto_user().goto_student(). \
            search_user_s(data.username).\
            get_the_fir_row_text(data.username)

        assert True == result

    @pytest.mark.parametrize("data", _cases)
    def test_get_staffNo_for_search_username(self, data):
        '''
        查找學生賬號，返回學生學號
        '''
        try:
            result = self.main.goto_unified_data(). \
                goto_user().goto_student(). \
                search_user_s(data.username).get_the_first_staffNo(data.username)
            db = shelve.open("staffNo_s")
            self._do_excel.write_excel(data.id + 1, 3,db["staffNo_s"])
            db.close()
            assert True == result
        except AssertionError as e:
            self._do_excel.write_excel(data.id + 1, 3,'None')
            raise e