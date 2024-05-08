class User:
    ENGINEER = "Engineer"
    MANAGER = "Manager"
    UNKNOWN = "Unknown"

    def __init__(self, name, age, user_type, phone, phone_code):
        self.name = name
        self.age = age
        self.user_type = self._validate_user_type(user_type)
        self.phone = phone
        self.phone_code = phone_code

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Type:", self.user_type)
        print("Phone:", self.full_phone_number)

    @property
    def full_phone_number(self):
        return f"{self.phone_code}{self.phone}"

    def _validate_user_type(self, user_type):
        if user_type in [self.ENGINEER, self.MANAGER]:
            return user_type
        else:
            return self.UNKNOWN


user = User("John", 25, User.ENGINEER, "9379992", "050")
user.display_details()