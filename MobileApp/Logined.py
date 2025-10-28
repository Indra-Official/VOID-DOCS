from pymongo import MongoClient
import bcrypt

def logined(user_id, user_pass, x):

    client = MongoClient(x)
    db = client["VOID-Docs"]
    Users_ID = db["Users_ID"]
    
    User_record = Users_ID.find_one({"ID": user_id})

    if User_record is None:
        return ["No admin found with that ID.", False]

    stored_hash = User_record.get("ID_Passwd").encode('utf-8')

    if bcrypt.checkpw(user_pass.encode('utf-8'), stored_hash):
        return ["Account Logged In." , True]

    else:
        return ["Account Login Failed.", False]