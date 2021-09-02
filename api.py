from flask import Flask
from flask_restful import Api, reqparse
from flask_swagger_ui import get_swaggerui_blueprint
from app.routes.hello_world import HelloWorld
from app.routes.random_message import RandomMessage

app = Flask(__name__)
api = Api(app)
prefix="/api/v1"
parser = reqparse.RequestParser()

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Example REST API"
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

api.add_resource(HelloWorld, prefix + '/hello-world')
api.add_resource(RandomMessage, prefix + '/message')

if __name__ == '__main__':
    app.run(debug=True)