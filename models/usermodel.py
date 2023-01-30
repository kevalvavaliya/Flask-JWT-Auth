from DB import DbInterface
import mysql.connector

class UserModel:


    def __init__(self,username="",mobile=""):
        self.username=username
        self.mobile=mobile

    def insert_User_DB(self,username,mobile):
        try:
            db = DbInterface()
            query = f"insert into users(username,mobile) values('{username}','{mobile}')"
            result = db.cur.execute(query)
            db.conn.commit()
            user = UserModel(username,mobile)
            return user
        except mysql.connector.Error as e:
            print(e.msg)
            raise mysql.connector.Error()
    
    def get_user_from_DB(self,mobile):
        try:
            db=DbInterface()
            query=f"select * from users where mobile='{mobile}'"
            db.cur.execute(query)
            user = db.cur.fetchone()
            if user:
                print("user found",user)
                return UserModel(username=user['username'],mobile=user['mobile'])
            return False
        except mysql.connector.Error as e:
            print(e.msg)
            raise mysql.connector.Error()

    def setUsername(self,username):
        self.username=username

    def setMobile(self,mobile):
        self.mobile=mobile

    def getUsername(self):
        return self.username

    def getMobile(self):
        return self.mobile
    
    def setToken(self,token):
        self.token = token
    
    def getToken(self):
        return self.token
    
    def json(self):
        return {
            "mobile":self.getMobile(),
            "username":self.getUsername()
        }
    


    

    