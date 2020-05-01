
import os
import time

# empty list
def empty_list(path_file):
    if os.path.exists(path_file):
        os.remove(path_file)

# delete item with id
def delete_item(path_file, message_id, recycle_in):
    # c = count_items(path_file)
    try:
        the_id = int(input(message_id))
        i = the_id + 1
        lt = [k for k in open(path_file)]
        print(lt[i])

    except (ValueError, NameError, SyntaxError, IndexError):
        print("It's not define")
    else:
        question = input("delete (y/n):")
        if question in ('y', 'Y', 'yes', 'yep', 'yeah'):
            if lt[i][1] == str(the_id):
                # rawx tb
                with open(path_file, "r") as f:
                    lines = f.readlines()  # it's an array

                with open(path_file, "w") as f:
                    for line in lines:
                        if line.strip("\n")[1] != str(the_id):
                            f.write(line)
                        else:
                            with open(recycle_in, "a") as m:
                                m.write("\n{}\n".format(time.asctime()) + "deleted user\n{}".format(line))
                            f.write("     user deleted\n")

                print("deleted")
        elif question in ('n', 'N', 'no', 'not'):
            print("no changed nothing")
        else:
            print("type \'y\' or \'n\'")

# search item with id
def search_item(path_file, the_id):
    try:
        i = the_id + 1
        lt = [k for k in open(path_file)]
        if str(the_id) not in lt[i]:
            return "This ID is deleted"
        else:
            e = lt[i].strip().split(' | ')
            return e
    except (ValueError, NameError, SystemError, TypeError, IndexError):
        return "This ID is not define"

# create item with id
def create_item(path_file, list_data, type_in, recycle_in, initial_text=""):
    if type_in == "w":
        with open(path_file, "w") as f:
            f.write("{}\n{}".format(initial_text, list_data))
            print("registered")
        # reclycle data in
        with open(recycle_in, "a") as f:
            f.write("\n{}\n{}\n{}".format(time.asctime(), initial_text, list_data))
    elif type_in == "a":
        with open(path_file, "a") as f:
            f.write(list_data)
            print("registered")
        # recycle data in
        with open(recycle_in, "a") as f:
            f.write("\n{}\n".format(time.asctime()) + list_data)

# modify item with id
def modify_item(path_file, message, recycle_in, *args):
    try:
        the_id = int(input(message))
        i = the_id + 1
        lt = [k for k in open(path_file)]
        print(lt[i])
    except (ValueError, SyntaxError, NameError, IndexError):
        print("It's not define, try again ...")
    else:
        question = input("Are you sure what you want to modify this user? (y/n): ")
        if question in ('y', 'Y', 'yes', 'yep', 'yeah'):
            if lt[i][1] == str(the_id):
                # rawx tb
                with open(path_file, "r") as f:
                    lines = f.readlines()  # it's an array

                with open(path_file, "w") as f:
                    for line in lines:
                        if line.strip("\n")[1] != str(the_id):
                            f.write(line)
                        else:
                            dl = global_regis(*args)
                            data_in_line = " {} ".format(the_id)
                            for k in dl:
                                data_in_line += "| {} ".format(k)
                            else:
                                data_in_line += "\n"
                            with open(recycle_in, "a") as m:
                                m.write("\n{}\n".format(time.asctime()) + "modified to:\n" + data_in_line)
                            f.write(data_in_line)
        elif question in ('n', 'N', 'no', 'not'):
            print("no changed nothing")
        else:
            print("type \'y\' or \'n\'")

# view row of the file
def view_file(path_file):
    with open(path_file, "r") as f:
        print(f.read())

# count items
def count_items(path_file):
    lt = [k for k in open(path_file)]
    # print(lt)
    c = len(lt)-2
    return c

# add field to register
def global_regis(*args):
    dl = []
    for k in args:
        call = input(k)
        dl.append(call)
    return dl
