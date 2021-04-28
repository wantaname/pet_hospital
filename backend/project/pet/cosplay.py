
from flask import Blueprint, request
from db import database_conn
import pymysql
from datetime import datetime
from mytoken import create_token,login_required,verify_token
import settings
bp = Blueprint('pet_cosplay', __name__, url_prefix='/pet_cosplay')

base_url = settings.baseURL

"""
数据格式：
work:[
        {index:0,name:"",steps:[{index:0,name:"",image:"",text:""}]}
      ]

"""


@bp.route('/qiantai', methods=['POST'])
@login_required
def qiantai():
    # 获取请求数据
    params = request.json  # type:dict




    try:
        # 连接数据库
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # sql语句
        sql = 'select * from cosplay where role=%s'
        # %s对应的参数
        sql_params = ["前台"]
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

    data = []
    work_index = 0
    work_dict = {}
    process_index = 0
    for item in result:
        if work_dict.get(item['work']):
            work_dict[item['work']]['steps'].append({
                "index":process_index,
                "name":item['process'],
                "image":base_url+item['note'],
                "text":item['detail']
            })
            process_index+=1
        else:
            work_dict[item['work']] = {"index":work_index,"name":item['work'],"steps":[]}
            process_index = 0
            work_dict[item['work']]['steps'].append({
                "index": process_index,
                "name": item['process'],
                "image": base_url + item['note'],
                "text": item['detail']
            })
            process_index +=1
            work_index+=1

    for index,value in work_dict.items():
        data.append(value)


    # 成功
    return {
        'status': 200,
        'msg': '添加成功',
        'data':data
    }

@bp.route('/yizhu', methods=['POST'])
@login_required
def yizhu():
    # 获取请求数据
    params = request.json  # type:dict




    try:
        # 连接数据库
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # sql语句
        sql = 'select * from cosplay where role=%s'
        # %s对应的参数
        sql_params = ["医助"]
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

    data = []
    work_index = 0
    work_dict = {}
    process_index = 0
    for item in result:
        if work_dict.get(item['work']):
            work_dict[item['work']]['steps'].append({
                "index":process_index,
                "name":item['process'],
                "image":base_url+item['note'],
                "text":item['detail']
            })
            process_index+=1
        else:
            work_dict[item['work']] = {"index":work_index,"name":item['work'],"steps":[]}
            process_index = 0
            work_dict[item['work']]['steps'].append({
                "index": process_index,
                "name": item['process'],
                "image": base_url + item['note'],
                "text": item['detail']
            })
            process_index +=1
            work_index+=1

    for index,value in work_dict.items():
        data.append(value)


    # 成功
    return {
        'status': 200,
        'msg': '添加成功',
        'data':data
    }

@bp.route('/yishi', methods=['POST'])
@login_required
def yishi():
    # 获取请求数据
    params = request.json  # type:dict




    try:
        # 连接数据库
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # sql语句
        sql = 'select * from cosplay where role=%s'
        # %s对应的参数
        sql_params = ["医师"]
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

    data = []
    work_index = 0
    work_dict = {}
    process_index = 0
    for item in result:
        if work_dict.get(item['work']):
            work_dict[item['work']]['steps'].append({
                "index":process_index,
                "name":item['process'],
                "image":base_url+item['note'],
                "text":item['detail']
            })
            process_index+=1
        else:
            work_dict[item['work']] = {"index":work_index,"name":item['work'],"steps":[]}
            process_index = 0
            work_dict[item['work']]['steps'].append({
                "index": process_index,
                "name": item['process'],
                "image": base_url + item['note'],
                "text": item['detail']
            })
            process_index +=1
            work_index+=1

    for index,value in work_dict.items():
        data.append(value)


    # 成功
    return {
        'status': 200,
        'msg': '添加成功',
        'data':data
    }



