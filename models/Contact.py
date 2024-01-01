class Contact:
    def __init__(self, user, country_code, phone_number):
        self.user = user
        self.country_code = country_code
        self.phone_number = phone_number

    def __repr__(self):
        return f"Contact({self.user.name}, {self.country_code}, {self.phone_number})"

    def __str__(self):
        return f"Contact({self.user.name}, {self.country_code}, {self.phone_number})"