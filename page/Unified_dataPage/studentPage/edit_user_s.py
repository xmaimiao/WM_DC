from common.contants import edit_user_s_dir
from page.basepage import BasePage


class Edit_User_S(BasePage):
    def edit_password(self,reset_psd):
        '''
        修改登陸密碼
        '''
        self._params["reset_psd"] = reset_psd
        self.step(edit_user_s_dir,"edit_password")
        return self

    def edit_name(self,name):
        '''
        修改姓名
        '''
        self._params["name"] = name
        self.step(edit_user_s_dir,"edit_name")
        return self

    def edit_enname(self,enname):
        '''
        修改英文姓名
        '''
        self._params["enname"] = enname
        self.step(edit_user_s_dir,"edit_enname")
        return self

    def edit_staffNo(self,staffNo):
        '''
        修改學號
        '''
        self._params["staffNo"] = staffNo
        self.step(edit_user_s_dir,"edit_staffNo")
        return self

    def edit_user(self,user):
        '''
        修改賬號
        '''
        self._params["user"] = user
        self.step(edit_user_s_dir,"edit_user")
        return self

    def edit_post_s(self,post_id):
        '''
        修改崗位，默認選中“學生”
        '''
        self._params["post_id"] = post_id
        get_post = self.step(edit_user_s_dir,"get_post")
        if '生' not in get_post :
            self.step(edit_user_s_dir,"edit_post_s")
        else:
            pass
        return self


    def edit_faculy(self,faculy_id):
        '''
        修改學院，默認選中“資訊科技學院”
        '''
        self._params["faculy_id"] = faculy_id
        # 先獲取學院，若學院沒值則輸入學院
        get_faculy = self.step(edit_user_s_dir,"get_faculy")
        if get_faculy == "請選擇":
            self.step(edit_user_s_dir,"edit_faculy")
        else:
            pass
        return self

    def edit_program(self,program):
        '''
        修改課程
        '''
        self._params["program"] = program
        get_program = (self.step(edit_user_s_dir,"get_program")).get_attribute('value')
        if get_program:
            pass
        else:
            self.step(edit_user_s_dir,"edit_program")
        return self

    def edit_programCode(self,programCode):
        '''
        修改課程編碼
        '''
        self._params["programCode"] = programCode
        get_programCode = (self.step(edit_user_s_dir,"get_programCode")).get_attribute('value')
        if get_programCode:
            pass
        else:
            self.step(edit_user_s_dir,"edit_programCode")
        return self

    def edit_entrance_term(self,entrance_term):
        '''
        修改入學學期
        '''
        self._params["entrance_term"] = entrance_term
        get_entrance_term = (self.step(edit_user_s_dir,"get_entrance_term")).get_attribute("title")
        if get_entrance_term == " 请选择":
            self.step(edit_user_s_dir,"edit_entrance_term")
        else:
            pass
        return self

    def edit_entrance_date(self,entrance_date):
        '''
        修改入學日期
        '''
        self._params["entrance_date"] = entrance_date
        get_entrance_date =(self.step(edit_user_s_dir,"get_entrance_date")).get_attribute('value')
        # 注意獲取日期，判斷不爲空則跳過，必須寫上“ ！=‘’ ”，判斷輸入框的值則不需要
        if get_entrance_date !='' and get_entrance_date is not None:
            pass
        else:
            self.step(edit_user_s_dir,"edit_entrance_date")
        return self

    def edit_type_of_accommodation(self):
        '''
        修改宿舍類型，默認選中“非住宿生”
        '''
        self.step(edit_user_s_dir,"edit_type_of_accommodation")
        return self

    def edit_sortOrder(self,sortorder):
        '''
        添加排序，必填項
        '''
        self._params["sortorder"] = sortorder
        sort = (self.step(edit_user_s_dir,"get_sortOrder")).get_attribute('value')
        print(f"sort:{sort}")
        if sort != '':
            pass
        else:
            self.step(edit_user_s_dir,"edit_sortOrder")
        return self

    def click_save(self):
        try:
            self.step(edit_user_s_dir,"click_save")
        except Exception as e:
            raise e
        finally:
            from page.Unified_dataPage.studentPage.student import Student
            return Student(self._driver)