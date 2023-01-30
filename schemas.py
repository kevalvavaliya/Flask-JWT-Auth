from marshmallow import Schema,fields

class UserSchema(Schema):
    username = fields.Str(required=True,error_messages={"required": "Username is required."})
    mobile = fields.Str(required=True,error_messages={"required": "Mobile no is required."})
    message = fields.Str(dump_only=True,default="success",)
    token = fields.Str()
    flag=fields.Int(load_default=0,load_only=True)

class UserauthSchema(Schema):
    otp = fields.Str(load_only=True,required=True)
    mobile = fields.Str(required=True,error_messages={"required": "Mobile no is required."})
    username = fields.Str(required=True,error_messages={"required": "Username is required."})
    flag=fields.Int(load_default=0,load_only=True)



