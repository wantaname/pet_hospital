''''
注册和登录
'''
from flask import Blueprint, request
from db import database_conn
import pymysql
from datetime import datetime
from mytoken import create_token,login_required,verify_token

bp = Blueprint('cosplay', __name__, url_prefix='/cosplay')



@bp.route('/addProcess', methods=['POST'])
@login_required
def addProcess():
    # 获取请求数据
    params = request.json#type:dict

    # 对接收来的数据params做处理
    data = params

    try:
        # 连接数据库
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # sql语句
        sql = 'insert into cosplay(role, work, process, detail, note) VALUES (%s,%s,%s,%s,%s)'
        # %s对应的参数
        sql_params=[data["role"],data['work'],data["process"],data["detail"],data["note"]]
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
获取指定关键词和页的科室信息
url: /cosplay/getData
methods: get
params: {column:"id",keyword:"id",pagenum,pagesize}
return: {"status":200,"msg":"消息",data:[{id:1,Process:"前台",introduction:"功能",charge:"主要负责人"},]}
"""
@bp.route('/getData', methods=['get'])
@login_required
def getData():
    # 请求参数
    params = request.args
    # 获取
    column = params.get("column")
    keyword = params.get("keyword")
    pagenum = params.get("pagenum")
    pagesize = params.get("pagesize")



    try:
        # 连接数据库
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # sql语句
        if keyword.strip()=="":
            sql = 'select * from cosplay'
            sql_params = []
        elif column=="id":
            keyword = int(keyword)
            sql = 'select * from cosplay where id = %s'
            sql_params = [keyword, ]
        else:
            sql = 'select * from cosplay where %s'%column+" like %s"
            # %s对应的参数
            sql_params=['%'+keyword+'%',]

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

    total = len(data)

    # 分页处理

    start = (int(pagenum) - 1) * int(pagesize)
    end = int(pagenum) * int(pagesize)
    data = data[start:end]
    # 成功
    return {
        'status':200,
        'msg':'获取成功',
        "data":data,
        "total":total
    }

"""
url: /cosplay/editProcess
methods: post
data: {Process,introduction,charge}
return: {"status":200,"msg":"消息"}
"""
@bp.route('/editProcess', methods=['POST'])
@login_required
def editProcess():
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
        sql = 'update cosplay set role=%s,work=%s,process=%s,detail=%s,note=%s where id = %s'
        # %s对应的参数
        sql_params=[data["role"],data['work'],data["process"],data["detail"],data["note"],data["id"]]
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
url: /cosplay/deleteProcess
methods: post
data: {ids:[id1,id2...]}
return: {"status":200,"msg":"消息"}
"""
@bp.route('/deleteProcess', methods=['POST'])
@login_required
def deleteProcess():
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
            sql = 'delete  from cosplay where id=%s'
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



