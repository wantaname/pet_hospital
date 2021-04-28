# 入口文件

from flask import Flask
import user
import administrator,cosplay, receive,case
import _inspect,result,cure
import department,question,exam_subject,user_exam
import score_analysis
import upload
import pet.user,pet.cosplay,pet.case,pet.exam

from flask_cors import CORS
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_pyfile('settings.py', silent=True)
    CORS(app, resources=r'/*')

    app.register_blueprint(user.bp)
    app.register_blueprint(administrator.bp)
    app.register_blueprint(department.bp)
    app.register_blueprint(cosplay.bp)
    app.register_blueprint(case.bp)
    app.register_blueprint(receive.bp)
    app.register_blueprint(_inspect.bp)
    app.register_blueprint(result.bp)
    app.register_blueprint(cure.bp)
    app.register_blueprint(question.bp)
    app.register_blueprint(exam_subject.bp)
    app.register_blueprint(user_exam.bp)
    app.register_blueprint(score_analysis.bp)
    app.register_blueprint(upload.bp)


    # 前台接口
    app.register_blueprint(pet.user.bp)
    app.register_blueprint(pet.cosplay.bp)
    app.register_blueprint(pet.case.bp)
    app.register_blueprint(pet.exam.bp)
    return app
app=create_app()


