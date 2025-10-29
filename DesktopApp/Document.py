from pymongo import MongoClient
from Commands import sha256_hasher , clear
import time

while True:
    clear()
    print("""-----------------------------------------------------------------
                      DOCUMENT CREATION
-----------------------------------------------------------------
        """)
    a = input("Enter prompt to generate document :")
    from google import genai

    client = genai.Client(api_key = )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=a+ str ("(This is used for a coding project and i want only the file as the output i am directlying taking the response as the whole document. )"),
    ).text
    print(response)
    document_hash = sha256_hasher(response)
    time.sleep(10)
    clear()

    print("""-----------------------------------------------------------------
                        DOCUMENT PREPARED
-----------------------------------------------------------------
        """)
    
    print(response,"\n")
    print("-----------------------------------------------------------------")

    x = input(" 1 | Confirm to Upload Document (Y/N) : ")

    if x.lower() == 'y':
        break
    else:
        clear()
        continue



client = MongoClient("mongodb+srv://thechallengeof100_db_user:Lalith%402007!@void-docs.chspz4j.mongodb.net/")

db = client["VOID-Docs"]
Docs = db["Documents"]
Users_Public = db["Users_Public"]

id_ = {"Document_Hash": document_hash, "Document": a}  
Docs.insert_one(id_)

print("Document Uploaded Successfully.")
time.sleep(0.5)
print("-----------------------------------------------------------------")


user_count = 1
public_key = {}
ver = ("""-----------------------------------------------------------------
                    DOCUMENT ACKNOWLEDGEMENT
-----------------------------------------------------------------""")
display = ("""-----------------------------------------------------------------
       SELECT USERS DOCUMENT ACKNOWLEDGEMENT REQUIRED FROM
-----------------------------------------------------------------""")

while True:

    clear()

    print(display)

    add = input(" Enter User ID Number or Press [ENTER] to Finalize : ")

    if add == "":
        break
    else:
        user_record = Users_Public.find_one({"ID": add})
        if user_record is None:
            print("\n-----------------------------------------------------------------")
            print("No user found with that ID.")
            input("Press Enter to try again...")
            continue
        else:
            ver += "\n" + str(user_count) + " | " + user_record.get("ID") + " " + user_record.get("Name")
            display += "\n" + str(user_count) + " | " + user_record.get("ID") + " " + user_record.get("Name")
            public_key[user_record.get("ID")] = user_record.get("Public_Key")
            user_count += 1


