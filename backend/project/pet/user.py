
from flask import Blueprint, request,g
from db import database_conn
import pymysql
from datetime import datetime
from mytoken import create_token,login_required,verify_token

bp = Blueprint('pet', __name__, url_prefix='/pet')



@bp.route('/register', methods=['POST'])
def register():
    # 获取请求体
    params = request.json#type:dict
    print(params)
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
    time = time.strftime("%Y-%m-%d")

    try:

        conn = database_conn()

        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql = 'insert into user(username,password,create_time) VALUES (%s,%s,%s)'
        params=[username,password,time]
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
        avatar = ""
        # 拿到用户头像
        try:
            # 连接数据库
            conn = database_conn()
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

            # sql语句
            sql = 'select avatar from user where username=%s'
            # %s对应的参数
            sql_params = [username]
            cursor.execute(sql, sql_params)
            result = cursor.fetchone()
            avatar = result.get("avatar")
            cursor.close()
            conn.close()
        except Exception as e:
            # 出现错误
            print(e)
            return {
                'status': 300,
                'msg': '获取数据失败！'
            }
        return {
            "status":200,
            "username":username,
            "avatar":avatar
        }
    else:
        return {
            'status':200,
            "username":""
        }


@bp.route('/uploadAvatar', methods=['POST'])
def uploadAvatar():
    fileDict = request.files
    print(fileDict)
    for item in fileDict.keys():
        filename = item
        file = fileDict[filename]

    creat_time = datetime.now()
    create_time = creat_time.strftime("%Y%m%d%H%M%S")
    filename = create_time
    filename = filename+".png"
    path = "./static/image/" + filename
    print(path)
    avatar = "/static/image/" + filename
    print(fileDict)


    file.save(path)


    # 成功
    return {
        'status':200,
        'msg':'上传成功',
        "url":avatar,
    }

@bp.route('/addAvatar', methods=['POST'])
@login_required
def addAvatar():

    params = request.json
    avatar = params.get("url")

    username = g.username


    try:
        # 连接数据库
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # sql语句
        sql = 'update user set avatar=%s where username=%s'
        # %s对应的参数
        sql_params = [avatar,username]
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
        'status':200,
        'msg':'上传成功！'
    }


# 修改密码
@bp.route('/modifyPassword', methods=['POST'])
@login_required
def modify():
    params = request.json
    oldValue = params.get("oldValue")
    newValue = params.get("newValue")
    username = g.username

    try:
        # 连接数据库
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql = 'select * from user where username=%s and password=%s'
        sql_params = [username,oldValue]
        cursor.execute(sql,sql_params)
        result = cursor.fetchone()
        if not result:
            return {
                'status': 300,
                'msg': '旧密码错误！'
            }

        # sql语句
        sql = 'update user set password=%s where username=%s'
        # %s对应的参数
        sql_params = [newValue,username]
        cursor.execute(sql, sql_params)
        cursor.close()
        conn.close()
    except Exception as e:
        # 出现错误
        print(e)
        return {
            'status': 300,
            'msg': '系统错误！'
        }
    # 成功
    return {
        'status': 200,
        'msg': '修改成功！'
    }