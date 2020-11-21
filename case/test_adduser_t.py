import pytest
from page.main import Main

def test_create_data():
    '''
    生成列表數據：1.列表生成器
    '''
    data = (("0924測試0"+str(x),
             "0924ceshi0"+str(x),
             "202009240" +str(x),
             "test09240" +str(x),
             "259",
             "23",
             "大學基金會(MUSTF)",
             "1509853",
             "123",
             "添加用戶成功！") for x in range(1,3))
    return data

class Test_AddUser_t:

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

    def teardown(self):
        '''
        開啓調試端口啓用
        '''
        self.main = Main().close_adduser_pop()

    @pytest.mark.parametrize("name,enname,staffno,"
                             "username_t,""port_id,email,group,tel,"
                             "groupSortOrder,expect", test_create_data())
    def test_add_user(self, name,enname,staffno,
                             username_t,port_id,email,group,tel,
                             groupSortOrder,expect):
        '''
        驗證添加教職工
        '''
        result = self.main.goto_unified_data().goto_user().\
            goto_teacher().goto_add_user_t().click_add().name(name).\
            enname(enname).staffno(staffno).username(username_t).\
            port(port_id).email(email).group(group).tel(tel).\
            groupSortOrder(groupSortOrder).submit().get_adduser_succeed()
        assert result == expect

