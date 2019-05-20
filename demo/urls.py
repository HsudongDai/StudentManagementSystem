"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
# from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from app import function

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path(r'', xadmin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('home/', function.home),
    path('', function.newHome),
    path('rootMenu/', function.rootMenu),
    path('score/', function.score),
    path('course/', function.course),

    path('checkCourses/', function.checkCourses),
    path('checkStudent/', function.checkStudent),
    path('checkStudentInfo/', function.checkStudentInfo),
    path('checkSelections/', function.checkSelections),
    path('checkScore/', function.checkScore),

    path('getAverageScore/', function.getAverageScore),
    path('getClassAverageScore/', function.getClassAverageScore),
    path('getCourseSelectAndScore/', function.getCourseSelectAndScore),
    path('getLevelAverageScore/', function.getLevelAverageScore),

    path('alter/', function.alter),
    path('alterStudent/', function.alterStudent),
    path('alterCourse/', function.alterCourse),
    path('alterSelection/', function.alterSelection),

]

urlpatterns += staticfiles_urlpatterns()