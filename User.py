class User:

    def __init__(self):
        self._first_name, self._last_name = self.setName()
        #self._constID = generateID()
        self._emails = self.setEmails()
        #self._phones = setPhones()
        #self._aliases = setAliases()
        #self._paypal = setPaypal()
        #self._username = setUsername()
        #self._password = setPassword()

    def setName(self):
        first, last = input("Please enter your name and press <Enter>: ").split()
        return first, last

    def changeFirst(self):
        self._first_name = input("Please enter your new first name and press <Enter>: ")
        return None

    def changeLast(self):
        self._last_name = input("Please enter your new last name and press <Enter>: ")
        return None

    #def generateID(self):

def setEmails():
    emails = [None]
    try:
        num = int(input("How many emails would you like to add? Press <Enter> when done: "))
    except ValueError:
        print(f"Invalid entry")
        emails = setEmails()
        return set(emails.reverse())
    if num < 1:
        raise ValueError(f"Invalid number of emails.")
        return None
    else:
        for item in range(num):
            emails.append(input(f"Please enter email {num}: "))
        return set(emails.reverse())

    #def setPhones(self):
