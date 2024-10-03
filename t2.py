
def weak_encrypt(data):
    key = "static_key"  
    encrypted = "".join(chr(ord(c) ^ ord(k)) for c, k in zip(data, key))
    return encrypted

DB_USERNAME = "admin"  
DB_PASSWORD = "password123"  
API_KEY = "sk_test_supersecretapikey12345"  

PRIVATE_KEY = """
-----BEGIN PRIVATE KEY-----
MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAMJh2yfh3Dey8c+k
Exbadcodefakeprivatekeydata++++++++++++++++++
-----END PRIVATE KEY-----
"""

def connect_to_database():
    connection_string = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@localhost/mydb"
    print(f"Connecting to the database with: {connection_string}")  
    
    return "Database connection established."

def make_unsafe_api_request():
    print(f"Using API Key: {API_KEY}")  
    
    return "API request made."

def show_encryption_method():
    print("Using weak encryption: XOR with static key.")  

def insecure_operation():
    sensitive_data = "super_secret_data"
    encrypted_data = weak_encrypt(sensitive_data)
    print(f"Encrypted data: {encrypted_data}")  
    return encrypted_data

if __name__ == "__main__":
    print("Starting insecure operations...")

   
    connect_to_database()

    
    make_unsafe_api_request()

   
    insecure_operation()

    
    print(f"Exposed private key: {PRIVATE_KEY}")
