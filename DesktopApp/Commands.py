import hashlib
import time
import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes



# ---------------------------------------------
# Generates SHA-256 hash of the given data
# ---------------------------------------------
def sha256_hasher(file_storage):
    sha256 = hashlib.sha256()
    file_storage.stream.seek(0)  # Ensure stream starts at beginning

    for chunk in iter(lambda: file_storage.stream.read(4096), b''):
        sha256.update(chunk)

    file_storage.stream.seek(0)  # Reset stream for future use
    return sha256.hexdigest()



def restore_file_from_mongo(file_id, output_folder, collection):
    from bson import ObjectId

    """
    Converts a MongoDB-stored file back to a regular file on disk.

    Parameters:
    - file_id: string or ObjectId of the MongoDB document
    - output_folder: path to save the restored file
    - collection: MongoDB collection object

    Returns:
    - Path to the saved file or error message
    """
    try:
        # Ensure file_id is an ObjectId
        if isinstance(file_id, str):
            file_id = ObjectId(file_id)

        # Fetch document
        doc = collection.find_one({'_id': file_id})
        if not doc:
            return "File not found in MongoDB."

        filename = doc.get('filename', 'restored_file')
        file_data = doc.get('file_data')

        if not file_data:
            return "No file data found in document."

        # Save to disk
        output_path = os.path.join(output_folder, filename)
        with open(output_path, 'wb') as f:
            f.write(file_data)

        return f"File restored to: {output_path}"

    except Exception as e:
        return f"Error: {str(e)}"



# ---------------------------------------------
# Generates a new RSA public/private key pair
# ---------------------------------------------
def generate_rsa_keypair():
    # Create RSA private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    # Extract public key from the private key
    public_key = private_key.public_key()

    # Convert private key to PEM format (readable text form)
    pem_private = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    # Convert public key to PEM format
    pem_public = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Decode PEM bytes to string for storage or display
    private_key = pem_private.decode()
    public_key = pem_public.decode()

    return [private_key, public_key]


# ---------------------------------------------
# Encrypts plaintext using a private key
# (Note: Typically, private keys are used for signing, not encryption)
# ---------------------------------------------
def encrypt_with_private_key(private_key, plaintext):
    ciphertext = private_key.encrypt(
        plaintext.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()), 
            algorithm=hashes.SHA256(), 
            label=None
        )
    )
    return ciphertext


# ---------------------------------------------
# Decrypts ciphertext using a public key
# (Note: Typically, public keys verify signatures, not decrypt)
# ---------------------------------------------
def decrypt_with_public_key(public_key, ciphertext):
    plaintext = public_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()), 
            algorithm=hashes.SHA256(), 
            label=None
        )
    )
    return plaintext.decode('utf-8')


# ---------------------------------------------
# Adds a new block to the blockchain text file
# ---------------------------------------------
def block_adder(block_data):
    # Open and read the existing blockchain file
    a = open("Blockchain.txt", "r")
    a.close()
    b = eval(a.read())  # Convert file string to Python object (list of blocks)

    # Get the last block and hash it for linkage
    previous_block = b[-1]
    hash_previous_block = sha256_hasher(previous_block)

    # Create new block with timestamp and reference to previous hash
    new_block = {
        "previous_hash": hash_previous_block,
        "time_stamp": time.time(),
        "data": block_data
    }

    # Append new block and save back to file
    b += new_block
    a = open("Blockchain.txt", "w")
    a.write(b)
    a.close()
