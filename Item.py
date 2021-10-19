def setEmails():
    emails = [None]
    print(type(emails))
    try:
        num = int(input(f"How many emails would you like to add? Press <Enter> when done: "))
    except ValueError:
        print(f"Invalid entry")
        emails = setEmails()
        return set(emails.reverse())
    if num < 1:
        raise ValueError(f"Invalid number of emails.")
        return None
    else:
        for item in range(num):
            emails.append(input(f"Please enter email {num}: ")).reverse()
        return set(emails)
