from flask import Flask, jsonify, request, render_template, make_response
#from flask_login import LoginManager, current_user, login_required, login_user, logout_user
#from flask_cors import CORS
import os

# https 만을 지원하는 기능을 http 에서 테스트할 때 필요한 설정
os.environ['OAUTHLIB-INSECURE_TRANSPORT'] = '1'
app = Flask(__name__, static_url_path='/static')
@app.route('/test')
def hello():
    return "<h1>Hello World</h1>"
app.run(host=None, port=5000, debug=True)
