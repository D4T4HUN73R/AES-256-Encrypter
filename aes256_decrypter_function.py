import base64
import hashlib
from Crypto.Cipher import AES

def decrypt(key, ciphertext, tag):
# Hash the key to ensure it is 32 bytes long
key = hashlib.sha256(key.encode('utf-8')).digest()

# Decode the ciphertext from base64
ciphertext = base64.b64decode(ciphertext.encode('utf-8'))

# Create a new cipher object using the key
cipher = AES.new(key, AES.MODE_EAX, tag)

# Decrypt the ciphertext
plaintext = cipher.decrypt(ciphertext).decode('utf-8')

# Return the plaintext
return plaintext
