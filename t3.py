import requests
import json

# 1. Hardcoded sensitive credentials and secrets (BAD PRACTICE)
DATABASE_PASSWORD = "password123"  # Hardcoded password, easy to guess
API_KEY = "supersecretapikey123456789"  # Hardcoded API key, exposed in plain text
SECRET_KEY = "topsecretkey"  # Hardcoded secret key
PRIVATE_KEY = """
-----BEGIN PRIVATE KEY-----
MIIBVwIBADANBgkqhkiG9w0BAQEFAASCAT8wggE7AgEAAkEAq4kdfjHbadcodeplainsuperbadkey
Q6V7+xBD/fakesuperlongkeyexposed+++++++wrongexposure+++++++++++++/+++++badsample
-----END PRIVATE KEY-----
"""  # Exposed private key (HUGE SECURITY RISK)

# 2. Weak encryption method (BAD PRACTICE)
def weak_encrypt(data):
    key = "weakkey123"  # Short, non-random key (easy to break)
    encrypted_data = ''.join(chr(ord(char) ^ ord(key[i % len(key)])) for i, char in enumerate(data))
    return encrypted_data

# 3. Poor database simulation (BAD)
def fetch_user_data(username):
    print(f"Connecting to database with password: {DATABASE_PASSWORD}")  # Exposing password in logs
    if username == "admin":
        return {"username": "admin", "password": "plaintextpassword", "role": "admin"}
    elif username == "user":
        return {"username": "user", "password": "userpassword", "role": "user"}
    else:
        # Forgot to handle non-existent users properly (BUG)
        print("User not found.")
    return None

# 4. Unprotected API request (Insecure)
def insecure_api_call(endpoint):
    # Expose API key in the request
    headers = {"Authorization": f"Bearer {API_KEY}"}
    print(f"Making API request to {endpoint} with headers: {headers}")  # Exposing sensitive data
    try:
        response = requests.get(endpoint, headers=headers)
        # Missing error handling and validation
        return response.json()  # Assuming everything will work fine (BUG)
    except Exception as e:
        # Broad exception catching (BAD PRACTICE)
        print(f"API request failed: {str(e)}")
        return None

# 5. Exposing sensitive info in logs (BAD)
def process_login(username, password):
    print(f"Processing login for user: {username} with password: {password}")  # Logging sensitive data
    user_data = fetch_user_data(username)
    if user_data and user_data["password"] == password:
        return f"Login successful for user: {username} with role: {user_data['role']}"
    else:
        return "Login failed."  # No specific error provided

# 6. Insecure encryption and decryption (BUGGY AND WEAK)
def handle_encryption(data):
    encrypted = weak_encrypt(data)
    print(f"Encrypted data: {encrypted}")  # Exposing encrypted data
    return encrypted

# 7. Handling private key insecurely
def insecure_private_key_usage():
    print(f"Using exposed private key: {PRIVATE_KEY}")  # BAD: Exposing private key
    # Simulating insecure private key usage (this doesn't even do anything useful)
    return f"Processed private key: {PRIVATE_KEY}"

# 8. Poor error handling and exposing secrets
def bad_secret_usage():
    try:
        print("Attempting to access secrets...")
        if not SECRET_KEY:
            raise ValueError("No secret key found!")  # Raising an error (BAD EXAMPLE)
        print(f"Using secret key: {SECRET_KEY}")  # Exposing sensitive data (BAD PRACTICE)
    except Exception as e:
        print(f"Error accessing secret: {e}")  # Broad exception handling (BAD PRACTICE)

# 9. Insecure file handling (exposing secrets in file output)
def insecure_file_operations():
    # Writing sensitive information to a file
    with open("secrets.txt", "w") as file:
        file.write(f"API_KEY: {API_KEY}\n")  # Writing API key in plain text (BAD)
        file.write(f"PRIVATE_KEY: {PRIVATE_KEY}\n")  # Writing private key in plain text (BAD)
        file.write(f"DATABASE_PASSWORD: {DATABASE_PASSWORD}\n")  # Writing database password (BAD)
    print("Sensitive data written to file (insecurely).")

if __name__ == "__main__":
    # 10. Weak login system
    print(process_login("admin", "plaintextpassword"))  # Success (Hardcoded values, no security)
    print(process_login("user", "wrongpassword"))  # Fail (No detailed error)

    # 11. Making insecure API calls
    insecure_api_call("https://jsonplaceholder.typicode.com/posts")  # Exposing API key in request

    # 12. Handling weak encryption
    handle_encryption("Sensitive information to encrypt")  # Weak encryption process

    # 13. Exposing and using private key
    insecure_private_key_usage()  # Exposes private key in plain text

    # 14. Using secrets with bad practices
    bad_secret_usage()  # Exposes secret key

    # 15. Insecure file operations (exposing sensitive info)
    insecure_file_operations()
