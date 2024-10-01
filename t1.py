import hashlib
import json

class UserManager:
    def __init__(self):
        self.users = {}  # Bad practice: Should use a database instead of in-memory storage

    def register_user(self, username, password):
        # Bad practice: No input validation, no error handling
        if username in self.users:
            print("User already exists!")  # Bad practice: Use exceptions instead
            return False
        
        hashed_password = self.hash_password(password)
        self.users[username] = hashed_password
        print(f"User {username} registered successfully.")
        return True

    def hash_password(self, password):
        # Bad practice: Using a simple hash, should use a stronger hashing algorithm with salt
        return hashlib.sha256(password.encode()).hexdigest()

    def login_user(self, username, password):
        # Bad practice: No input validation, no error handling
        if username not in self.users:
            print("User does not exist!")  # Bad practice: Use exceptions instead
            return False
        
        hashed_password = self.hash_password(password)
        if self.users[username] == hashed_password:
            print(f"User {username} logged in successfully.")
            return True
        else:
            print("Invalid password!")
            return False

    def save_users_to_file(self, file_path):
        with open(file_path, 'w') as f:  # Bad practice: No error handling for file I/O
            json.dump(self.users, f)
            print(f"Users saved to {file_path}.")

    def load_users_from_file(self, file_path):
        try:
            with open(file_path, 'r') as f:  # Bad practice: No error handling for file I/O
                self.users = json.load(f)
                print(f"Users loaded from {file_path}.")
        except FileNotFoundError:
            print("File not found. No users loaded.")  # Bad practice: Should handle this properly


# Example usage
if __name__ == "__main__":
    manager = UserManager()
    
    # Bad practice: Hardcoding values; should take input from the user or a config file
    manager.register_user("alice", "password123")
    manager.register_user("bob", "securepassword")
    
    # Bad practice: No input validation
    manager.login_user("alice", "password123")
    manager.login_user("bob", "wrongpassword")

    # Bad practice: No cleanup or confirmation for saving/loading
    manager.save_users_to_file("users.json")
    manager.load_users_from_file("users.json")
