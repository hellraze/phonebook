from .Phonebook import Phonebook


class User:
    def __init__(self, name):
        self.name = name
        self.friends = []
        self.phone_books = {}

    def add_friend(self, name):
        self.friends.append(name)

    def remove_friend(self, name):
        if name in self.friends:
            self.friends.remove(name)
        else:
            print("Friend does not exist")

    def add_phone_book(self, tag):
        if tag not in self.phone_books:
            self.phone_books[tag] = Phonebook(tag)
        else:
            print("Tag already exists")

    def add(self, contact, tag):
        if tag in self.phone_books:
            self.phone_books[tag].add_contact(contact)
        else:
            print("Tag not found")

    def share(self, friend, tag):
        if friend in self.friends and tag in self.phone_books:
            friend.add_phone_book(tag)
            friend.phone_books[tag].contacts.extend(self.phone_books[tag].contacts)
        else:
            print("It's not your friend")
