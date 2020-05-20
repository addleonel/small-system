
import os
import pathlib
import time
from tools import *

def menu():
    FILE_USERS = ".data_users.txt"
    RECYCLE_USER_IN = ".recycle_users.txt"
    opt = 1
    while opt != 0:
        try:
            print(welcome())
            opt = float(input("type option: "))
        except (ValueError, NameError, SyntaxError):
            print("This value is not define, type correct option ...")
        else:
            if opt == 1:
                print_option("Access user option.\nType 1.<sub_option>, sub_option = 1, 2, 3, 4, 5, 6, 7")
            elif opt == 1.1:
                registration_user(FILE_USERS, RECYCLE_USER_IN, "name", "surname", "age", "email", "password")
            elif opt == 1.2:
                list_user(FILE_USERS)
            elif opt == 1.3:
                search_user(FILE_USERS, "name", "surname", "age", "email", "password")
            elif opt == 1.4:
                delete_user(FILE_USERS, RECYCLE_USER_IN)
            elif opt == 1.5:
                modify_user(FILE_USERS, RECYCLE_USER_IN, "name", "surname", "age", "email", "password")
            elif opt == 1.6:
                empty_users(FILE_USERS)
            elif opt == 1.7:
                view_history_user(RECYCLE_USER_IN)
            elif opt == 0:
                print("thanks")
            else:
                print("this is not in options")
        finally:
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
    1.7 - history
0 - EXIT
"""

# option 1.1
@decor
def registration_user(pf, path_recycle, *args):
    print("REGISTRATION")
    dl = global_regis(*args)
    header_in_line = " ID "
    for k in args:
        col = k.upper()
        header_in_line += "| {} ".format(col)
    else:
        header_in_line += "\n{}".format("="*40)

    if pathlib.Path(pf).exists():
        c = count_items(pf)
        data_in_line = " {} ".format(c+1)
        for k in dl:
            data_in_line += "| {} ".format(k)
        else:
            data_in_line += "\n"
        create_item(pf, data_in_line, "a", path_recycle)
    else:
        data_in_line = " {} ".format(1)
        for k in dl:
            data_in_line += "| {} ".format(k)
        else:
            data_in_line += "\n"
        create_item(pf, data_in_line, "w", path_recycle, initial_text=header_in_line)

# option 1.2
@decor
def list_user(pf):
    print("LIST USERS")
    MESSAGE_USER_DELETED = "user deleted"
    if pathlib.Path(pf).exists():
        c = 0
        with open(pf) as f:
            lines = f.readlines()
            for line in lines:
                if line.rstrip("\n").lstrip() == MESSAGE_USER_DELETED:
                    c += 1
        print("quantity: {}".format(count_items(pf)-c))
        view_file(pf)
    else:
        print("empty list, there are not users")

# option 1.3
@decor
def search_user(pf, *args):
    print("SEARCH USERS")
    if pathlib.Path(pf).exists():
        try:
            user_id = int(input("Type user's ID: "))
        except (ValueError, NameError, SyntaxError):
            print("This value is not define, please try again ...")
        else:
            r = search_item(pf, user_id)
            if str(user_id) in r:
                i = 0
                show = "ID: {}\n".format(r[i])
                for k in args:
                    i += 1
                    v = k.upper()
                    show += "{}: {}\n".format(v, r[i])
                print(show)
            else:
                print(r)
    else:
        print("There are not users, register one")

# option 1.4
@decor
def delete_user(pf, path_recycle):
    print("DELETE USER")
    if pathlib.Path(pf).exists():
        delete_item(pf, "Type user's ID: ", path_recycle, "user deleted")
    else:
        print("There are not users, register one")

# option 1.5
@decor
def modify_user(pf, path_recycle, *args):
    print("MODIFY USERS")
    if pathlib.Path(pf).exists():
        # path_file, message, list_data, type_in, recycle_in)
        modify_item(pf, "type the user's ID: ", path_recycle, *args)
    else:
        print("There are not users")

# option 1.6
@decor
def empty_users(pf):
    print("EMPTY USER LIST")
    if pathlib.Path(pf).exists():
        m = input("Are you sure what you want to empty? (y/n): ")
        if m in ('y', 'Y', 'yes', 'yeah', 'yep'):
            empty_list(pf)
            print("OK, your list is empty now")
        elif m in ('n', 'N', 'no', 'not'):
            print("no changed nothing")
        else:
            print("It's not the option, type \'y\' or \'n\'")
    else:
        print("There are not users, register one ...")

# option 1.7
@decor
def view_history_user(path_recycle):
    print("HISTORY USERS")
    view_file(path_recycle)


if __name__ == '__main__':
    menu()
