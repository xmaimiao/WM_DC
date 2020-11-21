import shelve

from common.contants import teacher_dir
from page.Unified_dataPage.teacherPage.edit_user_t import Edit_User_T
from page.Unified_dataPage.teacherPage.adduser_t import AddUser_t
from page.Unified_dataPage.teacherPage.view_user_t import View_User_T
from page.basepage import BasePage


class Teacher(BasePage):
    def goto_add_user_t(self):
        '''
        添加用戶
        '''
        self.step(teacher_dir,"goto_add_user_t")
        return AddUser_t(self._driver)


    def search_user_t(self,user_t):
        '''
        查詢教職工
        :param user_t: 教職工賬號
        '''
        self._params["user_t"] = user_t
        self.step(teacher_dir,"search_user_t")
        return self

    def edit_the_first_user_t(self,user_t):
        '''
        用戶管理第一行數據，點擊”編輯“按鈕
        '''
        try:
            self._params["user_t"] = user_t
            self.step(teacher_dir,"edit_the_first_user_t")
            return Edit_User_T(self._driver)
        except Exception as e:
            print('该用户已离职，没有”编辑“按钮')

    def view_the_first_user_t(self,user_t):
        '''
        用戶管理第一行數據，點擊”查看“按鈕
        '''
        self._params["user_t"] = user_t
        self.step(teacher_dir,"view_the_first_user_t")
        return View_User_T(self._driver)

    def get_the_first_user_t_post(self,user_t):
        '''
        通過查詢賬號，獲取第一行用戶的崗位
        '''
        self._params["user_t"] = user_t
        try:
            db = shelve.open("post_t")
            post_t =  self.step(teacher_dir,"get_the_first_user_t_post")
            db["post_t"] = post_t
            db.close()
            print(f"{user_t}的崗位是：{post_t}")
            return "崗位:" + post_t
        except Exception as e:
            print("暫無數據！")
            raise e

    def get_the_first_user_t_user(self,user_t):
        '''
        獲取第一行用戶的賬號
        '''
        self._params["user_t"] = user_t
        user_t = self.step(teacher_dir,"get_the_first_user_t_user")
        return user_t

    def get_add_ele(self):
        '''
        獲取”添加用戶“按鈕
        '''
        return self.step(teacher_dir,"get_add_ele")

    def get_the_fir_row_text(self,user_t):
        '''
        验证查找老師賬號
        无数据时：表中數據為空 返回False
        '''
        self._params["user_t"] = user_t
        result_none = (self.step(teacher_dir,"get_the_fir_row_text")).text
        if result_none == "表中數據為空":
            return False
        else:
            return True
