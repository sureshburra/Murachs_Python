class User:
    def __init__(self, username, email, age=None, phone=None, address=None):
        self.username = username
        self.email = email
        self.age = age
        self.phone = phone
        self.address = address


class UserBuilder:
    def __init__(self):
        self._username = None
        self._email = None
        self._age = None
        self._phone = None
        self._address = None

    def username(self, username):
        self._username = username
        return self

    def email(self, email):
        self._email = email
        return self

    def age(self, age):
        self._age = age
        return self

    def phone(self, phone):
        self._phone = phone
        return self

    def address(self, address):
        self._address = address
        return self

    def build(self):
        if not self._username or not self._email:
            raise ValueError("username and email are required.")
        return User(self._username, self._email, self._age, self._phone, self._address)


user = UserBuilder().username("alice").email("alice@example.com").age(30).build()
print(user.username)
