import re

class PasswordChecker:
    def __init__(self, password):
        self.password = password

    def check_length(self):
        return len(self.password) >= 8

    def check_uppercase(self):
        return bool(re.search(r'[A-Z]', self.password))

    def check_lowercase(self):
        return bool(re.search(r'[a-z]', self.password))

    def check_digit(self):
        return bool(re.search(r'\d', self.password))

    def check_special_char(self):
        return bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', self.password))

    def is_strong(self):
        checks = [
            self.check_length(),
            self.check_uppercase(),
            self.check_lowercase(),
            self.check_digit(),
            self.check_special_char()
        ]
        return all(checks)

    def strength_report(self):
        print("Password Strength Report:")
        print(f"Minimum 8 characters: {'✅' if self.check_length() else '❌'}")
        print(f"Contains uppercase: {'✅' if self.check_uppercase() else '❌'}")
        print(f"Contains lowercase: {'✅' if self.check_lowercase() else '❌'}")
        print(f"Contains digit: {'✅' if self.check_digit() else '❌'}")
        print(f"Contains special char: {'✅' if self.check_special_char() else '❌'}")
        print(f"Overall strength: {'Strong ✅' if self.is_strong() else 'Weak ❌'}")

# Example usage
if __name__ == "__main__":
    password = input("Enter a password to check: ")
    checker = PasswordChecker(password)
    checker.strength_report()
