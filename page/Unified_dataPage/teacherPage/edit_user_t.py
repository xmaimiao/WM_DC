import shelve

from common.contants import edit_user_t_dir
from page.basepage import BasePage


class Edit_User_T(BasePage):

    def wait_sleep(self,sleeps):
        self.sleep(sleeps)
        return self

    def edit_post(self, post_id,post):
        '''
        添加崗位，傳進來的參數為崗位id
        '''
        self._params["post_id"] = post_id
        self._params["post"] = post
        exist_post = self.step(edit_user_t_dir, "get_exist_post")
        if post in exist_post:
            pass
        else:
            self.step(edit_user_t_dir, "edit_post")
        return self

    def edit_leave_type(self,leave_type):
        '''
        编辑休假类型,目前是傳入文本形式定位下拉框選項，僅傳入博士後會定位不準確，建議請假應用修改。
        不建議使用，存在博士後 、 博士後研究所。
        '''
        self._params["leave_type"] = leave_type
        self.step(edit_user_t_dir, "edit_leave_type")
        return self

    def edit_date_of_entry(self,entrydate):
        '''
        編輯入職日期
        :param entrydate: 入職日期
        '''
        self._params["entrydate"] = entrydate
        self.step(edit_user_t_dir,"edit_date_of_entry")
        return self


    def edit_contract_start_date(self, contract_start_date):
        '''
        編輯合同開始日期
        :param contract_start_date: 合同開始日期
        '''
        self._params["contract_start_date"] = contract_start_date
        self.step(edit_user_t_dir, "edit_contract_start_date")
        return self
    
    def edit_contract_end_date(self,contract_end_date):
        '''
        編輯合同結束日期
        :param contract_end_date: 合同結束日期
        '''
        self._params["contract_end_date"] = contract_end_date
        self.step(edit_user_t_dir,"edit_contract_end_date")
        return self

    def edit_password(self,reset_psd):
        '''
        修改登陸密碼
        '''
        self._params["reset_psd"] = reset_psd
        self.step(edit_user_t_dir,"edit_password")
        return self

    def edit_email(self,email):
        '''
        修改系统邮箱
        '''
        self._params["email"] = email
        self.step(edit_user_t_dir,"edit_email")
        return self

    def get_email(self):
        '''
        获取教师系统邮箱
        '''
        try:
            db = shelve.open("email_t")
            email_t = (self.step(edit_user_t_dir, "get_email")).get_attribute("value")
            db["email_t"] = email_t
            db.close()
            print(email_t)
        except Exception as e:
            pass
        return self

    def click_save(self):
        try:
            self.step(edit_user_t_dir,"click_save")
        except Exception as e:
            raise e
        finally:
            from page.Unified_dataPage.teacherPage.teacher import Teacher
            return Teacher(self._driver)

