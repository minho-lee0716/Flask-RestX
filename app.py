# from flask import Flask
# from flask_restx import Api

# api = Api()
# app = Flask(__name__)
# api.init_app(app)


from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {"hello":"world"}

if __name__ == "__main__":
    app.run(port=5000, debug=True)