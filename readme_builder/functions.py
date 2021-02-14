import os
import urllib.parse

"""
Some functions for my readme builder
"""


def is_n_in_range(n, min, max):
    return min <= n <= max


def get_color_by_percentage(part, whole):
    percentage = 100 * float(part) / float(whole)
    if is_n_in_range(percentage, 0, 30):
        return 'FF0000'
    elif is_n_in_range(percentage, 30, 90):
        return 'FFFF00'
    elif is_n_in_range(percentage, 90, 100):
        return '00FF00'


def url_query_builder(query_dictionary):
    """
    :param query_dictionary: Dictionary with queries -> {paramName1: propertyValue1, paramName2: propertyValue2}
    """
    str_out = ''
    for key in query_dictionary:
        str_out += f'&{key}={urllib.parse.quote_plus(query_dictionary.get(key))}'
    return str_out[1:]


def get_badge(label, message, color_hex='0000FF'):
    return 'https://img.shields.io/static/v1?' + url_query_builder(
        {'label': label, 'message': message, 'color': color_hex})


def count_files_in_dir(path_to_folder):
    count = 0
    for element in os.listdir(path_to_folder):
        if not os.path.isfile(element):
            count += 1
    return count
