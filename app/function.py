import pymysql
from django.shortcuts import render

db = pymysql.connect("localhost", "root", "990916", "stu_info")
cursor = db.cursor()


def home(request) :
    return render(request, 'home.html')


def newHome(request):
    return render(request, 'index.html')

def score(request) :
    return render(request, 'score.html')


def course(request) :
    return render(request, 'course.html')


def rootMenu(request) :
    return render(request, 'rootMenu.html')


def checkStudent(request) :
    return render(request, 'checkStudent.html')


def checkScore(request) :
    return render(request, 'checkScore.html')


def alter(request) :
    return render(request, 'alter.html')


def alterStudent(request) :
    return render(request, 'alterStudent.html')


def alterCourse(request) :
    return render(request, 'alterCourse.html')


def alterSelection(request) :
    return render(request, 'alterSelection.html')


# 取得
def checkStudentInfo(request) :
    db = pymysql.connect("localhost", "root", "990916", "stu_info")
    cursor = db.cursor()
    sid = request.GET['link']
    if '1' <= sid[0] <= '9' :
        cursor.execute(" select sname, sid, enter_date, age, "
                       " sex, address, class_name_id"
                       " from app_Students "
                       " where sid  ='%s'" % sid)
        found = cursor.fetchall()
        return render(request, 'checkStudentInfo.html', {'res' : found})
    cursor.execute(" select sname, sid, enter_date, age, "
                   " sex,address, class_name_id "
                   " from app_Student"
                   " where sname like '%%%s%%'" % sid)
    found = cursor.fetchall()
    return render(request, 'checkStudentInfo.html', {'res' : found})


def getCourseSelectAndScore(request) :
    db = pymysql.connect("localhost", "root", "990916", "stu_info")
    cursor = db.cursor()
    sid = request.GET['course_selection']
    if '9' >= sid[0] >= '1' :
        cursor.execute("select app_Students.sid,  app_Subjects.cname, app_Students.sname, app_Curriculum.score "
                       "from app_Curriculum,app_Students,app_Subjects "
                       "where app_Students.sid= %d "
                       "and app_Curriculum.sid_id=app_Students.sid "
                       "and app_Curriculum.cid_id = app_Subjects.cid" % int(sid))
        res = cursor.fetchall()
        return render(request, 'getCourseSelectAndScore.html', {'b' : res})

    cursor.execute("select app_Curriculum.sid_id, app_Students.sname, app_Subjects.cname, app_Curriculum.score "
                   "from app_Curriculum,app_Students,app_Subjects "
                   "where app_Students.sname = '%s'"
                   "and app_Curriculum.sid=app_Students.sid "
                   "and app_Curriculum.cid_id = app_Subjects.cid" % int(sid))
    res = cursor.fetchall()
    print(res)
    return render(request, 'getCourseSelectAndScore.html', {'b' : res})


def checkCourses(request) :
    db = pymysql.connect("localhost", "root", "990916", "stu_info")
    cursor = db.cursor()
    cid = request.GET['course_selection']
    if '1' <= cid[0] <= '9' :
        cursor.execute("select * "
                       "from app_Subjects "
                       "where app_Subjects.cid = %d" % int(cid))
        res = cursor.fetchall()
        return render(request, 'checkCourses.html', {'b' : res})

    cursor.execute("select * "
                   "from app_Subjects "
                   "where app_Subjects.cname = '%s'" % cid)
    res = cursor.fetchall()
    print(res)
    return render(request, 'checkCourses.html', {'b' : res})


def checkSelections(request) :
    db = pymysql.connect("localhost", "root", "990916", "stu_info")
    cursor = db.cursor()
    cid = request.GET['course_selection']
    if '1' <= cid[0] <= '9' :
        cursor.execute("select app_Students.sid, app_Students.sname, app_Subjects.cname "
                       "from app_Subjects, app_Students, app_Curriculum "
                       "where app_Curriculum.cid_id = %d "
                       "and app_Subjects.cid = app_Curriculum.cid_id "
                       "and app_Students.sid = app_Curriculum.sid_id" % int(cid))
        res = cursor.fetchall()
        return render(request, 'checkSelections.html', {'b' : res})
    cursor.execute("select app_Subjects.cname, app_Students.sid, app_Students.sname "
                   "from app_Subjects, app_Curriculum, app_Students "
                   "where app_Subjects.cname = '%s'"
                   "and app_Students.sid = app_Curriculum.sid_id  "
                   "and  app_Subjects.cid = app_Curriculum.cid_id  " % (cid))

    res = cursor.fetchall()
    return render(request, 'checkSelections.html', {'b' : res})


