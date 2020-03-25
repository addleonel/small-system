
import os
import pathlib

def menu():
    opt = 1
    while opt != 0:
        print(welcome())
        opt = int(input("type option: "))
        if opt == 1:
            registration_user()
        elif opt == 2:
            list_user()
        elif opt == 3:
            print("option 3")
        elif opt == 4:
            print("option 4")
        elif opt == 5:
            print("option 5")
        else:
            print("this is not in options")

    print("finished")

def welcome():
    return """
WELCOME
1. registrate user
2. list users
3. registrate product
4. list products
5. make shop
0. exit
"""

#option 1
# aplicate rawx bt
def registration_user():
    print("REGISTRATION")
    dl = global_regis("name: ", "surname: ", "email: ", "password: ")
    header_in_line = "ID | NAME | SURNAME | EMAIL | PASSWORD "
    data_in_line = "{} | {} | {} | {} \n".format(dl[0],dl[1], dl[2], dl[3])
    if pathlib.Path("data_users.txt").exists():
        create_item("data_users.txt",data_in_line, "a")
    else:
        create_item("data_users.txt",data_in_line, "w",initial_text=header_in_line)
#option2
def list_user():
    print("LIST USERS")
    if pathlib.Path("data_users.txt").exists():
         print("quantity: {}".format(count_items("data_users.txt")))
         view_file("data_users.txt")
    else:
        print("empty list, there are not users")

#option3
def registration_product():
    print("NEW PRODUCT")
    dl = global_regis("name: ", "prize: ", "proveedor: ", "amount: ", "")


def create_item(path_file, list_data, type_in, initial_text=""):
    if type_in == "w":
        f = open(path_file, "w")
        f.write("{}\n{}".format(initial_text, list_data))
        f.close()
        print("you already are registrated")
    elif type_in == "a":
        f = open(path_file, "a")
        f.write(list_data)
        f.close()
        print("you already are registrated")

def view_file(path_file):
    f = open(path_file, "r")
    print(f.read())
    f.close()

def count_items(path_file):

    lt = [k for k in open(path_file)]
    return "{}".format(len(lt)-1)

def global_regis(*args):
    dl = []
    for k in args:
        call = input(k)
        dl.append(call)
    return dl



#registration_user()
menu()   
#global_regis("name: ", "surname: ", "email: ", "pass: ")
#print("amount: {}".format(count_items("data_users.txt")))





    
