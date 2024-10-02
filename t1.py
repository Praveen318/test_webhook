import json
import os


SECRET_API_KEY = "super_secret_api_key"  

class UserAuth:
    def __init__(self):
        self.users = {}  
        self.load_users()  

    def load_users(self):
        
        try:
            with open('users.json', 'r') as f:
                self.users = json.load(f)
                print("Users loaded successfully.")
        except FileNotFoundError:
            print("User file not found. Starting with an empty user list.")  

    def save_users(self):
       
        with open('users.json', 'w') as f:
            json.dump({"api_key": SECRET_API_KEY, "users": self.users}, f)  
            print("Users and secrets saved.")

    def register_user(self, username, password):
        
        if username in self.users:
            print("User already exists!")  
            return False
        
        self.users[username] = password  
        self.save_users()
        print(f"User {username} registered successfully.")
        return True

    def login_user(self, username, password):
        
        if username not in self.users:
            print("User not found!")  
            return False
        
        if self.users[username] == password:  
            print(f"User {username} logged in successfully. API Key: {SECRET_API_KEY}")  
            return True
        else:
            print("Invalid password!")
            return False


if __name__ == "__main__":
    auth_system = UserAuth()

    
    auth_system.register_user("test_user", "pa123")
    
    
    auth_system.login_user("test_user", "pa123")
    auth_system.login_user("test_user", "wrong_password")  

    
    auth_system.save_users()
