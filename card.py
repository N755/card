from faker import Faker
fake = Faker()
'''class Contacts:
     def __init__(self, name, surname, company_name, position, mail):
        self.name = name
        self.surname = surname
        self.company_name = company_name
        self.position = position
        self. mail =  mail
card1 = Contacts(name="David", surname="Kyler", company_name="Apple", position="manager", mail="kylerd@gmail.com")
card2 = Contacts(name="Brain", surname="Coyle", company_name="Google", position="director", mail="coyle1234@gmail.com")
card3 = Contacts(name="Helen", surname="Ames", company_name="Food", position="driver", mail="helenka@gmail.com")
card4 = Contacts(name="Barbara", surname="Hassan", company_name="Animal", position="accountant", mail="barbi24@gmail.com")
card5 = Contacts(name="Albert", surname="Tryon", company_name="Google", position="cleaner", mail="tryon@gmail.com")
my_contacts = [card1,card2,card3,card4,card5]
for contact in my_contacts:
    print(f"{contact.name} {contact.surname} {contact.mail}")

by_first_name = sorted(my_contacts, key=lambda contact: contact.name)
for contact in by_first_name:
    print(f"{contact.name} {contact.surname} {contact.mail}")

by_last_name = sorted(my_contacts, key=lambda contact: contact.surname)
for contact in by_last_name:
    print(f"{contact.name} {contact.surname} {contact.mail}")

by_email = sorted(my_contacts, key=lambda contact: contact.mail)
for contact in by_email:
    print(f"{contact.name} {contact.surname} {contact.mail}")'''

class Contacts:
    def __init__(fake, first_name, last_name, company, job, email, phone_number):
        fake.first_name = first_name
        fake.last_name = last_name
        fake.company = company
        fake.job = job
        fake.email =  email
        fake.phone_number = phone_number
    def __str__(fake):
        return f"{contact.first_name} {contact.last_name} {contact.email}"
    
card1 = Contacts(fake.first_name(), fake.last_name(), fake.company(), fake.job(), fake.email(), fake.phone_number())
card2 = Contacts(fake.first_name(), fake.last_name(), fake.company(), fake.job(), fake.email(), fake.phone_number())
card3 = Contacts(fake.first_name(), fake.last_name(), fake.company(), fake.job(), fake.email(), fake.phone_number())
card4 = Contacts(fake.first_name(), fake.last_name(), fake.company(), fake.job(), fake.email(), fake.phone_number())
card5 = Contacts(fake.first_name(), fake.last_name(), fake.company(), fake.job(), fake.email(), fake.phone_number())
my_contacts = [card1, card2, card3, card4, card5]
for contact in my_contacts:
    print(contact)

by_first_name = sorted(my_contacts, key=lambda contact: contact.first_name)
for contact in by_first_name:
    print(f"{contact.first_name} {contact.last_name} {contact.email}")

'''def sort_by_first_name(contact):
    return contact.first_name

by_first_name = sorted(my_contacts, key=sort_by_first_name)

for contact in by_first_name:
    print(f"{contact.first_name} {contact.last_name} {contact.email}")'''