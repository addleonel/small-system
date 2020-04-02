
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
            registration_user("data_users.txt")
        elif opt == 1.2:
            list_user("data_users.txt")
        elif opt == 1.3:
            print_option("option {}".format(opt))
        elif opt == 1.4:
            print_option("option {}".format(opt))
            delete_user()
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

# option 1.1
@decor
def registration_user(pf):
    print("REGISTRATION")
    dl = global_regis("name: ", "surname: ", "email: ", "password: ")
    header_in_line = " ID | NAME | SURNAME | EMAIL | PASSWORD \n{}".format("="*40)
    if pathlib.Path(pf).exists():
        c = count_items(pf)
        data_in_line = " {} | {} | {} | {} | {} \n".format(c+1, dl[0],dl[1], dl[2], dl[3])
        create_item(pf, data_in_line, "a")
    else:
        data_in_line = " {} | {} | {} | {} | {} \n".format(1, dl[0],dl[1], dl[2], dl[3])
        create_item(pf, data_in_line, "w", initial_text=header_in_line)
# option 1.2
@decor
def list_user(pf):
    print("LIST USERS")
    if pathlib.Path(pf).exists():
         print("quantity: {}".format(count_items(pf)))
         view_file(pf)
    else:
        print("empty list, there are not users")

# option 1.4
def delete_user(pf):
    print("\033[1;34;1m DELETE USER")
    if pathlib.Path(pf).exists():
        delete_item(pf)





# option 2.1
def registration_product():
    print("NEW PRODUCT")
    dl = global_regis("name: ", "prize: ", "proveedor: ", "amount: ", "")

# modify current
def delete_item(path_file, the_id):
    # c = count_items(path_file)
    i = the_id + 1
    lt = [k for k in open(path_file)]
    print(lt[i])
    question = input("delete (y, n):")
    if question in ('y', 'yes', 'yep'):
        if lt[i][1] == str(the_id):
            # rawx tb
            with open(path_file, "r") as f:
                line = f.readline()
                print(line)
            #with open(path_file, "w") as f:
            #    for li in line:
             #       if li.strip("\n") != lt[i]:
              #          f.write(li)
            print("deleted")
    elif question in ('n', 'no', 'not'):
        pass
        print("no changed nothing")


def create_item(path_file, list_data, type_in, initial_text=""):
    if type_in == "w":
        f = open(path_file, "w")
        f.write("{}\n{}".format(initial_text, list_data))
        f.close()
        print("registered")
    elif type_in == "a":
        f = open(path_file, "a")
        f.write(list_data)
        f.close()
        print("registered")

def view_file(path_file):
    f = open(path_file, "r")
    print(f.read())
    f.close()

def count_items(path_file):
    lt = [k for k in open(path_file)]
    # print(lt)
    c = len(lt)-2
    return c


def global_regis(*args):
    dl = []
    for k in args:
        call = input(k)
        dl.append(call)
    return dl


# registration_user()
delete_item("data_users.txt", 2)
# menu()
# count_items("data_users.txt")
# global_regis("name: ", "surname: ", "email: ", "pass: ")
# print("amount: {}".format(count_items("data_users.txt")))





    
