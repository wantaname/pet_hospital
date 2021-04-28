
from flask import Blueprint, request
from db import database_conn
import pymysql
from datetime import datetime
from mytoken import create_token,login_required,verify_token

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/add', methods=['POST'])
@login_required
def add():
    # 获取请求数据
    params = request.json  # type:dict

    # 对接收来的数据params做处理
    data = params

    # 写入数据库，获取当前时间
    creat_time = datetime.now().date()
    creat_time = creat_time.strftime("%Y-%m-%d")
    try:
        # 连接数据库
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # sql语句
        sql = 'insert into `user`(username, password, create_time) VALUES (%s,%s,%s)'
        # %s对应的参数
        sql_params = [data["username"], data['password'], creat_time]
        cursor.execute(sql, sql_params)
        cursor.close()
        conn.close()
    except Exception as e:
        # 出现错误
        print(e)
        return {
            'status': 300,
            'msg': '添加失败！'
        }

    # 成功
    return {
        'status': 200,
        'msg': '添加成功'
    }


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

    print(params)


    try:
        # 连接数据库
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # sql语句
        if keyword.strip()=="":
            sql = 'select * from `user`'
            sql_params = []
        elif column=="id":
            keyword = int(keyword)
            sql = 'select * from `user` where id = %s'
            sql_params = [keyword, ]
        else:
            sql = 'select * from `user` where %s'%column+" like %s"
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

    for item in data:
        item['password'] = hash(item['password'])
    # 成功
    return {
        'status':200,
        'msg':'获取成功',
        "data":data,
        "total":total
    }



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
        sql = 'update `user` set username=%s,`password`=%s where id = %s'
        # %s对应的参数
        sql_params=[data["username"],data['password'],data["id"]]
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
            sql = 'delete  from `user` where id=%s'
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


@bp.route('/register', methods=['POST'])
def register():
    # 获取请求体
    params = request.json#type:dict

    username=params.get('username')
    password=params.get('password')

    if ' ' in username or ' ' in password:
        return {
            'status': 300,
            'msg': '账号密码不合法'
        }

    # 检查参数
    if not username or not password:
        return {
            'status':300,
            'msg':'账号密码不合法'
        }

    # 写入数据库，获取当前时间
    time = datetime.now().date()


    try:

        conn = database_conn()

        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql = 'insert into user(username,password) VALUES (%s,%s)'
        params=[username,password]
        cursor.execute(sql,params)
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)
        return {
            'status': 300,
            'msg':'账号已被注册'
        }
    return {
        'status':200,
        'msg':'注册成功'
    }


@bp.route('/login', methods=['POST'])
def login():
    # 获取请求体
    params = request.json#type:dict

    username=params.get('username')
    password=params.get('password')
    if ' ' in username or ' ' in password:
        return {
            'status': 300,
            'msg': '账号密码不合法'
        }

    # 检查数据库
    try:
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql = 'select * from user where username=%s and password=%s'
        params=[username,password]
        cursor.execute(sql,params)

        res = cursor.fetchone()

        cursor.close()
        conn.close()
    except Exception as e:
        print(e)
        return {
            'status': 300,
            'msg':'系统错误'
        }

    # 成功
    if res:
        token = create_token(username=username)
        print(token)
        return {
            'status':200,
            'token':token,
            'msg':'登录成功'
        }
    else:
        return {
            'status': 300,

            'msg': '账号或密码错误！'
        }


@bp.route('/getUserName', methods=['GET'])
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
