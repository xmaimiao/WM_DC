import shelve

from common.contants import student_dir
from page.Unified_dataPage.studentPage.edit_user_s import Edit_User_S
from page.basepage import BasePage


class Student(BasePage):
    def search_user_s(self, user_s):
        '''
        查詢學生
        :param user_s: 賬號
        '''
        self._params["user_s"] = user_s
        self.step(student_dir, "search_user_s")
        return self


    def edit_she_first_user_s(self):
        '''
        用戶管理第一行數據，點擊”編輯“按鈕
        '''
        try:
            self.step(student_dir, "edit_the_first_user_s")
            return Edit_User_S(self._driver)
        except Exception as e:
            print("学生不存在")
            raise e

    def get_the_first_user_s_post(self,user_s):
        '''
        獲取第一行用戶的崗位
        '''
        self._params["user_s"] = user_s
        return self.step(student_dir, "get_the_first_user_s_post")

    def get_add_ele(self):
        '''
        獲取”添加用戶“按鈕
        '''
        return self.step(student_dir, "get_add_ele")

    def get_current_total(self):
        '''
        獲取當前頁面的數據量
        '''
        return self.step(student_dir, "get_current_total")

    def get_the_first_username(self,user_s):
        '''
        獲取第一行數據的賬號
        '''
        self._params["user_s"] = user_s
        result = self.step(student_dir, "get_the_first_username")
        return result


    def get_the_first_staffNo(self,user_s):
        '''
        獲取第一行數據的學號
        '''
        self._params["user_s"] = user_s
        try:
            db = shelve.open("staffNo_s")
            staffNo_s = str(self.step(student_dir,"get_the_first_staffNo"))
            db["staffNo_s"] = staffNo_s
            db.close()
            print(f"{user_s}該學生學號為：{staffNo_s}")
            return True
        except Exception as e:
            print("暫無數據！")
            return False

    def get_not_data_text(self,user_s):
        '''
        獲取無數據時的顯示語：表中數據為空
        '''
        self._params["user_s"] = user_s
        return  self.step(student_dir,"get_not_data_text")

    def get_the_fir_row_text(self,user_s):
        '''
        验证查找学生学号
        无数据时：表中數據為空 返回False
        '''
        self._params["user_s"] = user_s
        result_none = (self.step(student_dir,"get_the_fir_row_text")).text
        if result_none == "表中數據為空":
            return False
        else:
            return True