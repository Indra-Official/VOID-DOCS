import hashlib
import time
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def sha256_hasher(data):
    if isinstance(data, str):
        data = data.encode('utf-8')

    hash_object = hashlib.sha256(data)
    return hash_object.hexdigest()

def generate_rsa_keypair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,)
    public_key = private_key.public_key()

    pem_private = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption())

    pem_public = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo)

    private_key = pem_private.decode()
    public_key = pem_public.decode()
    return [private_key, public_key]

def encrypt_with_private_key(private_key, plaintext):
    ciphertext = private_key.encrypt(
        plaintext.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()), 
            algorithm=hashes.SHA256(), 
            label=None))
    return ciphertext

def decrypt_with_public_key(public_key, ciphertext):
    plaintext = public_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()), 
            algorithm=hashes.SHA256(), 
            label=None))
    
    return plaintext.decode('utf-8')

def block_adder(block_data):
    a = open("Blockchain.txt","r")
    a.close()
    b = eval(a.read())
    previous_block = b[-1]
    hash_previous_block = sha256_hasher(previous_block)
    new_block = {"previous_hash": hash_previous_block, "time_stamp": time.time(), "data": block_data}
    b += new_block
    a = open("Blockchain.txt","w")
    a.write(b)
    a.close()
