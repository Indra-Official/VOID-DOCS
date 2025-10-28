from pymongo import MongoClient
import bcrypt
from Commands import generate_rsa_keypair

def registeration(name, user_id, user_pass, x):

      client = MongoClient(x)

      db = client["VOID-Docs"]
      Users_ID = db["Users_ID"]
      Users_Public = db["Users_Public"]

      m = Users_ID.find_one({"ID": user_id})

      if m == None:
            id_ = {"ID": user_id, "ID_Passwd": (bcrypt.hashpw(user_pass.encode('utf-8'), bcrypt.gensalt())).decode('utf-8')}  
            Users_ID.insert_one(id_)

            keys = generate_rsa_keypair()

            public_ = {"Public_Key": keys[1], "ID": user_id, "Name": name}
            Users_Public.insert_one(public_)

            return ["Registeration Successfull.", True, keys[0]]
      
      else:
            return ["User ID already in use.", False]