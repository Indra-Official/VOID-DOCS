from pymongo import MongoClient
import bcrypt
import os
from Commands import generate_rsa_keypair, clear

clear()


print("""-----------------------------------------------------------------
                      ADMIN REGISTERATION
-----------------------------------------------------------------
      """)
a = input(" 1 | Enter your Full Name : ")
b = input(" 2 | Enter your ID Number : ")
c = input(" 3 | Create a Password : ")


client = MongoClient("mongodb+srv://thechallengeof100_db_user:Lalith%402007!@void-docs.chspz4j.mongodb.net/")

db = client["VOID-Docs"]
Admins_ID = db["Admins_ID"]
Admins_Public = db["Admins_Public"]

id_ = {"ID": b, "ID_Passwd": (bcrypt.hashpw(c.encode('utf-8'), bcrypt.gensalt())).decode('utf-8')}  
Admins_ID.insert_one(id_)

keys = generate_rsa_keypair()

public_ = {"Public_Key": keys[1], "ID": b, "Name": a}
Admins_Public.insert_one(public_)

x = open("DesktopApp/Private_Key.txt", "w")
x.write(keys[0])
x.close()

print("""
-----------------------------------------------------------------""")
print("Account Registered.")
print("-----------------------------------------------------------------")
print("\n",keys[1])
print("-----------------------------------------------------------------")