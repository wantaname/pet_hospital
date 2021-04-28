
from flask import Blueprint, request
from db import database_conn
import pymysql
from datetime import datetime
from mytoken import create_token,login_required,verify_token

bp = Blueprint('upload', __name__, url_prefix='/upload')

@bp.route('/uploadImage', methods=['POST'])
def upload():
    fileDict = request.files
    print(fileDict)
    for item in fileDict.keys():
        filename = item
        file = fileDict[filename]
    path = "./static/image/" + filename

    print(fileDict)


    file.save(path)
    # 成功
    return {
        'status':200,
        'msg':'上传成功'
    }


@bp.route('/addImage', methods=['POST'])
@login_required
def add():
    # 获取请求数据
    params = request.json#type:dict
    name = params.get("name")
    path = "/static/image/" + name
    note = params.get("note")
    try:
        # 连接数据库
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # sql语句
        sql = 'insert into image(name, path,note) VALUES (%s,%s,%s)'
        # %s对应的参数
        sql_params = [name, path,note]
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


"""
获取指定关键词和页的科室信息
url: /case/getData
methods: get
params: {column:"id",keyword:"id",pagenum,pagesize}
return: {"status":200,"msg":"消息",data:[{id:1,case:"前台",introduction:"功能",charge:"主要负责人"},]}
"""
@bp.route('/getImage', methods=['get'])
@login_required
def getData():
    # 请求参数
    params = request.args
    # 获取
    column = params.get("column")
    keyword = params.get("keyword")#type:str
    pagenum = params.get("pagenum")
    pagesize = params.get("pagesize")


    try:
        # 连接数据库
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # sql语句
        if keyword.strip()=="":
            sql = 'select * from image'
            sql_params = []
        else:
            sql = 'select * from image where %s'%column+" like %s"
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
根据id批量删除科室数据
url: /case/deletecase
methods: post
data: {ids:[id1,id2...]}
return: {"status":200,"msg":"消息"}
"""
@bp.route('/deleteImage', methods=['POST'])
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
            sql = 'delete  from `image` where id=%s'
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


@bp.route('/uploadVideo', methods=['POST'])
def uploadVideo():
    fileDict = request.files
    print(fileDict)
    for item in fileDict.keys():
        filename = item
        file = fileDict[filename]
    path = "./static/video/" + filename



    file.save(path)
    # 成功
    return {
        'status':200,
        'msg':'上传成功'
    }


@bp.route('/addVideo', methods=['POST'])
@login_required
def addVideo():
    # 获取请求数据
    params = request.json#type:dict
    name = params.get("name")
    path = "/static/video/" + name
    note = params.get("note")
    try:
        # 连接数据库
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # sql语句
        sql = 'insert into video(name, path,note) VALUES (%s,%s,%s)'
        # %s对应的参数
        sql_params = [name, path,note]
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



@bp.route('/getVideo', methods=['get'])
@login_required
def getVideo():
    # 请求参数
    params = request.args
    # 获取
    column = params.get("column")
    keyword = params.get("keyword")#type:str
    pagenum = params.get("pagenum")
    pagesize = params.get("pagesize")


    try:
        # 连接数据库
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # sql语句
        if keyword.strip()=="":
            sql = 'select * from video'
            sql_params = []
        else:
            sql = 'select * from video where %s'%column+" like %s"
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




@bp.route('/deleteVideo', methods=['POST'])
@login_required
def deleteVideo():
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
            sql = 'delete  from `video` where id=%s'
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
