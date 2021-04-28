''''
注册和登录
'''
from flask import Blueprint, request
from db import database_conn
import pymysql
from datetime import datetime
from mytoken import create_token,login_required,verify_token

bp = Blueprint('overview', __name__, url_prefix='/overview')


"""
url: /overview/addDepartment
methods: post
data: {department,introduction,charge}
return: {"status":200,"msg":"消息"}
"""
@bp.route('/addDepartment', methods=['POST'])
@login_required
def addDepartment():
    # 获取请求数据
    params = request.json#type:dict

    # 对接收来的数据params做处理
    data = params

    try:
        # 连接数据库
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # sql语句
        sql = 'insert into overview(department,introduction,charge) VALUES (%s,%s,%s)'
        # %s对应的参数
        sql_params=[data["department"],data['introduction'],data["charge"]]
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
url: /overview/getData
methods: get
params: {column:"id",keyword:"id",pagenum,pagesize}
return: {"status":200,"msg":"消息",data:[{id:1,department:"前台",introduction:"功能",charge:"主要负责人"},]}
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
            sql = 'select id,department,introduction,charge from overview'
            sql_params = []
        elif column=="id":
            keyword = int(keyword)
            sql = 'select id,department,introduction,charge from overview where id = %s'
            sql_params = [keyword, ]
        else:
            sql = 'select id,department,introduction,charge from overview where %s'%column+" like %s"
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
url: /overview/editDepartment
methods: post
data: {department,introduction,charge}
return: {"status":200,"msg":"消息"}
"""
@bp.route('/editDepartment', methods=['POST'])
@login_required
def editDepartment():
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
        sql = 'update overview set department=%s,introduction=%s,charge=%s where id = %s'
        # %s对应的参数
        sql_params=[data["department"],data['introduction'],data["charge"],data["id"]]
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
url: /overview/deleteDepartment
methods: post
data: {ids:[id1,id2...]}
return: {"status":200,"msg":"消息"}
"""
@bp.route('/deleteDepartment', methods=['POST'])
@login_required
def deleteDepartment():
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
            sql = 'delete  from overview where id=%s'
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

@bp.route('/getUserName', methods=['GET'])
@login_required
def getUserName():
    token = request.headers.get('Authorization')

    if not token:
        return {
            'status': 200,
            'username':""
        }
    username = verify_token(token)
    if username:
        return {
            "status":200,
            "username":username
        }
    else:
        return {
            'status':200,
            "username":""
        }


# 查询
@bp.route('/record', methods=['GET'])
@login_required
def getRecord():

    conn = database_conn()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    params = request.args

    sql = "select * from operate_record"
    cursor.execute(sql)
    res = cursor.fetchall()
    cursor.close()
    conn.close()

    keyword = params['keyword']
    column = params['column']
    pagenum = int(params['pagenum'])
    pagesize = int(params['pagesize'])

    data = []

    # 有搜索关键字
    if keyword:
        if column!="all":
            for item in res:
                if keyword in str(item[column]):
                    data.append(item)

    else:
        data=res


    #分页处理
    total = len(data)
    start = (int(pagenum) - 1) * int(pagesize)
    end = int(pagenum) * int(pagesize)
    data = data[start:end]

    for i in range(0,len(data)):
        data[i]["op_time"]=str(data[i]["op_time"])
    return {
        'status': 200,
        'data': data,
        'total': total,
        'msg': '获取成功'
    }
