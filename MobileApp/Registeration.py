from pymongo import MongoClient
import bcrypt
from Commands import generate_rsa_keypair

def registeration(name, user_id, user_pass, x):
    # Connect to MongoDB using the provided connection string
    client = MongoClient(x)

    # Access the database and collections
    db = client["VOID-Docs"]
    Admins_ID = db["Admins_ID"]
    Admins_Public = db["Admins_Public"]

    # Check if the user ID already exists
    existing_user = Admins_ID.find_one({"ID": user_id})

    # If user does not exist, proceed with registration
    if existing_user is None:
        # Hash the user's password using bcrypt for security
        hashed_password = bcrypt.hashpw(user_pass.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # Store user credentials in Admins_ID collection
        Admins_ID.insert_one({"ID": user_id, "ID_Passwd": hashed_password})

        # Generate a new RSA key pair (private, public)
        keys = generate_rsa_keypair()

        # Store public key and user details in Admins_Public collection
        Admins_Public.insert_one({
            "Public_Key": keys[1],
            "ID": user_id,
            "Name": name
        })

        # Return success message, status flag, and private key
        return ["Registration Successful.", True, keys[0]]

    # If user ID already exists, return failure message
    else:
        return ["Admin ID already in use.", False]
