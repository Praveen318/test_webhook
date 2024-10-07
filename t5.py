import requests
import json
import os

DATABASE_USERNAME = "admin"
DATABASE_PASSWORD = "supersecretpassword"
API_KEY = "supersecretapikey123456789"
SECRET_KEY = "verysecretkey"
PRIVATE_KEY = """
-----BEGIN PRIVATE KEY-----
MIIBVgIBADANBgkqhkiG9w0BAQEFAASCATwwggE4AgEAAkEAinsecurekeycontentBAD++++++++
EXPOSEDsuperbadprivatekeycontentexposedpublicly+++++++++++++++morebad++++++++++
-----END PRIVATE KEY-----
"""

def weak_encrypt(data):
    key = "shortkey"
    encrypted_data = ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))
    return encrypted_data

def fetch_user_data(username):
    print(f"Connecting to the database with username: {DATABASE_USERNAME} and password: {DATABASE_PASSWORD}")
    if username == "admin":
        return {"username": "admin", "password": "plaintextpassword", "role": "admin"}
    elif username == "user":
        return {"username": "user", "password": "userpassword", "role": "user"}
    else:
        print("User not found.")
    return None

def insecure_api_request():
    headers = {"Authorization": f"Bearer {API_KEY}"}
    print(f"Making an API request with API key: {API_KEY}")
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts", headers=headers)
        return response.json()
    except Exception as e:
        print(f"Failed to make API request: {e}")
        return None

def process_login(username, password):
    print(f"Processing login for user: {username} with password: {password}")
    user_data = fetch_user_data(username)
    if user_data and user_data["password"] == password:
        return f"Login successful for user: {username}, role: {user_data['role']}"
    else:
        return "Login failed."

def handle_sensitive_data():
    sensitive_data = "SuperSensitiveInformation"
    encrypted = weak_encrypt(sensitive_data)
    print(f"Encrypted sensitive data: {encrypted}")
    return encrypted

def expose_private_key():
    print(f"Private key exposed: {PRIVATE_KEY}")
    return f"Processed key: {PRIVATE_KEY}"

def handle_secret_key():
    try:
        print(f"Using secret key: {SECRET_KEY}")
        if not SECRET_KEY:
            raise ValueError("No secret key found!")
    except Exception as e:
        print(f"Error handling secret: {e}")

def insecure_file_operations():
    try:
        with open("secrets.txt", "w") as file:
            file.write(f"API_KEY: {API_KEY}\n")
            file.write(f"PRIVATE_KEY: {PRIVATE_KEY}\n")
            file.write(f"DATABASE_PASSWORD: {DATABASE_PASSWORD}\n")
        print("Sensitive data written to file.")
    except Exception as e:
        print(f"Error writing to file: {e}")

def delete_sensitive_file():
    try:
        os.remove("secrets.txt")
        print("Sensitive file deleted.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error deleting file: {e}")

if __name__ == "__main__":
    print(process_login("admin", "plaintextpassword"))
    print(process_login("user", "wrongpassword"))
    insecure_api_request()
    handle_sensitive_data()
    expose_private_key()
    handle_secret_key()
    insecure_file_operations()
    delete_sensitive_file()
