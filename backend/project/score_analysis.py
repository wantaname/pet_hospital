
from flask import Blueprint, request
from db import database_conn
import pymysql
from datetime import datetime
from mytoken import create_token,login_required,verify_token

bp = Blueprint('score_analysis', __name__, url_prefix='/score_analysis')



@bp.route('/add', methods=['POST'])
@login_required
def add():
    # 获取请求数据
    params = request.json#type:dict
    print(params)
    # 对接收来的数据params做处理
    data = params
    try:
        data["question_id"] = int(data["question_id"])
    except:
        return {
            "status":300,
            "msg":'题号有误！'
        }

    try:
        # 连接数据库
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # sql语句
        sql = 'insert into exam(username, question_id, answer, result, score) VALUES (%s,%s,%s,%s,%s)'
        # %s对应的参数
        sql_params=[data['username'],data["question_id"],data["answer"],data["result"],data["score"]]
        cursor.execute(sql,sql_params)
        cursor.close()
        conn.close()
    except Exception as e:
        # 出现错误
        print(e)
        return {
            'status': 300,
            'msg':'添加失败！'
        }

    # 成功
    return {
        'status':200,
        'msg':'添加成功'
    }


"""
获取实时分数
返回 [{username,score}]
"""
@bp.route('/getData', methods=['get'])
@login_required
def getData():
    # 请求参数
    params = request.args
    # 获取
    column = params.get("column")
    keyword = params.get("keyword")#type:str


    result = []

    try:
        # 连接数据库
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        if column=="username" and keyword.strip():
            sql = 'select * from user where %s' % column + " like %s"
            # %s对应的参数
            sql_params = ['%' + keyword + '%', ]
            cursor.execute(sql, sql_params)
            data = cursor.fetchall()



        else:
            sql = 'select username from user'
            sql_params = []
            cursor.execute(sql, sql_params)
            data = cursor.fetchall()
        for user in data:
            username = user['username']
            item = {"username": username, "score": 0}
            sql = "select score from user_exam where username=%s"
            sql_params = [username, ]
            cursor.execute(sql, sql_params)
            data = cursor.fetchall()

            for row in data:
                item["score"] += int(row['score'])
            result.append(item)

        cursor.execute(sql,sql_params)
        data = cursor.fetchall()
        cursor.close()
        conn.close()

    except Exception as e:
        # 出现错误
        print(e)
        return {
            'status': 300,
            'msg':'获取失败！'
        }


    # 成功
    return {
        'status':200,
        'msg':'获取成功',
        "data":result,

    }

"""
url: /case/editcase
methods: post
data: {case,introduction,charge}
return: {"status":200,"msg":"消息"}
"""
@bp.route('/edit', methods=['POST'])
@login_required
def edit():
    # 获取请求数据
    params = request.json#type:dict

    print(params)
    # 对接收来的数据params做处理
    data = params

    try:
        # 连接数据库
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # sql语句
        sql = 'update `exam` set username=%s,question_id=%s,answer=%s,result=%s,score=%s where id = %s'
        # %s对应的参数
        sql_params=[data['username'],int(data["question_id"]),data["answer"],data["result"],data['score'],data["id"]]
        cursor.execute(sql,sql_params)
        cursor.close()
        conn.close()
    except Exception as e:
        # 出现错误

        print(e)
        return {
            'status': 300,
            'msg':'修改失败！'
        }

    # 成功
    return {
        'status':200,
        'msg':'修改成功'
    }



"""
根据id批量删除科室数据
url: /case/deletecase
methods: post
data: {ids:[id1,id2...]}
return: {"status":200,"msg":"消息"}
"""
@bp.route('/delete', methods=['POST'])
@login_required
def delete():
    # 请求参数
    params = request.json
    # 获取id数组
    ids = params.get("ids")

    try:
        # 连接数据库
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # sql语句
        for id in ids:
            sql = 'delete  from `exam` where id=%s'
            # %s对应的参数
            sql_params=[id,]
            cursor.execute(sql,sql_params)

        cursor.close()
        conn.close()
    except Exception as e:
        # 出现错误
        print(e)
        return {
            'status': 300,
            'msg':'删除失败！'
        }

    # 成功
    return {
        'status':200,
        'msg':'删除成功',

    }



