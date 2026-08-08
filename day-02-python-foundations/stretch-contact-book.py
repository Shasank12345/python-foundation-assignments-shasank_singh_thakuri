'''Interactive Contact Book
IN this Contact Book it is assumed that one person can have only one contact and is not optimimal code:
''' 

Contact_Book = {}

# function to display menu
def display_menu():
    print('''
......Welcome to Virtual Contact BOOK.....
.....        Choose a Option:      .....
\t'1' for Adding Contact
\t'2' for Searching Contact
\t'3' for Deleting Contact
\t'4' for Displaying all Contacts
\t'5' for Exit
''')
# function to add_contact
def add_contact():
    contact_id = input("Enter the Contact ID (e.g.,CONT-004):").lower().strip()
    #Check for duplicate Contact id 
    if contact_id in Contact_Book:
        print(f"Contact ID '{contact_id}' already exists! Cannot add duplicate.")
        return
    name = (input("Enter the Name : \n ")).lower().strip()
    phn_no = input("Enter the Phone_Number : \n").lower().strip()
    email = input("Enter email address \n ").lower().strip()
    #check for duplicate attributes as contact should be unique 
    for cid, details in Contact_Book.items():
        if details["Name"] == name:
            print(f"Name '{name}' already exists under contact '{cid}'.")
            return
        if details["Phone Number"] == phn_no:
            print(f"Phone number '{phn_no}' already exists under contact '{cid}'.")
            return
        if details["Email"] == email:
            print(f"Email '{email}' already exists under contact '{cid}'.")
            return
    Contact_Book[contact_id] = {
        "Name":name,
        "Phone Number":phn_no,
        "Email":email
    }
#function to search contact
def search_contact(cont_id='', name=' ', phn='', email=''):
    match_id = None
    cont_id=cont_id.lower().strip()
    name=name.lower().strip()
    email=email.lower().strip()
    print(f"Searching For Contact ............")
    for contact_id, contact_info in Contact_Book.items():
        if (cont_id.lower() and contact_id.lower().strip == cont_id) or \
            (name and contact_info['Name'].lower() == name) or \
           (phn and contact_info['Phone Number'] == phn) or \
           (email and contact_info['Email'] == email):
            match_id = contact_id
    if match_id:
        display_contact(cont_id, name, phn, email)
    else:
        print("Sorry! The Contact you searched for doesnt exist.....")

#function to delete contact
def delete_contact(cont_id='', name='', phn='', email=''):
    print("Searching For Contact to delete ..................")\
    
    match_id = None
    cont_id=cont_id.lower().strip()
    name=name.lower().strip()
    email=email.lower().strip()
    for contact_id, contact_info in Contact_Book.items():
        if (cont_id and contact_id == cont_id) or \
           (name and contact_info['Name'].lower() == name) or \
           (phn and contact_info['Phone Number'] == phn) or \
           (email and contact_info['Email'] == email):
            match_id = contact_id

    if match_id:
        removed = Contact_Book.pop(match_id)
        print(f"Deleted contact: {match_id} - {removed}")
    else:
        print("Sorry! Couldn't find the Contact you want to delete...")

#function to display contact
def display_contact(cont_id='', name='', phn='', email=''):
    cont_id=cont_id.lower().strip()
    name=name.lower().strip()
    email=email.lower().strip()
    print("Displaying Contact............")
    if not (cont_id or name or phn or email):
        for cid, details in Contact_Book.items():
            print(f"ID: {cid}")
            for key, value in details.items():
                print(f"  {key}: {value}")
        return

    for cid, details in Contact_Book.items():
        if (cont_id and cid == cont_id) or \
           (name and details.get("name") == name) or \
           (phn and details.get("phn") == phn) or \
           (email and details.get("email") == email):
            print(f"ID: {cid}")
            for key, value in details.items():
                print(f"{key}: {value}")
            print("")



#Start of the program
display_menu()
choice=int(input("Enter Your Choice Consulting the Menu"))
while (choice != 5):
    match choice:
        case 1:
            print("Enter the Details........\n")
            add_contact()
        case 2:
            C = input('''MAKE A CHOICE.....
            "1" if you want to search by contact id
            "2" if you want to search by name
            "3" if you want to search by phone number
            "4: if you want to search by email
            ''')
            match C:
                case '1':
                    search_parameter = input("Enter the contact_id :")
                    search_contact(cont_id=search_parameter)
                case '2':
                    search_parameter = input("Enter the Name :")
                    search_contact(name=search_parameter)
                case '3':
                    search_parameter = input("Enter the Phone Number :")
                    search_contact(phn=search_parameter)
                case '4':
                    search_parameter = input("Enter the Email :")
                    search_contact(email=search_parameter)
                case _:
                    print("Unknown Parameter")
        case 3:
            C = input('''MAKE A CHOICE TO SEARCH THE CONTACT YOU WANT TO DELETE.....
                    "1" if you want to delete by contact id
                    "2" if you want to delete by name
                    "3" if you want to delete by phone number
                    "4: if you want to delete by email
                    ''')
            
            match C:
                case '1':
                        search_parameter = input("Enter the contact_id :")
                        delete_contact(cont_id=search_parameter)
                case '2':
                        search_parameter = input("Enter the Name :")
                        delete_contact(name=search_parameter)
                case '3':
                        search_parameter = input("Enter the Phone Number :")
                        delete_contact(phn=search_parameter)
                case '4':
                        search_parameter = input("Enter the Email :")
                        delete_contact(email=search_parameter)
                case _:
                    print("Unknown Parameter")
        case 4:
            display_contact()
        case 5:
            print("Thanks For Visiting ..................")
            break
        case _:
            print("Invalid Choice, Please Enter the right choice consulting with the Menu")

    c2=input("Do you want to Continue? Say Y or N \n")
    if(c2.lower().strip()=='n'):
        break
    menu=input("Do you want to Display Menu Again? say Y or N \n")
    if(menu.lower()=="y"):
        display_menu()
    choice=int(input("Enter Your Choice Consulting the Menu\n"))  
     

