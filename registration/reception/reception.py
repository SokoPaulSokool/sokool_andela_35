import os
"""Reads the vip list text file and returns a list of registered users

"""


def get_vip_list():
    fpath = os.path.join('../data/vip_list.txt')
    vip_file_data = open(fpath, 'r')
    vip_list = []
    for name in vip_file_data.readlines():
        if name is not None:
            vip_list.append({"name": name.rstrip('\n'), "category": "VIP"})
    vip_file_data.close()
    return vip_list


print(get_vip_list())

"""Reads the ordinary list text file and returns a list of registered users

"""


def get_ordinary_list():
    ordinary_file_data = open('../data/ordinary_list.txt', 'r')
    ordinary_list = []
    for name in ordinary_file_data.readlines():
        if name is not None:
            ordinary_list.append(
                {"name": name.rstrip('\n'), "category": "ORDINARY"})
    ordinary_file_data.close()
    return ordinary_list
