# -*- coding: utf-8 -*-
from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


def test_tid(tid):
    if len(str(tid)) != 6:
        raise ValidationError('教师工号长度必须为6位！')


class Teachers(models.Model):
    tid = models.BigIntegerField(verbose_name='教师工号', blank=False, primary_key=True)
    tname = models.CharField(verbose_name='教师姓名', max_length=50, blank=False)


    class Meta:
        verbose_name = '教师信息'
        verbose_name_plural = '教师信息'

    def __str__(self):
        return self.tname


def test_class_id(id):
    if len(str(id)) != 13:
        raise ValidationError("长度必须为13位")


class Class(models.Model):
    class_id = models.BigIntegerField(verbose_name="班级编号",primary_key=True,validators=[test_class_id])
    class_name = models.CharField(verbose_name='班级', max_length=100)
    headmaster = models.OneToOneField(Teachers, verbose_name='班主任', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = '班级'
        verbose_name_plural = '班级'

    def __str__(self):
        return self.class_name


#cancelYear = [0]
#bestYear = [0]
#chooseYear = [0]


def test_cid(cid):
    if len(cid) != 7:
        raise ValidationError("课程编号长度必须为7位！")


class Subjects(models.Model):
    cid = models.CharField(verbose_name=u"课程编号", max_length=7, validators=[test_cid], primary_key=True)
    cname = models.CharField(verbose_name='课程名称', max_length=50, blank=True)
    tname = models.CharField(verbose_name="授课教师", max_length=10)
    credit = models.IntegerField(verbose_name='学分', blank=True)
    bestSemester = models.IntegerField(verbose_name="推荐选课学期")
    openTill = models.IntegerField(verbose_name="开课年份", blank=True, default=2019)

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = '课程信息'

    def __str__(self):
        return self.cname


def test_sid(sid):
    if len(str(sid)) != 10:
        raise ValidationError(u"学号必须为10位数字")


def test_age(age):
    if age < 10 or age > 45:
        raise ValidationError(u"入学年龄必须在10~45岁之间！")


class Students(models.Model):
    SEX = (
        ('male', '男'),
        ('female', '女')
    )
    sid = models.BigIntegerField(verbose_name='学号', validators=[test_sid], primary_key=True)
    sname = models.CharField(verbose_name='学生姓名', max_length=50)
    sex = models.CharField(choices=SEX, verbose_name='性别', max_length=50)
    age = models.IntegerField(verbose_name='年龄', validators=[test_age])
    address = models.CharField(verbose_name='家庭住址', max_length=250, blank=True)
    enter_date = models.DateField(verbose_name='入学时间')
    remarks = models.TextField(verbose_name='备注', blank=True)
    subjects = models.ManyToManyField(Subjects, verbose_name='选修课程', blank=True)
    # grade_name = models.ForeignKey(Grade, verbose_name='所在年级', on_delete=models.CASCADE, blank=True, null=True)
    class_name = models.ForeignKey(Class, verbose_name='所在班级', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = '学生信息'

    def __str__(self):
        return self.sname


cancelYear = [0]
bestYear = [0]
chooseYear = [0]
grade = [0]


def test_proper_year(year):
    cancelYear = Subjects.objects.filter(cid=year)[0].openTill
    bestYear = Subjects.objects.filter(cid=year)[0].bestSemester


def test_choose_year(year):
    chooseYear[0] = year


'''def test_suit_grade(grade):
    grade[0] = Students.objects.filter(sid=grade)[0].enter_date
'''

def test_complex():
    if cancelYear[0] <= chooseYear[0] and grade[0] <= bestYear[0]:
        raise ValidationError('该课程已经取消')
    elif grade[0] > bestYear[0] and cancelYear[0] > chooseYear[0]:
        raise ValidationError('该课程不适合当前您所在的年级')
    elif cancelYear[0] <= chooseYear[0] and grade[0] > bestYear[0]:
        raise ValidationError("1.该课程已取消；2.该课程不适合您当前年级")
    else:
        pass


class Curriculum(models.Model):
    record_id = models.AutoField(verbose_name='选课记录编号', primary_key=True)
    choose_year = models.IntegerField(verbose_name='选课年份', validators=[test_choose_year],default=2019)
    sid = models.ForeignKey(verbose_name="学生", to='Students', to_field='sid',
                            on_delete=models.CASCADE)
    cid = models.ForeignKey(verbose_name='课程名', to='Subjects', to_field='cid', null=True,
                            on_delete=models.SET_NULL, validators=[test_proper_year])
    tid = models.ForeignKey(verbose_name='教师', to='Teachers', to_field='tid', null=True,
                            on_delete=models.SET_NULL)
    score = models.IntegerField(verbose_name="成绩", default=0, blank=True, null=True, validators=[])

    class Meta:
        unique_together = ['sid', 'cid', 'choose_year']
        verbose_name = "选课信息"
        verbose_name_plural = "选课信息"

    def __str__(self):
        return self.sid.sname + "选课信息"
