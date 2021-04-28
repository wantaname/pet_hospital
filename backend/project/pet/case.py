
from flask import Blueprint, request
from db import database_conn
import pymysql
from datetime import datetime
from mytoken import create_token,login_required,verify_token

bp = Blueprint('pet_case', __name__, url_prefix='/pet_case')
import settings
base_url = settings.baseURL

"""


"""


@bp.route('/getCase', methods=['POST'])
@login_required
def getCase():
    # 获取请求数据
    params = request.json  # type:dict




    try:
        # 连接数据库
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # sql语句
        sql = 'select * from `case`'
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


    type_dict = {}
    for item in result:
        if type_dict.get(item['type']):
            type_dict[item['type']].append(item['case_name'])

        else:
            type_dict[item['type']] = []

            type_dict[item['type']].append(item['case_name'])


    types=[]
    cases = []
    for index,value in type_dict.items():
        types.append(index)
        cases.append(value)


    # 成功
    return {
        'status': 200,
        'msg': '获取成功',
        'types':types,
        "cases":cases
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

@bp.route('/getInfo', methods=['POST'])
@login_required
def getInfo():
    # 获取请求数据
    params = request.json  # type:dict

    def operateData(info):
        if info and "http" not in info[0]['image']:
            info[0]['image'] = base_url+ info[0]['image']
        if info and "iframe" not in info[0]['video']:
            info[0]['video'] =  base_url+info[0]['video']


    case_name = params.get("case")

    try:
        # 连接数据库
        conn = database_conn()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # sql语句
        sql = 'select case_name,text,image,video from `case` where case_name=%s'
        # %s对应的参数
        sql_params = [case_name,]
        cursor.execute(sql, sql_params)
        info = cursor.fetchall()
        operateData(info)

        # sql语句
        sql = 'select case_name,text,image,video from `receive` where case_name=%s'
        # %s对应的参数
        sql_params = [case_name, ]
        cursor.execute(sql, sql_params)
        receive = cursor.fetchall()
        operateData(receive)

        # sql语句
        sql = 'select case_name,text,image,video from `inspect` where case_name=%s'
        # %s对应的参数
        sql_params = [case_name, ]
        cursor.execute(sql, sql_params)
        inspect = cursor.fetchall()
        operateData(inspect)

        # sql语句
        sql = 'select case_name,text,image,video from `result` where case_name=%s'
        # %s对应的参数
        sql_params = [case_name, ]
        cursor.execute(sql, sql_params)
        result = cursor.fetchall()
        operateData(result)

        # sql语句
        sql = 'select case_name,text,image,video from `cure` where case_name=%s'
        # %s对应的参数
        sql_params = [case_name, ]
        cursor.execute(sql, sql_params)
        cure = cursor.fetchall()
        operateData(cure)

        cursor.close()
        conn.close()
    except Exception as e:
        # 出现错误
        print(e)
        return {
            'status': 300,
            'msg': '获取数据失败！'
        }

    caseInfo = {
        "info":info,
        "receive":receive,
        "inspect":inspect,
        "result":result,
        "cure":cure
    }

    # 成功
    return {
        'status': 200,
        'msg': '添加成功',
        'caseInfo':caseInfo
    }



