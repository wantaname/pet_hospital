
import pymysql

host = '127.0.0.1'
port = 3306
user = 'root'
password = '981011yzp'
database = 'pet_hospital'
charset = 'utf8'



# 连接数据库
def database_conn():
    conn = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        charset=charset,
        autocommit=True,
    )
    return conn
