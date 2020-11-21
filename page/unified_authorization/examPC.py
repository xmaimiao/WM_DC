from common.contants import examPC_dir
from page.basepage import BasePage


class ExamPC(BasePage):
    def give_exam_exam_plan(self,memu):
        '''
        給予排考計劃權限
        '''
        self._params["memu"] = memu
        self.step(examPC_dir,"give_exam_exam_plan")
        return self

    def click_save(self,role):
        '''
        點擊確認
        通過確認存在搜索框驗證 回到“角色管理”界面
        '''
        self._params["role"] = role
        return self.step(examPC_dir,"click_save")