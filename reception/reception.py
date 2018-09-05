import os


def get_vip_list():
    """Reads the vip list text file and returns a list of registered users

    """
    fpath = os.path.join(os.getcwd(),
                         'data/vip_list.txt').replace('\\', '/')
    vip_file_data = open(fpath, 'r')
    vip_list = []
    for name in vip_file_data.readlines():
        if name is not None:
            vip_list.append({"name": name.rstrip('\n'), "category": "VIP"})
    vip_file_data.close()
    return vip_list


def get_ordinary_list():
    """Reads the ordinary list text file and returns a list of registered users

    """
    fpath = os.path.join(os.getcwd(),
                         'data/ordinary_list.txt').replace('\\', '/')
    ordinary_file_data = open(fpath, 'r')
    ordinary_list = []
    for name in ordinary_file_data.readlines():
        if name is not None:
            ordinary_list.append(
                {"name": name.rstrip('\n'), "category": "ORDINARY"})
    ordinary_file_data.close()
    return ordinary_list


def registration_checker(name):
    """Checks if user is registered or not

    Keyword arguments:
    name -- name of the person to be checked from registration list
    the_user -- stores the person's object once name is found in list
    registration_list -- stores combined list of both ordinary and vip lists
    Return: returns person's data once found or none once not found
    """
    vip_list = get_vip_list()
    ordinary_list = get_ordinary_list()

    vip_list.extend(ordinary_list)
    registration_list = vip_list

    the_user = None

    for user in registration_list:
        if user['name'].lower().find(name.lower()) is not -1:
            the_user = user
            return the_user['name']+", " + the_user['category']
        else:
            the_user = None
    return 'Not Registered'


"""Prompt for input"""

print("\n\n\nWELCOME TO EVENTS REGISTRATION\n")
print("You can check if a person is registered\n")
name = input("Please enter person's name: ")
print("\nSearching for  " + str(name) + ' ...')

print(registration_checker(name))
