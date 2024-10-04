import requests
import json
import os

# 1. Hardcoded sensitive credentials and secrets (BAD PRACTICE)
DATABASE_USERNAME = "admin"  # Hardcoded username (BAD)
DATABASE_PASSWORD = "password123"  # Hardcoded password (BAD)
API_KEY = "my_secret_api_key_123"  # Hardcoded API key (BAD PRACTICE)
SECRET_KEY = "my_secret_key_987"  # Hardcoded secret key (BAD)
PRIVATE_KEY = """
-----BEGIN PRIVATE KEY-----
MIIBVgIBADANBgkqhkiG9w0BAQEFAASCATwwggE4AgEAAkEAhackable_private_key_content
badsecretkeyexposedtoeveryone+++++++++++++++/+++++++more_bad_exposure++
-----END PRIVATE KEY-----
"""  # Exposed private key (BIG SECURITY RISK)

# 2. Weak encryption (XOR-based encryption) - BAD PRACTICE
def weak_encrypt(data):
    key = "weak_key_123"  # Weak encryption key (easy to guess)
    encrypted_data = ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))
    return encrypted_data

# 3. Poor error handling with a broad exception catch
def fetch_user_data(username):
    print(f"Connecting to the database with username: {DATABASE_USERNAME} and password: {DATABASE_PASSWORD}")  # Exposing sensitive information in logs
    try:
        # Simulating insecure database query with hardcoded credentials
        if username == "admin":
            return {"username": "admin", "password": "plaintextpassword", "role": "admin"}  # Exposing plaintext passwords
        elif username == "user":
            return {"username": "user", "password": "userpassword", "role": "user"}  # No password protection (BAD)
        else:
            # Return None for non-existent users, with no proper error message
            print("User not found.")
    except Exception as e:
        # Broad exception catch (BAD PRACTICE)
        print("An error occurred:", e)

# 4. Insecure API requests, exposing API keys
def insecure_api_request():
    headers = {"Authorization": f"Bearer {API_KEY}"}
    print(f"Making an API request with API key: {API_KEY}")  # Exposing API key in logs
    try:
        # Fake API request
        response = requests.get("https://jsonplaceholder.typicode.com/posts", headers=headers)
        return response.json()  # Assuming response is valid without validation
    except Exception as e:
        # No specific exception handling, just catching everything
        print("Failed to make API request:", e)
        return None

# 5. Logging sensitive information like passwords in plain text (BAD PRACTICE)
def process_login(username, password):
    print(f"Attempting login for user: {username} with password: {password}")  # Logging sensitive info
    user_data = fetch_user_data(username)
    if user_data and user_data["password"] == password:
        return f"Login successful for user: {username} with role: {user_data['role']}"
    else:
        return "Login failed."  # No details provided for failed logins

# 6. Poor encryption handling (BAD and buggy)
def handle_sensitive_data():
    sensitive_data = "SuperSecretInformation"
    encrypted = weak_encrypt(sensitive_data)
    print(f"Encrypted sensitive data (weakly): {encrypted}")  # Exposing weakly encrypted data
    return encrypted

# 7. Exposing private key in logs
def expose_private_key():
    print(f"Exposing private key: {PRIVATE_KEY}")  # HUGE security risk
    # Simulate insecure usage of the private key
    return f"Processed key: {PRIVATE_KEY}"

# 8. Poor secret management, errors in accessing secrets
def handle_secret_key():
    try:
        print(f"Using secret key: {SECRET_KEY}")  # Exposing sensitive data in logs
        if not SECRET_KEY:
            raise ValueError("No secret key found!")  # Raising error unnecessarily
    except Exception as e:
        print(f"Error handling secret: {e}")  # General exception catch

# 9. Writing sensitive information to a file (Insecure practice)
def insecure_file_operations():
    try:
        with open("secrets.txt", "w") as file:
            file.write(f"API_KEY: {API_KEY}\n")  # Exposing API key in file
            file.write(f"PRIVATE_KEY: {PRIVATE_KEY}\n")  # Exposing private key in file
            file.write(f"DATABASE_PASSWORD: {DATABASE_PASSWORD}\n")  # Exposing database password in file
        print("Sensitive data written to file.")
    except Exception as e:
        print(f"Error writing to file: {e}")  # No specific error handling

# 10. Mismanaging sensitive file deletion (Insecure)
def delete_sensitive_file():
    try:
        os.remove("secrets.txt")  # Exposing that sensitive file existed
        print("Sensitive file deleted (but it shouldn't have been created!)")
    except FileNotFoundError:
        print("File not found (couldn't delete).")
    except Exception as e:
        print(f"Error deleting file: {e}")  # General exception catch

if __name__ == "__main__":
    # 11. Processing insecure login (Hardcoded credentials)
    print(process_login("admin", "plaintextpassword"))  # Logs and exposes sensitive information
    print(process_login("user", "wrongpassword"))  # Login failure with no details

    # 12. Making an insecure API call
    insecure_api_request()

    # 13. Handling sensitive data with weak encryption
    handle_sensitive_data()

    # 14. Exposing the private key (HUGE risk)
    expose_private_key()

    # 15. Handling secrets poorly
    handle_secret_key()

    # 16. Insecurely writing sensitive information to a file
    insecure_file_operations()

    # 17. Attempting to delete sensitive file insecurely
    delete_sensitive_file()
