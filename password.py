class InvalidLoginError(Exception):
    pass
class AccountLockedError(Exception):
    pass
class LoginSystem:
    def __init__(self):
        print("Create Account")
        self.username = input("Set Username: ")
        self.password = input("Set Password: ")
    def login(self):
        attempts = 0
        max_attempts = 3
        while attempts < max_attempts:
            try:
                user = input("\nEnter Username: ")
                pwd = input("Enter Password: ")

                if user != self.username or pwd != self.password:
                    attempts += 1
                    raise InvalidLoginError
                print("Login Successful")
                return
            except InvalidLoginError:
                print("Invalid Username or Password")

        raise AccountLockedError
try:
    l = LoginSystem()
    l.login()
except AccountLockedError:
    print("Account Locked! Too many attempts")
