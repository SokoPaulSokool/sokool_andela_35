# Checks if user is registered or mot


def registration_checker(name):
    vip_list = [{'name': 'paul', 'category': "VIP"},
                {'name': 'peter', 'category': "VIP"}]
    ordinary_list = [{'name': 'paul', 'category': "ORDINARY"},
                     {'name': 'peter', 'category': "ORDINARY"}]
    # combines the lists to one list
    vip_list.extend(ordinary_list)
    registration_list = vip_list