import os
base_dir = os.path.dirname(os.path.dirname(__file__))

loginpage_dir = os.path.join(base_dir,'data/loginpage.yaml')

main1_dir = os.path.join(base_dir,'data/main1.yaml')

index_dir = os.path.join(base_dir,'data/index.yaml')

basepage_dir = os.path.join(base_dir,'data/basepage.yaml')

# 统一数据
unified_dataPage_dir = os.path.join(base_dir,'data/Unified_dataPage/unified_dataPage.yaml')

userPage_dir = os.path.join(base_dir,'data/Unified_dataPage/userPage.yaml')

teacher_dir = os.path.join(base_dir,'data/Unified_dataPage/teacherPage/teacher.yaml')

adduser_t_dir = os.path.join(base_dir,'data/Unified_dataPage/teacherPage/adduser_t.yaml')

edit_user_t_dir = os.path.join(base_dir,'data/Unified_dataPage/teacherPage/edit_user_t.yaml')

view_user_t_dir = os.path.join(base_dir,'data/Unified_dataPage/teacherPage/view_user_t.yaml')

student_dir = os.path.join(base_dir,'data/Unified_dataPage/studentPage/student.yaml')

edit_user_s_dir = os.path.join(base_dir,'data/Unified_dataPage/studentPage/edit_user_s.yaml')



# case
test_adduser_t_dir = os.path.join(base_dir,'data/case/Unified_dataPage/test_adduser_t.yaml')

test_edit_user_t_dir = os.path.join(base_dir,'data/case/Unified_dataPage/test_edit_user_t.yaml')

test_edit_user_s_dir = os.path.join(base_dir,'data/case/Unified_dataPage/test_edit_user_s.yaml')

test_search_student_dir = os.path.join(base_dir,'data/case/Unified_dataPage/test_search_student.yaml')

test_user_t_post_and_psd_dir = os.path.join(base_dir,'data/case/Unified_dataPage/test_user_t_post_and_psd.yaml')


# 统一授权

unified_authorizationPage_dir = os.path.join(base_dir,'data/unified_authorization/unified_authorizationPage.yaml')

role_management_dir = os.path.join(base_dir,'data/unified_authorization/role_management.yaml')

permission_setting_dir = os.path.join(base_dir,'data/unified_authorization/permission_setting.yaml')

platform_for_academia_service_dir = os.path.join(base_dir,'data/unified_authorization/platform_for_academia_service.yaml')

examPC_dir = os.path.join(base_dir,'data/unified_authorization/examPC.yaml')

# case
test_exam_authorization_setting_dir = os.path.join(base_dir,'data/case/unified_authorization/test_exam_authorization_setting.yaml')

# excel
username_dir = os.path.join(base_dir,'excel/username.xlsx')







class TestPath:
    def test_path(self):
        print(loginpage_dir)