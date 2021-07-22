#from flask import Flask, jsonify, request, render_template, make_response
##from flask_login import LoginManager, current_user, login_required, login_user, logout_user
##from flask_cors import CORS
#import os
#
## https 만을 지원하는 기능을 http 에서 테스트할 때 필요한 설정
#os.environ['OAUTHLIB-INSECURE_TRANSPORT'] = '1'
#app = Flask(__name__, static_url_path='/static')
#@app.route('/test')
#def hello():
#    return "<h1>Hello World</h1>"
#app.run(host=None, port=5000, debug=True)

from flask import Flask

app = Flask(__name__)

if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler # handler는 여러개의 종류가 있다.
    file_handler = RotatingFileHandler('test_log.log', maxBytes=2000, backupCount=10)
    file_handler.setLevel(logging.DEBUG) # 어느 단계까지 로깅을 허용할 것인지.
    # app.logger.addHandler()에 등록을 해주어야 app.logger로 사용이 가능하다.
    app.logger.addHandler(file_handler)

@app.errorhandler(404)
def page_not_found(info):
    app.logger.error(info)
    return "<h1>404 Not Found Test</h1>", 404

@app.route("/test_page")
def hello():
    return "<h1>Hello World</h1>"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080", debug=True)
