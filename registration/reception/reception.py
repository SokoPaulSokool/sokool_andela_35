"""Reads the vip list text file and returns a list of registered users

"""


def get_vip_list():
    vip_file_data = open('../data/vip_list.txt', 'r')
    vip_list = []
    for name in vip_file_data.readlines():
        if name is not None:
            vip_list.append({"name": name.rstrip('\n'), "category": "VIP"})
    vip_file_data.close()
    return vip_list


"""Reads the ordinary list text file and returns a list of registered users

"""


def get_ordinary_list():
    pass
