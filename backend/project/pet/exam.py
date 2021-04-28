
from flask import Blueprint, request,g
from db import database_conn
import pymysql
import random
import settings
from datetime import datetime
from mytoken import create_token,login_required,verify_token

bp = Blueprint('pet_exam', __name__, url_prefix='/pet_exam')

base_url = settings.baseURL

"""


"""


@bp.route('/getData', methods=['POST'])
@login_required
def getData():
    # 获取请求数据
    params = request.json  # type:dict

    try:
        # 连接数据库
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # sql语句
        sql = 'select id,question from `question`'
        # %s对应的参数
        sql_params = []
        cursor.execute(sql, sql_params)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
    except Exception as e:
        # 出现错误
        print(e)
        return {
            'status': 300,
            'msg': '获取数据失败！'
        }


    questions = []

    if len(result)>25:
        s = random.sample(result,25)
    else:
        s = result


    for item in s:
        Q = item['question'].split("问题：")[-1]
        Q = Q.split("选项：")
        Q,A = Q[0],Q[-1]


        d = {"id":item['id'],"Q":Q.strip(),"A":A.split(),"answer":""}
        questions.append(d)

    # 成功
    return {
        'status': 200,
        'msg': '获取成功',
        'questions':questions,

    }

@bp.route('/submit', methods=['POST'])
@login_required
def submit():
    # 获取请求数据
    params = request.json  # type:dict

    # [{"answer":"","id":1}]
    answers = params.get("answers")
    use_time = params.get("use_time")
    creat_time = datetime.now()
    exam_time = creat_time.strftime("%Y-%m-%d %H:%M:%S")

    username = g.username

    yes = 0
    no = 0

    try:
        # 连接数据库
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # 插入考试数据
        for item in answers:
            # sql语句
            sql = 'select id,answer from `question` where id=%s'
            # %s对应的参数
            sql_params = [item['id']]
            cursor.execute(sql, sql_params)
            result = cursor.fetchone()
            # 正确
            if item['answer']==result['answer']:
                re = "正确"
                item['result'] = re
                item['score'] = 4
                yes+=1
            else:
                re = "错误"
                item['result'] = re
                item['score'] = 0
                no+=1
            score = str(yes*4)
        insert_sql = "insert into user_exam(username, score, use_time,exam_time) VALUES (%s,%s,%s,%s)"
        sql_params=[username,score,use_time,exam_time]
        cursor.execute(insert_sql,sql_params)

        exam_id = cursor.lastrowid
        # 插入答题数据
        for item in answers:

            insert_sql = "insert into exam_subject(exam_id, username, question_id, answer, result, score) VALUES (%s,%s,%s,%s,%s,%s)"
            sql_params=[exam_id,username,item['id'],item['answer'],item['result'],item['score']]
            cursor.execute(insert_sql,sql_params)

        cursor.close()
        conn.close()
    except Exception as e:
        # 出现错误
        print(e)
        return {
            'status': 300,
            'msg': '提交失败！'
        }

    # 成功
    return {
        'status': 200,
        'msg': '提交成功！',
        'yes':yes,
        'no':no


    }


# 获取指定考试答题数据
"""
{id,username,question_id,answer,result,solution,note,score}
"""
@bp.route('/getExam', methods=['POST'])
@login_required
def getExam():
    # 获取请求数据
    params = request.json  # type:dict

    examId = params.get("examId")
    username = g.username
    try:
        # 连接数据库
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # sql语句
        sql = 'select id,username,question_id,answer,result,score from `exam_subject` where exam_id=%s'
        # %s对应的参数
        sql_params = [examId,]
        cursor.execute(sql, sql_params)
        result = cursor.fetchall()

        sql = "select score,use_time,exam_time from user_exam where id=%s"
        sql_params = [examId]
        cursor.execute(sql, sql_params)
        exam_info =cursor.fetchone()

        info = {
            "total_score":exam_info.get("score"),
            "use_time":exam_info.get("use_time"),
            "exam_time":exam_info.get("exam_time")
        }


        res = []
        for item in result:
            sql = "select answer,note,question from question where id = %s"
            sql_params = [item['question_id'],]
            cursor.execute(sql,sql_params)
            a = cursor.fetchone()

            if a:
                item['solution'] = a.get("answer")
                item['note'] = a.get("note")

                Q = a['question'].split("问题：")[-1]
                Q = Q.split("选项：")
                Q, A = Q[0], Q[-1]

                item['question'] = Q.strip()
                item['options'] = A.split()

                res.append(item)
        cursor.close()
        conn.close()
    except Exception as e:
        # 出现错误
        print(e)
        return {
            'status': 300,
            'msg': '获取数据失败！'
        }



    # 成功
    return {
        'status': 200,
        'msg': '获取成功',
        'examData':{"info":info,"data":res}

    }