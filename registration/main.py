# Checks if user is registered or mot


def registration_checker(name):
    vip_list = [{'name': 'paul', 'category': "VIP"},
                {'name': 'peter', 'category': "VIP"}]
    ordinary_list = [{'name': 'paul', 'category': "ORDINARY"},
                     {'name': 'peter', 'category': "ORDINARY"}]
    # combines the lists to one list
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
