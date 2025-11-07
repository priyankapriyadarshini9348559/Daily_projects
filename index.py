contacts=[]
while True:
    print("\ncontact  book Menu")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice=input("enter your choice:")
    if choice =="1":
        name=input("enter your name :")
        phone_num=input("enter your phone number:")
        email=input("enter your email:")
        contacts.extend((name,phone_num,email))
        print("contacts added",contacts)
    elif choice=="2":
        if not contacts:
            print("no contancts available")
        else:
            print("all contacts",contacts)
    elif choice=="3":
        user_choice=input("enter a name")
        if user_choice in contacts:
            print(f" the name :{user_choice} you serach in conatct book is present")
        else:
            print(f"the name {user_choice} you search here is not present")
    elif choice=="4":
        print("you want to update  people here:")
        print("what you want to change here,person's \n 1.name \n2. number \n 3. email")
        user_update=input("enter what you want to change:")
        if user_update=="1":
            updated_name=input("enter the new name:")
            contacts[0]=updated_name
        
        elif user_update =="2":
            updated_num=input("enter the new phone number:")
            contacts[1]=updated_num
        elif user_update=="3":
            updated_email=input("enter the new email:")
            contacts[2]=updated_email
        print(contacts)
    elif choice=="5":
        print('you want to delete the file!!')
        del contacts
        print("your file is deleted",contacts)
    else:
        print("EXIT")
    break           
        
    
