from common.contants import adduser_t_dir
from page.basepage import BasePage


class AddUser_t(BasePage):
    def click_add(self):
        '''
        點擊“添加用戶
        '''
        self.step(adduser_t_dir,"click_add")
        return self

    def name(self,name):
        '''
        填寫姓名
        '''
        self._params["name"] = name
        self.step(adduser_t_dir,"name")
        return self

    def enname(self,enname):
        '''
        填寫英文名
        '''
        self._params["enname"] = enname
        self.step(adduser_t_dir, "enname")
        return self

    def staffno(self,staffno):
        '''
        填寫學號
        '''
        self._params["staffno"] = staffno
        self.step(adduser_t_dir,"staffno")
        return self

    def username(self,username):
        '''
        填寫賬號
        '''
        self._params["username"] = username
        self.step(adduser_t_dir,"username")
        return self

    def port(self,port_id):
        '''
        填寫崗位
        '''
        self._params["port_id"] = port_id
        self.step(adduser_t_dir,"port")
        return self

    def email(self,email):
        '''
        填寫郵箱
        '''
        self._params["email"] = email
        self.step(adduser_t_dir,"email")
        return self

    def group(self,group):
        '''
        填寫部門
        '''
        self._params["group"] = group
        self.step(adduser_t_dir,"group")
        return self

    def tel(self,tel):
        '''
        填寫電話
        '''
        self._params["tel"] = tel
        self.step(adduser_t_dir,"tel")
        return self

    def groupSortOrder(self,groupSortOrder):
        '''
        填寫部門排序
        '''
        self._params["groupSortOrder"] = groupSortOrder
        self.step(adduser_t_dir,"groupSortOrder")
        return self

    def submit(self):
        '''
        點擊確認
        '''
        self.step(adduser_t_dir,"submit")
        return self

    def get_adduser_succeed(self):
        return self.step(adduser_t_dir,"get_adduser_succeed")

    def search_keywords(self,keywords):
        '''
        查詢關鍵字
        '''
        self._params["keywords"] = keywords
        self.step(adduser_t_dir,"search_keywords")
        return self

    def get_current_teacher_num(self):
        '''
        獲取當前頁面教職工人數
        '''
        return self.step(adduser_t_dir,"get_current_teacher_num")



