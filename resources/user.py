from flask_smorest import Blueprint,abort
from flask.views import MethodView
from flask import request
from DB import DbInterface
from util.auth import Verify
from models.usermodel import UserModel
from flask import request
from twilio.base.exceptions import TwilioRestException
import mysql.connector.errors as err
from schemas import UserSchema,UserauthSchema
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    get_jwt,
    jwt_required,
)

blp = Blueprint("users", __name__,description="Operation on users")
verify=Verify()

@blp.route("/registeruserorlogin")
class UserRegister(MethodView):

    @blp.arguments(UserSchema)
    def post(self,userdata):
        try: 
            username=userdata.get("username")
            usermobile=userdata.get("mobile") 
            isUser = UserModel().get_user_from_DB(usermobile) 

            if isUser==False:
                    if(userdata.get("flag")==1):
                        sts = verify.sendOtp(usermobile)
                        return {"message":"otp sent sucessfully"}
                    abort(403,message="user not exists")
            else:
                    print(userdata.get("flag"))
                    if(userdata.get("flag")==0):
                        
                        sts = verify.sendOtp(usermobile)
                        return {"message":"otp sent sucessfully"}
                    abort(403,message="user Already exists")
              
            
        except err.Error as e:
                abort(403,message="Databse operation error")
        except TwilioRestException as e:
                print(e.__str__())
                abort(403,message="error in otp send"+e.__str__())

            

@blp.route("/verifyuser")
class verifyuser(MethodView):

    @blp.arguments(UserauthSchema)
    @blp.response(200,UserSchema)
    def post(self,userdata):
        usermobile=userdata.get("mobile")
        code = userdata.get("otp")
        username=userdata.get("username")
        # sid = Verify().createNewAuthService()
        try:
            sts = verify.verifyOtp(usermobile, code)
            if sts.__eq__("approved"):
                print(userdata.get("flag"))
                if(userdata.get("flag")==1):
                    user = UserModel().insert_User_DB(username, usermobile) 
                else:
                    user=UserModel().get_user_from_DB(usermobile)    
                    if(user==False):
                        abort(403,message="user not found and Something went wrong")
                access_token = create_access_token(identity=user.json())
                print(access_token)
                user.setToken(access_token)
                return user
            else:
                abort(403,message="Otp verfiication failed")
        except TwilioRestException as e:
            abort(403,message="error in otp verify"+e.__str__())
        except err.Error as e:
            abort(403,message="Databse operation error")

    
        

