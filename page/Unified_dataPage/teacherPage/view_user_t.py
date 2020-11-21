import shelve

from common.contants import view_user_t_dir
from page.basepage import BasePage


class View_User_T(BasePage):

    def wait_sleep(self,sleeps):
        self.sleep(sleeps)
        return self

    def get_email(self):
        '''
        获取教师系统邮箱
        '''
        db = shelve.open("email_t")
        email_t = self.step(view_user_t_dir, "get_email")
        db["email_t"] = email_t
        db.close()
        print(f'用户的邮箱：{email_t}')
        return self

    def close_page(self):
        '''
        关闭抽屉页
        '''
        self.step(view_user_t_dir, "close_page")
        from page.Unified_dataPage.teacherPage.teacher import Teacher
        return Teacher(self._driver)