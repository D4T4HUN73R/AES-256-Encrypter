import base64
import hashlib
from Crypto.Cipher import AES

def encrypt(key, plaintext):
    # Hash the key to ensure it is 32 bytes long
    key = hashlib.sha256(key.encode('utf-8')).digest()

    # Create a new cipher object using the key
    cipher = AES.new(key, AES.MODE_EAX)

    # Encrypt the plaintext
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode('utf-8'))

    # Encode the ciphertext in base64
    ciphertext = base64.b64encode(ciphertext).decode('utf-8')

    # Return the ciphertext and the tag
    return ciphertext, tag

def main():
    # Prompt the user for the key and plaintext
    key = input("Enter the key: ")
    plaintext = input("Enter the plaintext: ")

    # Encrypt the plaintext
    ciphertext, tag = encrypt(key, plaintext)

    # Print the ciphertext and tag
    print("Ciphertext:", ciphertext)
    print("Tag:", tag)

if __name__ == "__main__":
    main()
