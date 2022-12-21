# AES-256-Encrypter
This script prompts the user for a key and a plaintext string, and then encrypts the plaintext using AES 256 in EAX mode. The ciphertext and tag are returned and printed to the console. 

To decrypt the ciphertext, you can use the following function:
```
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
```

You can use this function by passing in the key, ciphertext, and tag as arguments. The plaintext will be returned.
