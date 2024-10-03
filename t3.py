# Example of a very bad, insecure, and buggy Python script

# 1. Hardcoded sensitive credentials and secrets
DATABASE_PASSWORD = "superSecret123"  # Hardcoded password (BAD PRACTICE)
API_KEY = "abc123apikeysupersecret"  # Hardcoded API key (BAD PRACTICE)
PRIVATE_KEY = """
-----BEGIN PRIVATE KEY-----
MIICXQIBAAKBgQCv+bigbadexamplefakeprivatekeywhichislongbutwrong
Y6lOCIxJkLDxJnJ7lf6F8bigerrorpronecodeexposedinplaintextsuperbad
-----END PRIVATE KEY-----
"""  # Exposing private key (HUGE SECURITY RISK)

# 2. Using weak encryption (Insecure)
def weak_encryption(data):
    key = "12345"  # A short, weak key (BAD PRACTICE)
    encrypted_data = "".join(chr(ord(c) ^ ord(k)) for c, k in zip(data, key))
    return encrypted_data

# 3. Poor error handling (missing error checks)
def fetch_from_db(username):
    connection = None  # Not actually connecting to a database
    try:
        # Simulated database query with hardcoded credentials
        print(f"Connecting to the database with password: {DATABASE_PASSWORD}")
        if username == "admin":
            return {"username": username, "role": "admin", "password": "plaintextpassword"}  # BAD: Returning sensitive info
        else:
            # Error: forgot to return anything for non-admin users, causing potential crashes
            print("User not found.")
    except Exception as e:
        # Error: Using broad exception handling (BAD PRACTICE)
        print("An error occurred: ", str(e))

# 4. Unprotected API call (Insecure)
def make_insecure_api_request():
    # Exposes the API key in plain text
    print(f"Making an API request with key: {API_KEY}")
    # Error: No actual API handling or error handling, just logging the sensitive info
    return "API request made, but this does nothing."

# 5. Exposing sensitive data in logs
def process_user_login(username, password):
    # Logging sensitive information (BAD PRACTICE)
    print(f"Processing login for user: {username} with password: {password}")
    # Error: Using plaintext passwords without hashing or validation
    if username == "admin" and password == "admin123":
        print("Admin login successful.")
    else:
        # Error: Incorrect condition check leads to failed logins
        print("Login failed.")

# 6. Insecure encryption and returning raw sensitive data
def process_sensitive_data():
    sensitive_data = "This is super secret data."
    encrypted_data = weak_encryption(sensitive_data)
    print(f"Encrypted sensitive data: {encrypted_data}")  # BAD: Exposing encryption process
    return encrypted_data

# 7. Inefficient and insecure use of private key
def handle_private_key():
    print(f"Handling private key: {PRIVATE_KEY}")  # BAD: Exposing the private key

if __name__ == "__main__":
    # 8. Weak login system with no validation and hardcoded credentials
    process_user_login("admin", "admin123")
    process_user_login("user", "wrongpassword")  # This will fail without any proper reason being given

    # 9. Fetching data with hardcoded credentials and missing checks
    fetch_from_db("admin")
    fetch_from_db("nonexistent_user")

    # 10. Making an insecure API call
    make_insecure_api_request()

    # 11. Processing sensitive data using weak encryption
    process_sensitive_data()

    # 12. Handling private key without protection
    handle_private_key()
