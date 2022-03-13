import re
import os


def only_letter_and_nums(arg):
    return re.sub("[^A-Za-z0-9]", '-', arg)


def get_page_name(url):
    temp_str = url
    temp_str = re.sub("(http://|https://)", '', temp_str)
    temp_str = only_letter_and_nums(temp_str)
    return temp_str


def get_path(path):
    return_path = ''
    if path == '':
        return_path = os.getcwd()
    else:
        return_path = path
    return return_path


def get_resource_dir_name(url):
    return get_page_name(url) + '_files'


def get_res_full_path(path):
    dir, extension = os.path.splitext(path)
    return only_letter_and_nums(dir) + extension

