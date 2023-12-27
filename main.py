from models.User import User
from models.Admin import Admin
from models.Contact import Contact

user1 = User("Alice")
user2 = User("Bob")
admin = Admin(user1)


user1.add_friend(user2)


contact1 = Contact(user1, "+1", "555-1234")
user1.add_phone_book("family")
user1.add(contact1, "family")


contact2 = Contact(user2, "+1", "555-5678")
admin.add_contact_to_phone_book(contact2, user1.phone_books["family"])


user1.share(user2, "family")


print(repr(user2.phone_books["family"].contacts))