def getAverageScore(request) :
    db = pymysql.connect("localhost", "root", "990916", "stu_info")
    cursor = db.cursor()
    cid = request.GET['sid']
    if '1' <= cid[0] <= '9' :
        cursor.execute("select app_Students.sid, app_Students.sname,avg(score) as '平均成绩' "
                       "from app_Students, app_Curriculum "
                       "where app_Curriculum.sid_id = %d and app_Students.sid = app_Curriculum.sid_id  " % int(cid))
        res = cursor.fetchall()
        return render(request, 'getAverageScore.html', {'b' : res})

    cursor.execute("select app_Students.sid, app_Students.sname,avg(score) as '平均成绩' "
                   "from app_Students, app_Curriculum "
                   "where app_Students.sname= '%s' and app_Curriculum.sid_id=app_Students.sid" % int(cid))
    res = cursor.fetchall()
    return render(request, 'getAverageScore.html', {'b' : res})


def getClassAverageScore(request) :
    db = pymysql.connect("localhost", "root", "990916", "stu_info")
    cursor = db.cursor()
    cid = request.GET['class']
    cursor.execute("select app_Students.class_name_id,avg(score) "
                   "from app_Curriculum, app_Students"
                   " where app_Students.class_name_id = '%d'"
                   " and app_Curriculum.sid_id = app_Students.sid " % int(cid))
    res = cursor.fetchall()
    return render(request, 'getClassAverageScore.html', {'b' : res})


def getLevelAverageScore(request) :
    db = pymysql.connect("localhost", "root", "990916", "stu_info")
    cursor = db.cursor()
    cid = request.GET['cid']
    cursor.execute("select app_Subjects.cname , avg(score) "
                   "from app_Subjects, app_Curriculum "
                   "where app_Curriculum.cid_id = %d "
                   "and app_Subjects.cid = app_Curriculum.cid_id" % int(cid))
    res = cursor.fetchall()
    #   return render(request, 'checkcinfo3.html', {'b': res})
    cursor.execute("select count(score) "
                   "from app_Subjects, app_Curriculum "
                   "where app_Curriculum.cid_id = %d "
                   "and  app_Curriculum.cid_id= app_Subjects.cid  "
                   "and app_Curriculum.score< 60" % int(cid))
    fail = cursor.fetchall()
    cursor.execute("select count(score) "
                   "from app_Subjects, app_Curriculum "
                   "where app_Subjects.cid = %d "
                   "and  app_Curriculum.cid_id = app_Subjects.cid "
                   "and app_Curriculum.score > 59 "
                   "and app_Curriculum.score < 70" % int(cid))
    level5 = cursor.fetchall()
    cursor.execute("select count(score) "
                   "from app_Subjects, app_Curriculum "
                   "where app_Subjects.cid = %d "
                   "and  app_Subjects.cid = app_Curriculum.cid_id "
                   "and app_Curriculum.score> 69 "
                   "and app_Curriculum.score<80" % int(cid))
    level4 = cursor.fetchall()
    cursor.execute("select count(score) "
                   "from app_Subjects, app_Curriculum "
                   "where app_Subjects.cid = %d "
                   "and  app_Subjects.cid = app_Curriculum.cid_id "
                   "and app_Curriculum.score> 79 "
                   "and app_Curriculum.score<90" % int(cid))
    level3 = cursor.fetchall()
    cursor.execute("select  count(score) "
                   "from app_Subjects, app_Curriculum "
                   "where app_Subjects.cid = %d "
                   "and  app_Subjects.cid = app_Curriculum.cid_id "
                   "and app_Curriculum.score> 89 "
                   "and app_Curriculum.score<99" % int(cid))
    level2 = cursor.fetchall()
    cursor.execute("select count(score) "
                   "from app_Subjects, app_Curriculum "
                   "where app_Subjects.cid = %d "
                   "and  app_Subjects.cid = app_Curriculum.cid_id "
                   "and app_Curriculum.score = 100" % int(cid))
    level1 = cursor.fetchall()
    return render(request, 'getLevelAverageScore.html',
                  {'res' : res, 's1' : fail, 's2' : level5, 's3' : level4, 's4' : level3, 's5' : level2, 's6' : level1})
