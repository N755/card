from typing import List
from faker import Faker
fake = Faker()

class Contact:
    def __init__(self, first_name: str, last_name: str, email: str, phone_number: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
   
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.email}"
   
    @property
    def lenght(self) -> int:
        return len(self.first_name) + len(self.last_name)

card = Contact(first_name="David", last_name="Kyler", email="kylerd@gmail.com", phone_number = '123456789')
card2 = Contact(first_name="Brain", last_name="Coyle", email="coyle1234@gmail.com", phone_number = '987654321')
card3 = Contact(first_name="Helen", last_name="Ames", email="helenka@gmail.com", phone_number = '123789456')
card4 = Contact(first_name="Barbara", last_name="Hassan", email="barbi24@gmail.com", phone_number = '456789123')
card5 = Contact(first_name="Albert", last_name="Tryon", email="tryon@gmail.com", phone_number = '321654987')
my_contacts = [card,card2,card3,card4,card5]


class BaseContact(Contact):
    def __init__(self, first_name: str, last_name: str, company: str, job: str, email: str, phone_number: str) -> None:
        super().__init__(first_name, last_name, email, phone_number)
        self.company = company
        self.job = job

card1 = BaseContact(first_name="David", last_name="Kyler", company="Apple", job="manager", email="kylerd@gmail.com", phone_number = '123456789')
card2 = BaseContact(first_name="Brain", last_name="Coyle", company="Google", job="director",email="coyle1234@gmail.com", phone_number = '987654321')
card3 = BaseContact(first_name="Helen", last_name="Ames", company="Food", job="driver", email="helenka@gmail.com", phone_number = '123789456')
card4 = BaseContact(first_name="Barbara", last_name="Hassan", company="Animal", job="accountant", email="barbi24@gmail.com", phone_number = '456789123')
card5 = BaseContact(first_name="Albert", last_name="Tryon", company="Google", job="cleaner",email="tryon@gmail.com", phone_number = '321654987')
my_contacts = [card1,card2,card3,card4,card5]


class BusinessContact(BaseContact): 
    def __init__(self, first_name: str, last_name: str, company: str, job: str, email: str, phone_number: str, job_phone_number:str) -> None:
        super().__init__(first_name, last_name, company, job, email, phone_number)
        self.job_phone_number = job_phone_number

card1 = BusinessContact(first_name="Anna", last_name="Kyler", company="Apple", job="manager", email="kylerd@gmail.com", phone_number = '123456789', job_phone_number = '985236417')
card2 = BusinessContact(first_name="Brain", last_name="Coyle", company="Google", job="director",email="coyle1234@gmail.com", phone_number = '987654321', job_phone_number = '985236417')
card3 = BusinessContact(first_name="Helen", last_name="Ames", company="Food", job="driver", email="helenka@gmail.com", phone_number = '123789456', job_phone_number = '985236417')
card4 = BusinessContact(first_name="Barbara", last_name="Hassan", company="Animal", job="accountant", email="barbi24@gmail.com", phone_number = '456789123', job_phone_number = '985236417')
card5 = BusinessContact(first_name="Albert", last_name="Tryon", company="Google", job="cleaner",email="tryon@gmail.com", phone_number = '321654987', job_phone_number = '985236417')
my_contacts = [card1,card2,card3,card4,card5]
for card in  my_contacts:
   print(f'{card}, {card.lenght}')

def contact(self) -> str:
        name_for_commun = input("Будь ласка, введіть ім'я зі списку: ")
        for contact in my_contacts:
         if contact.first_name == name_for_commun:
            print (f"Зв'язуюся з {contact.first_name} {contact.last_name}, {contact.email}")
contact(my_contacts)          

def create_contacts() -> List:
    type_card = input('Please enter type card: base or business: ')
    quantity_card = int(input('Enter quantity of cards: '))
    if type_card == 'base':
        contact_list = []
        for i in range(quantity_card):
            card = {fake.first_name(), fake.last_name(), fake.company(), fake.job(), fake.email(), fake.phone_number()}
            contact_list.append(card)
        print( contact_list)
    elif type_card == 'business':
        contact_list = []
        for i in range(quantity_card):
            card = {fake.first_name(), fake.last_name(), fake.company(), fake.job(), fake.email(), fake.phone_number(), fake.company_email()}
            contact_list.append(card)
        print( contact_list)
        return

create_contacts()
contact_list = []

