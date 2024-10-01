import json
import os

# Exposing sensitive data
SECRET_API_KEY = "super_secret_api_key"  # Bad practice: Hardcoding sensitive information

class UserAuth:
    def __init__(self):
        self.users = {}  # Bad practice: Using an in-memory dictionary for user storage
        self.load_users()  # Bad practice: Not checking for errors during loading

    def load_users(self):
        # Bad practice: No error handling for file operations
        try:
            with open('users.json', 'r') as f:
                self.users = json.load(f)
                print("Users loaded successfully.")
        except FileNotFoundError:
            print("User file not found. Starting with an empty user list.")  # Bad practice: No specific error handling

    def save_users(self):
        # Bad practice: Exposing secrets in the saved file
        with open('users.json', 'w') as f:
            json.dump({"api_key": SECRET_API_KEY, "users": self.users}, f)  # Bad practice: Storing secrets
            print("Users and secrets saved.")

    def register_user(self, username, password):
        # Bad practice: No validation on username or password
        if username in self.users:
            print("User already exists!")  # Bad practice: Should raise an exception instead
            return False
        
        self.users[username] = password  # Bad practice: Storing plaintext passwords
        self.save_users()
        print(f"User {username} registered successfully.")
        return True

    def login_user(self, username, password):
        # Bad practice: No error handling and no input validation
        if username not in self.users:
            print("User not found!")  # Bad practice: Should raise an exception instead
            return False
        
        if self.users[username] == password:  # Bad practice: Checking against plaintext password
            print(f"User {username} logged in successfully. API Key: {SECRET_API_KEY}")  # Exposing secret in logs
            return True
        else:
            print("Invalid password!")
            return False

# Example usage
if __name__ == "__main__":
    auth_system = UserAuth()

    # Hardcoded test user, exposing potential security vulnerabilities
    auth_system.register_user("test_user", "password123")
    
    # Logging in with hardcoded credentials
    auth_system.login_user("test_user", "password123")
    auth_system.login_user("test_user", "wrong_password")  # Bad practice: No proper feedback for invalid attempts

    # Bad practice: No cleanup or checks for saving/loading user data
    auth_system.save_users()
