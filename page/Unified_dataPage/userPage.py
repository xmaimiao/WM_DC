from common.contants import userPage_dir
from page.Unified_dataPage.studentPage.student import Student
from page.Unified_dataPage.teacherPage.teacher import Teacher
from page.basepage import BasePage


class User(BasePage):
    def goto_teacher(self):
        '''
        打開”教職工“界面
        '''
        self.step(userPage_dir,"goto_teacher")
        return Teacher(self._driver)

    def goto_student(self):
        '''
        打開”學生“界面
        '''
        self.step(userPage_dir,"goto_student")
        return Student(self._driver)