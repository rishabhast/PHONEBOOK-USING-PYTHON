class PhoneBook():
    def __init__(self):
        self.phonebk = {}
        operation = input("choose the operation you want to perform (ADD, SEARCH, UPDATE & DELETE)\n")
        if operation.lower() == "add" or operation.lower() == "a":
            self.addContact()
        elif operation.lower() == "search" or operation.lower() == "s":
            self.searchContact()
        elif operation.lower() == "update" or operation.lower() == "u":
            self.upadateContact()
        elif operation.lower() == "delete" or operation.lower() == "d":
            self.deleteContact()
        else:
            print("Enter valid Choice")
            self.againOperation()

    def againOperation(self):
        request = input("do you want to perform another operation: YES or NO ?\n")
        if request.lower() == "yes" or request.lower() == "y":
            self.operation = input("choose the operation you want to perform (ADD, SEARCH, UPDATE & DELETE)\n")
            if self.operation.lower() == "add" or self.operation.lower() == "a":
                self.addContact()
            elif self.operation.lower() == "search" or self.operation.lower() == "s":
                self.searchContact()
            elif self.operation.lower() == "update" or self.operation.lower() == "u":
                self.upadateContact()
            elif self.operation.lower() == "delete" or self.operation.lower() == "d":
                self.deleteContact()
            else:
                print("Enter valid Choice")
                self.againOperation()
        else:
            print("Thank you for using this PhoneBook")

    def addContact(self):
        name = input("Please enter the Name\n")
        if name.title() in self.phonebk.keys():
            print("Contact already exists")
            self.againOperation()
        else:
            contactNum = input("Please enter Contact Number\n")
            if contactNum.isnumeric() == True and contactNum not in self.phonebk.values() and len(contactNum)==10:
                self.phonebk.update({name.title():contactNum})
                print("Contact added successfully")
                self.againOperation()
            elif contactNum.isnumeric() == True and contactNum in self.phonebk.values():
                print("Contact number already associated with other contact")
                self.againOperation()
            else:
                print("Enter a valid 10 digit Number")
                self.againOperation()

    def upadateContact(self):
        update = input("Please enter the Name / Number to update\n")
        for i,j in self.phonebk.items():
            if update == i:
                new_name = input("Please enter updated name\n")
                self.phonebk.update({new_name:j})
                del (self.phonebk[i])
                print(new_name,j)
                print(self.phonebk)
                self.againOperation()
            elif update == j:
                new_num = input("Please enter updated number\n")
                self.phonebk.update({i:new_num})
                print(i,new_num)
                print(self.phonebk)
                self.againOperation()
            else:
                Print("Contact not found")
                self.againOperation()

    def searchContact(self):
        search = input("Please enter the Name / Number to search\n")
        for i,j in self.phonebk.items():
            if search.title() == i or search.title() in i:
                print(i,j)
                self.againOperation()
            if search.title() == j or search.title() in j:
                print(i,j)
                self.againOperation()

    def deleteContact(self):
        delete= input("Please enter the name / number to delete\n")
        if len(self.phonebk) == 0:
            print("No Contacts in Phonebook")
            self.againOperation()
        elif delete.title() not in self.phonebk.keys() or delete.title() not in self.phonebk.values():
            print("No Contact exists with {} detail".format(delete))
            self.againOperation()
        else:
            for i,j in self.phonebk.items():
                if delete.title() == i:
                    del(self.phonebk[i])
                    print("Contact deleted successfully")
                    self.againOperation()
                elif delete.title() == j:
                    del(self.phonebk[i])
                    print("Number deleted successfully")
                    self.againOperation()

object = PhoneBook()

