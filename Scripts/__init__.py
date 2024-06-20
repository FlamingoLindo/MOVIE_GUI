# MOVIE COMPANY
from Scripts.MOVIE.Master.account.createAccount import create_account_master_func
from Scripts.MOVIE.Master.configs.configAll import config_master_func
from Scripts.MOVIE.Master.courses.createApprovePublishCourse import create_app_pub_func
from Scripts.MOVIE.Master.courses.approveCourse import approve_course_func
from Scripts.MOVIE.Master.courses.createApprovePublishCourse2 import create_app_pub_input_func
from Scripts.MOVIE.Master.courses.createCourse import create_course_func
from Scripts.MOVIE.Master.courses.deleteCourse import delete_course_func
from Scripts.MOVIE.Master.courses.duplicate import duplicate_course_func
from Scripts.MOVIE.Master.imports.affiliates import import_affiliate_list_func
from Scripts.MOVIE.Master.imports.aluno import import_student_list_func
from Scripts.MOVIE.Master.imports.teacher import import_teacher_list_func
from Scripts.MOVIE.Master.account.fullAccountCreation import full_account_creation_master
from Scripts.MOVIE.load_paths import load_chromedriver
from Scripts.MOVIE.load_paths import load_aff_xlsx
from Scripts.MOVIE.load_paths import load_pro_xlsx
from Scripts.MOVIE.load_paths import load_stu_xlsx

# MOVIE STUDENT
from Scripts.MOVIE.Student.account.createAccount import create_student_account_func
from Scripts.MOVIE.Student.account.preparingAccount import prep_account_client_func
from Scripts.MOVIE.Student.courses.buyCourse import buy_course_func
from Scripts.MOVIE.Student.courses.doCourse import do_course_func

# MOVIE PROFESSOR
from Scripts.MOVIE.Professor.account.createAccount import create_account_professor
from Scripts.MOVIE.Professor.courses.deleteCourse import delete_course_teacher_func
from Scripts.MOVIE.Professor.courses.profCreateCourse import create_course_professor_func

# MOVIE AFFILIATE
from Scripts.MOVIE.Affiliate.createAccount import create_affiliate_account_func
from Scripts.MOVIE.Affiliate.CreateAffiliateRequest import create_affiliate_request_func
