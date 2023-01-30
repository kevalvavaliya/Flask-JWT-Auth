import mysql.connector

class DbInterface():
     
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            db="ClassyCommerce",
        )
        if self.conn.is_connected():
            print("Database Connected")
            self.cur = self.conn.cursor(buffered=True,dictionary=True)
        else:
            print("Database NOT Connected")
            
            

    def __del__(self):
        print("destructor")
        self.cur.close()
        self.conn.close()

        

    

   
        

    
