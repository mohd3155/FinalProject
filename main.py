from library import *

myBook = ""
bookStatus = ""


def userName():
    who = input("are you a Client or an Librarian")
    return who


clients_list: list[Client] = []
librarians_list: list[Librarian] = []
books_list: list[Book] = []
bowrroedOrders_list: list[Borrowing_order] = []
counter = 0


def add_new_client():
    global counter
    clients_list.append(
        Client(id=counter, name=input("please enter your name"), age=int(input("please enter your age")),
               ide=int(input("please enter your identification num")),
               phone=int(input("please enter your phone number"))))
    counter += 1


def add_new_lib():
    global counter
    librarians_list.append(
        Librarian(id=counter, name=input("please enter your name"), age=int(input("please enter your age")),
                  ide=int(input("please enter your identification num")),
                  empType=input("please enter your work time type(Full/part) ")))
    counter += 1


if userName() == "client":
    add_new_client()
elif userName() == "Librarian":
    add_new_lib()
else:
    print("Undefined")
    quit()


book1 = Book(id=1, title="History", desc="short brief of history", author="Ron Chernow", status="available")
books_list.append(book1)

book2 = Book(id=2, title="politics", desc="short brief of politics", author="Elizabeth A. Fenn", status="Un-available")
books_list.append(book2)

book3 = Book(id=3, title="biology", desc="short brief of biology", author="Jared Diamond", status="available")
books_list.append(book3)

print("Books in our system")

for item in books_list:
    print(item.get_id(), "-", item.get_title(), "is about a", item.get_desc())
    continue


def chooseBook():
    global myBook
    global bookStatus
    myBook = int(input("Which book you would like to borrow?, Please choose by Id number"))

    for book in books_list:
        if book.get_id() == myBook:
            bookStatus = book.get_status()
            if bookStatus == "available":
                print("this book is available ")
                clientId1 = int(input("please enter you identification no"))
                for things in clients_list:
                    global counter
                    if clientId1 == things.get_ide():
                        order1 = Borrowing_order(id=counter, date="7/1/2022", clientId=int(clientId1), bookId=int(myBook),
                                                 status="Active")
                        bowrroedOrders_list.append(order1)
                        counter = +1
                        print("your Borrowing order has bees issued ")
            else:
                print("Un-available")
                quit()


chooseBook()

search = input("do you want to search for an order, ans yes or no")

if search == "yes":
    for order in bowrroedOrders_list:
        print("ID order:",order.get_id())
else:
    print("Thank you for using our website")
    quit()
