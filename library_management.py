library = {
    "Python Basics": {"author": "A. Kumar", "copies": 5},
    "Data Science 101": {"author": "s.panda", "copies": 2},
    "Machine Learning": {"author": "R. Verma", "copies": 3}
}
#Display all books with author and available copies.
for book_name,info in library.items():
    print(f"{book_name} : author and availble copies are: {info['author']} - {info['copies']}")
#Issue a book to a student:
user_book=input("whick book you want to take:")
if user_book in library:
    print(f"{user_book} :this book is availble 📔 ")
    info=library[user_book]
# check how many copies are availble for that book
    if info['copies']>0:
        print("the book you want is availble in manty copies ") 
        user_take=int(input("how much book you want to take:"))
        coipies=info["copies"]-user_take
        print("after user take the book the remaining copies are",coipies)

    else:
        print("the book is not availble")
#Return a book:
print(f"you have taken {user_take} books ")
print("the rule is here that you cant kept it for 7 days if you kept more than this you will give fine")
user_kept=int(input("how many days you kept:"))
if user_kept <=7:
    print("you are not giving any fine")
else:
    print("you are giving ₹100 fine")