from .User import User


class Admin(User):
    @staticmethod
    def add_contact_to_phone_book(contact, phone_book):
        phone_book.add_contact(contact)

    @staticmethod
    def remove_contact_from_phone_book(contact, phone_book):
        phone_book.remove_contact(contact)
