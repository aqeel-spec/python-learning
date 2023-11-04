from typing import Any

class User():
    def __init__(self,first_name : str,last_name : str , **more):
        self.first_name : str =first_name
        self.last_name : str =last_name
        self.age : int =more.get('age',0)
        self.city : str =more.get('city','')
        # add an attribute for login_attempts
        self.login_attempts : int = 0
        
         # attribute to store list of privileges 
        self.privileges : list[str] = ["can add post", "can delete post", "can ban user "]


    
    def describe_user(self):
        print(f"First Name : {self.first_name}")
        print(f"Last Name : {self.last_name}")
        print(f"Age : {self.age}")
        print(f"City : {self.city}")

    
    def greet_user(self):
        print(f"\nWelcome {self.first_name} {self.last_name}!")
    
    # method that increments login_attempts by 1
    def increment_login_attempts(self):
        self.login_attempts += 1

    # another method that resets login_attempts to 0
    def reset_login_attempts(self):
        self.login_attempts = 0

    # method that shows adminiter privileges
    def show_privileges(self):
        print(f"Admin has following privileges : {self.privileges}")

class Privileges():
    def __init__(self,privileges : list[str] = []):
        self.privileges : list[str] = privileges
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self,first_name : str,last_name : str , **more):
        super().__init__(first_name,last_name,**more)
        privileges_instance : Privileges = Privileges(privileges=["can add post","can delete post","can ban user"])
        self.privileges : Any = privileges_instance
         