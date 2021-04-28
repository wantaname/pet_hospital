from itsdangerous import TimedJSONWebSignatureSerializer as Serializer,BadSignature,SignatureExpired
from flask import current_app,g,request
# token机制

def create_token(username):
    serializer = Serializer(secret_key=current_app.config['SECRET_KEY'], expires_in=360000)
    token = serializer.dumps({'username':username}).decode()
    return token

def verify_token(token):
    serializer = Serializer(secret_key=current_app.config['SECRET_KEY'])

    try:
        data = serializer.loads(token)
    except BadSignature:
        return None
    except SignatureExpired:
        return None
    g.username=data['username']
    return data['username']

# 装饰器，已登录继续执行，未登录返回404
def login_required(func):
    def wrapper(**options):
        # 请求
        token = request.headers.get('Authorization')
        print(token)
        if not token or not verify_token(token):
            return {
                'status':404,
                'msg':'未登录'
            }
        res=func(**options)
        return res

    wrapper.__name__ = func.__name__
    return wrapper


