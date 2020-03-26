
import os
import pathlib

def menu():
    opt = 1
    while opt != 0:
        print(welcome())
        opt = float(input("type option: "))
        if opt == 1:
            print_option("Access user option.\nType 1.<sub_option>, sub_option = 1, 2, 3, 4, 5, 6")
        elif opt == 1.1:
            registration_user()
        elif opt == 1.2:
            list_user()
        elif opt == 1.3:
            print_option("option {}".format(opt))
        elif opt == 1.4:
            print_option("option {}".format(opt))
        elif opt == 1.5:
            print_option("option {}".format(opt))
        elif opt == 1.6:
            print_option("option {}".format(opt))
        elif opt == 2:
            print_option("Access product option.\nType 2.<sub_option>, sub_option = 1, 2, 3, 4, 5, 6")
        elif opt == 2.1:
            print_option("option {}".format(opt))
        elif opt == 2.2:
            print_option("option {}".format(opt))
        elif opt == 2.3:
            print_option("option {}".format(opt))
        elif opt == 2.4:
            print_option("option {}".format(opt))
        elif opt == 2.5:
            print_option("option {}".format(opt))
        elif opt == 2.6:
            print_option("option {}".format(opt))
        elif opt == 3:
            print_option("option {}".format(opt))
        else:
            print("this is not in options")

    print("finished")

def decor(func):
    def wrap(*args, **kwargs):
        print("-"*70)
        func(*args, **kwargs)
        print("-"*70)
    return wrap

@decor
def print_option(op):
    print(op)

def welcome():
    return """
WELCOME
1 - USER
    1.1 - registration user
    1.2 - list users
    1.3 - search user (with ID)
    1.4 - delete user (with ID)
    1.5 - modify user (with ID)
    1.6 - empty user list
2 - PRODUCTS
    2.1 - registration product
    2.2 - list products
    2.3 - search products (with ID)
    2.4 - delete product (with ID)
    2.5 - modify product (with ID)
    2.6 - empty products list
3 - MAKE SHOP 
0 - EXIT
"""

#option 1.1
# aplicate rawx bt
@decor
def registration_user():
    print("REGISTRATION")
    dl = global_regis("name: ", "surname: ", "email: ", "password: ")
    header_in_line = " ID | NAME | SURNAME | EMAIL | PASSWORD \n{}".format("="*40)
    if pathlib.Path("data_users.txt").exists():
        c = count_items("data_users.txt")
        data_in_line = " {} | {} | {} | {} | {} \n".format(c+1, dl[0],dl[1], dl[2], dl[3])
        create_item("data_users.txt",data_in_line, "a")
    else:
        data_in_line = " {} | {} | {} | {} | {} \n".format(1, dl[0],dl[1], dl[2], dl[3])
        create_item("data_users.txt",data_in_line, "w",initial_text=header_in_line)
#option 1.2
@decor
def list_user():
    print("LIST USERS")
    if pathlib.Path("data_users.txt").exists():
         print("quantity: {}".format(count_items("data_users.txt")))
         view_file("data_users.txt")
    else:
        print("empty list, there are not users")

#option 2.1
def registration_product():
    print("NEW PRODUCT")
    dl = global_regis("name: ", "prize: ", "proveedor: ", "amount: ", "")


def create_item(path_file, list_data, type_in, initial_text=""):
    if type_in == "w":
        f = open(path_file, "w")
        f.write("{}\n{}".format(initial_text, list_data))
        f.close()
        print("registrated")
    elif type_in == "a":
        f = open(path_file, "a")
        f.write(list_data)
        f.close()
        print("registrated")

def view_file(path_file):
    f = open(path_file, "r")
    print(f.read())
    f.close()

def count_items(path_file):

    lt = [k for k in open(path_file)]
    #print(lt)
    c = len(lt)-2
    return c


def global_regis(*args):
    dl = []
    for k in args:
        call = input(k)
        dl.append(call)
    return dl



#registration_user()
menu()
#count_items("data_users.txt")
#global_regis("name: ", "surname: ", "email: ", "pass: ")
#print("amount: {}".format(count_items("data_users.txt")))





    
