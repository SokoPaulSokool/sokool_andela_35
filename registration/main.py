
"""Checks if user is registered or not

Keyword arguments:
name -- name of the person to be checked from registration list
the_user -- stores the person's object once name is found in list
registration_list -- stores combined list of both ordinary and vip lists
Return: returns person's data once found or none once not found
"""


def registration_checker(name):
    vip_list = [{'name': 'paul', 'category': "VIP"},
                {'name': 'peter', 'category': "VIP"}]
    ordinary_list = [{'name': 'paul', 'category': "ORDINARY"},
                     {'name': 'peter', 'category': "ORDINARY"}]
    
    vip_list.extend(ordinary_list)
    registration_list = vip_list

    the_user = None

    for user in registration_list:
        if user['name'] == name:
            the_user = user
            return the_user
        else:
            the_user = None
    return the_user
