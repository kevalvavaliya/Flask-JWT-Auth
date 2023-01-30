from flask import Flask,request
from flask_smorest import abort
from flask_cors import CORS 
import secrets
from flask_jwt_extended import JWTManager
from flask_smorest import Api
from resources.user import blp as userblueprint


app = Flask(__name__)
CORS(app)


app.config["JWT_SECRET_KEY"]="keval"
jwt = JWTManager(app)


app.config["PROPAGATE_EXCEPTIONS"]=True
app.config["API_TITLE"]="Classy Commerce API interface"
app.config["API_VERSION"]="v1"
app.config["OPENAPI_VERSION"]="3.0.3"
app.config["OPENAPI_URL_PREFIX"]="/"
app.config["OPENAPI_SWAGGER_UI_PATH"]="/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"]="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.19.5/"

api = Api(app)

api.register_blueprint(userblueprint)



