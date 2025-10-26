from pymongo import MongoClient
import bcrypt
import os
from Commands import generate_rsa_keypair

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

clear()
print("""-----------------------------------------------------------------
                      ADMIN REGISTERATION
-----------------------------------------------------------------
      """)
a = input(" 1 | Enter your Full Name : ")
b = input(" 2 | Enter you ID Number : ")
c = input(" 3 | Create a Password : ")


client = MongoClient("mongodb://localhost:27017/")

db = client["Void-Docs"]
Admins_ID = db["Admins_ID"]
Admins_Public = db["Admins_Public"]

id_ = {"ID": b, "ID_Passwd": (bcrypt.hashpw(c.encode('utf-8'), bcrypt.gensalt())).decode('utf-8')}  
Admins_ID.insert_one(id_)

keys = generate_rsa_keypair()

public_ = {"Public_Key": keys[1], "ID": b, "Name": a}
Admins_Public.insert_one(public_)

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
file_path = os.path.join(desktop_path, "PRIVATE_KEY.txt")
with open(file_path, "w") as file:
    file.write(keys[0])

print(f"File saved at: {file_path}")

print("""
-----------------------------------------------------------------""")
print("Account Registered.")
print("-----------------------------------------------------------------")
print("\n",keys[1])
print("-----------------------------------------------------------------")



'''
if bcrypt.checkpw(entered_password.encode('utf-8'), hashed):
    print("Password match")

else:
    print("Password does not match")
'''