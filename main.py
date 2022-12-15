class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPhone(self):
        return self.phone

    def setPhone(self, phone):
        self.phone = phone

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email        

class PhoneBook:
    def __init__(self, name):
        self.name = name
        self.contacts = [Contact("John Doe", "0000000000", "deadguy@iainthere.com"), Contact("Jane Doe", "0000000111", "deadgal@iainthere.com"), Contact("Jimmy Doe", "0000003333", "deadman@iainthere.com")]

    def getAllContacts(self):
        return self.contacts

    def getContactCount(self):
        return len(self.contacts)

    def addContact(self, contact):
        self.contacts.append(contact)
    
    def viewAllContacts(self):
        for contact in self.getAllContacts():
                print(f"{contact.getName()} {contact.getPhone()} {contact.getEmail()}")


    def askForInput(self):
        print(f"Your phonebook currently has {self.getContactCount()} contacts")
        print("1 -create a contact")
        print("2 -view all contacts")
        print("3 -delete contact")
        print("4 update a contact")
        print("5 -exit")
        return input("Enter Option")

    def handleDelete(self):
        print("How would you like to delete a contact?")
        print("1 -By name")
        print("2 By phone")
        print("3 -By email")
        print("4 -cancel")
        choice = input("Enter option")
        if int(choice) == 1:
            self.deleteByContactName()
        elif int(choice) ==2:
            self.deleteByContactPhone()
        elif int(choice) ==3:
            self.deleteByContactEmail()
        elif int(choice) ==4:
            self.handleChoice(self.askForInput())
        else:
            print("Invalid input.")
            self.handleDelete()

    def handleUpdateChoice(self, contact: Contact):
            print("1 for Name")
            print("2 for Phone")
            print("3 for Email")
            choice = input("Enter Option")
            if int(choice) == 1:
               un = input("What would you like to change the name to?")
               contact.setName(un)
               print("Contact Successfully Updated!")
               self.handleChoice(self.askForInput()) 
            elif int(choice) ==2:
                up = input("What would you like to change the phone to?")
                contact.setPhone(up)
                print("Contact Successfully Updated!")
                self.handleChoice(self.askForInput())

            elif int(choice) ==3:
               ue = input("What would you like to change the email to?")
               contact.setEmail(ue)
               print("Contact Successfully Updated!")
               self.handleChoice(self.askForInput())
            else:
                print("Invalid Choice")
                self.handleUpdateChoice()

    def handleUpdate(self):
        name = input("Which contact would you like to update? (c for cancel)")
        if name == "c":
            self.handleChoice(self.askForInput())
        contact = self.getContactByName(name)
        if contact:
            self.handleUpdateChoice(contact)
        else:
            self.handleUpdate()


    def deleteByContactName(self):
        self.viewAllContacts()
        dn = input("Enter Contact Name(c for cancel)")
        if dn == "c":
            self.handleChoice(self.askForInput())
        contact = self.getContactByName(dn)
        if contact:
            self.contacts.remove(contact)
            print("Contact Successfully Deleted!")
            self.handleChoice(self.askForInput())
        else:
            self.deleteByContactName()
            

    def deleteByContactPhone(self):
        self.viewAllContacts()
        dp = input("Enter Contact Phone(c for cancel)")
        if dp == "c":
            self.handleChoice(self.askForInput())
        contact = self.getContactByPhone(dp)
        if contact:
            self.contacts.remove(contact)
            print("Contact Successfully Deleted!")
            self.handleChoice(self.askForInput())
        else:
            self.deleteByContactPhone()

    def deleteByContactEmail(self):
        self.viewAllContacts()
        de = input("Enter Contact Email(c for cancel)")
        if de == "c":
            self.handleChoice(self.askForInput())
        contact = self.getContactByEmail(de)
        if contact:
            self.contacts.remove(contact)
            print("Contact Successfully Deleted!")
            self.handleChoice(self.askForInput())
        else:
            self.deleteByContactEmail()


    def handleChoice(self, choice):
        if int(choice) == 1:
            self.getContactInfo()
            self.handleChoice(self.askForInput())
        elif int(choice) ==2:
            self.viewAllContacts()
            self.handleChoice(self.askForInput())
        elif int(choice) ==3:
            print("I made it here")
            self.handleDelete()
            self.handleChoice(self.askForInput())
        elif int(choice) ==4:
            self.handleUpdate()
            self.handleChoice(self.askForInput())
        elif int(choice) == 5:
            exit()
        else:
            print("Sorry. That's an invalid choice.")
            self.handleChoice(self.askForInput())
    
    def getContactInfo(self):
        en = input("Enter Name")
        ep = input("Enter Phone Number")
        ee = input("Enter Email")
        c = Contact(en, ep, ee)
        print(f"Created Contact {c.getName()} with phone number {c.getPhone()} with email {c.getEmail()}")
        self.addContact(c)
    
    def getContactByName(self, name):
        for c in self.getAllContacts():
            if c.getName() == name:
                return c
            else:
                print(f"No cantact found with the name {name}")
                return None 

    def getContactByPhone(self, phone):
        for c in self.getAllContacts():
            if c.getPhone() == phone:
                return c
            else:
                print(f"No cantact found with the number {phone}")
                return None

    def getContactByEmail(self, email):
        for c in self.getAllContacts():
            if c.getEmail() == email:
                return c
            else:
                print(f"No cantact found with the name {email}")
                return None
                




def main():
    pb = PhoneBook("mock phone book")
    while True: 
        print("Welcome to your Phone Book")
        # n = input("Enter Phone Book name")
        choice = pb.askForInput()
        pb.handleChoice(choice)
    

    
main()