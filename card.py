from faker import Faker
fake = Faker()
class Contacts:
    def __init__(self, first_name, last_name, company, job, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.job = job
        self.email = email
        self.phone_number = phone_number
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"
    def contact(self):
        name_for_commun = input("Будь ласка, введіть ім'я зі списку: ")
        for contact in my_contacts:
         if contact.first_name == name_for_commun:
            print (f"Зв'язуюся з {contact.first_name} {contact.last_name}, {contact.job}, {contact.email}")
    @property
    def lenght(self):
        return len(self.first_name) + len(self.last_name)

card1 = Contacts(first_name="David", last_name="Kyler", company="Apple", job="manager", email="kylerd@gmail.com", phone_number = 123456789)
card2 = Contacts(first_name="Brain", last_name="Coyle", company="Google", job="director",email="coyle1234@gmail.com", phone_number = 987654321)
card3 = Contacts(first_name="Helen", last_name="Ames", company="Food", job="driver", email="helenka@gmail.com", phone_number = 123789456)
card4 = Contacts(first_name="Barbara", last_name="Hassan", company="Animal", job="accountant", email="barbi24@gmail.com", phone_number = 456789123)
card5 = Contacts(first_name="Albert", last_name="Tryon", company="Google", job="cleaner",email="tryon@gmail.com", phone_number = 321654987)
my_contacts = [card1,card2,card3,card4,card5]

class BaseContact(Contacts):
    def __init__(self, first_name, last_name, company, job, email, phone_number):
         super().__init__(first_name, last_name,company, job, email, phone_number)
         del self.company
         del self.job

    def contact(self):
        name_for_commun = input("Будь ласка, введіть ім'я зі списку: ")
        for contact in my_contacts:
         if contact.first_name == name_for_commun:
            print (f"Я набираю {self.phone_number} і телефоную {contact.first_name} {contact.last_name}")
    @property
    def label_length(self):
        return len(self.first_name) + len(self.last_name)
card1 = Contacts(first_name="David", last_name="Kyler", company="Apple", job="manager", email="kylerd@gmail.com", phone_number = 123456789)
card2 = Contacts(first_name="Brain", last_name="Coyle", company="Google", job="director",email="coyle1234@gmail.com", phone_number = 987654321)
card3 = Contacts(first_name="Helen", last_name="Ames", company="Food", job="driver", email="helenka@gmail.com", phone_number = 123789456)
card4 = Contacts(first_name="Barbara", last_name="Hassan", company="Animal", job="accountant", email="barbi24@gmail.com", phone_number = 456789123)
card5 = Contacts(first_name="Albert", last_name="Tryon", company="Google", job="cleaner",email="tryon@gmail.com", phone_number = 321654987)
my_contacts = [card1,card2,card3,card4,card5]
for card in  my_contacts:
   print(f'{card}, ')#як визвати метод довжини
BaseContact.contact() #????метод контакт


'''class BusinessContact(BaseContact): 
    def __init__(self, *args, job_phone_number, **kwargs):
       super().__init__(*args, job_phone_number, **kwargs)
       self.job_phone_number = job_phone_number
    def contact(self):
        name_for_commun = input("Будь ласка, введіть ім'я зі списку: ")
        for contact in my_contacts:
         if contact.first_name == name_for_commun:
            print (f"Я набираю {self.job_phone_number} і телефоную {contact.first_name} {contact.last_name}")
    @property
    def label_length(self):
        return len(self.first_name) + len(self.last_name)
    
card1 = BusinessContact(first_name="David", last_name="Kyler", company="Apple", job="manager", email="kylerd@gmail.com", phone_number = 123456789, job_phone_number = 985236417)
card2 = BusinessContact(first_name="Brain", last_name="Coyle", company="Google", job="director",email="coyle1234@gmail.com", phone_number = 987654321, job_phone_number = 985236417)
card3 = BusinessContact(first_name="Helen", last_name="Ames", company="Food", job="driver", email="helenka@gmail.com", phone_number = 123789456, job_phone_number = 985236417)
card4 = BusinessContact(first_name="Barbara", last_name="Hassan", company="Animal", job="accountant", email="barbi24@gmail.com", phone_number = 456789123, job_phone_number = 985236417)
card5 = BusinessContact(first_name="Albert", last_name="Tryon", company="Google", job="cleaner",email="tryon@gmail.com", phone_number = 321654987, job_phone_number = 985236417)
my_contacts = [card1,card2,card3,card4,card5]

for contact in my_contacts:
    print(contact)
'''



'''by_first_name = sorted(my_contacts, key=lambda contact: contact.first_name)
for contact in by_first_name:
    print(f"{contact.first_name} {contact.last_name} {contact.email}")

by_last_name = sorted(my_contacts, key=lambda contact: contact.last_name)
for contact in by_last_name:
    print(f"{contact.first_name} {contact.last_name} {contact.email}")

by_email = sorted(my_contacts, key=lambda contact: contact.email)
for contact in by_email:
    print(f"{contact.first_name} {contact.last_name} {contact.email}")'''

'''class Contacts:
    def __init__(fake, first_name, last_name, company, job, email, phone_number):
        fake.first_name = first_name
        fake.last_name = last_name
        fake.company = company
        fake.job = job
        fake.email =  email
        fake.phone_number = phone_number
    def __str__(fake):
        return f"{contact.first_name} {contact.last_name} {contact.email}"
    def contact():
        name_for_commun = input("Будь ласка, введіть імя зі списку: ")
        return f"Звязуюся з {name_for_commun}"
    
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
    print(f"{contact.first_name} {contact.last_name} {contact.email}") #дописати сортування за призвищем та емейлом



def sort_by_first_name(contact):
    return contact.first_name

by_first_name = sorted(my_contacts, key=sort_by_first_name)

for contact in by_first_name:
    print(f"{contact.first_name} {contact.last_name} {contact.email}")'''