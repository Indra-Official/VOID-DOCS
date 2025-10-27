from pymongo import MongoClient
import bcrypt
import os
from Commands import clear

while True:
    clear()
    print("""-----------------------------------------------------------------
                        USER LOGIN
-----------------------------------------------------------------
    """)

    user_id = input(" 1 | Enter your ID Number : ")
    user_pass = input(" 2 | Enter your Password : ")

    client = MongoClient("mongodb+srv://thechallengeof100_db_user:Lalith%402007!@void-docs.chspz4j.mongodb.net/")
    db = client["VOID-Docs"]
    Users_ID = db["Users_ID"]
    
    User_record = Users_ID.find_one({"ID": user_id})

    if User_record is None:
        print("\n-----------------------------------------------------------------")
        print("No admin found with that ID.")
        print("-----------------------------------------------------------------")
        input("Press Enter to try again...")
        continue

    stored_hash = User_record.get("ID_Passwd").encode('utf-8')

    if bcrypt.checkpw(user_pass.encode('utf-8'), stored_hash):
        print("\n-----------------------------------------------------------------")
        print("Account Logged In.")
        print("-----------------------------------------------------------------")
        break

    else:
        print("\n-----------------------------------------------------------------")
        print("Account Login Failed.")
        print("-----------------------------------------------------------------")
        input("Press Enter to try again...")