# from django.contrib import admin
import xadmin
from .models import *
from xadmin.views.website import LoginView
from xadmin import views


class GlobalSettings(object):
    site_title = '天津大学学生信息管理系统'
    site_header = '天津大学学生信息管理系统登录页面'
    site_footer = 'Copyright™ 2019 - now, Hsudong Dai'
    menu_style = 'accordion'  # 左边导航栏 收缩 手风琴


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True  # 调出主题菜单


class LoginViewAdmin(LoginView):
    title = '天津大学学生信息管理系统'


class StudentsAdmin(object):
    list_display = {'sex', 'age','sid','sname' ,'class_name', }
    style_fields = {'subjects': 'checkbox-inline', }
    search_fields = {'sname'}
    list_fields = {'sex', 'sid', 'class_name__class_id'}
    model_icon = 'fa fa-id-card'
    ordering = {'sid'}


class TeachersAdmin(object):
    list_display = {'tid', 'tname'}
    model_icon = 'fa fa-linux rotate-90'
    ordering = {'tid'}


class SubjectsAdmin(object):
    list_display = {'cid', 'cname',  'credit', 'tname', 'bestSemester', 'openTill'}
    model_icon = 'fa fa-archive'
    ordering = {'cid'}


class ClassAdmin(object):
    list_display = {'class_id', 'class_name', 'headmaster'}
    model_icon = 'fa fa-address-book-o'
    ordering = {'class_id'}


class CurriculumAdmin(object):
    list_display = {'record_id', 'choose_year', 'sid', 'cid', 'score'}
    model_icon = 'fa fa-check-square'
    ordering = {'record_id'}


xadmin.site.register(Students, StudentsAdmin)
xadmin.site.register(Teachers, TeachersAdmin)
xadmin.site.register(Subjects, SubjectsAdmin)
xadmin.site.register(Class, ClassAdmin)
xadmin.site.register(Curriculum, CurriculumAdmin)
# Register your models here.
xadmin.site.register(LoginView, LoginViewAdmin)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)
