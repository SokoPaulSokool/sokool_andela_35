from reception.reception import get_ordinary_list, get_vip_list
"""Checks if user is registered or not

Keyword arguments:
name -- name of the person to be checked from registration list
the_user -- stores the person's object once name is found in list
registration_list -- stores combined list of both ordinary and vip lists
Return: returns person's data once found or none once not found
"""


def registration_checker(name):
    vip_list = get_vip_list()
    ordinary_list = get_ordinary_list()

    vip_list.extend(ordinary_list)
    registration_list = vip_list

    the_user = None

    for user in registration_list:
        if user['name'].lower().find(name.lower()) is not -1:
            the_user = user
            return the_user
        else:
            the_user = None
    return the_user


print(registration_checker('paul'))
