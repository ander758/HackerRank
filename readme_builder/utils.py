import os
import urllib.parse

"""
Some functions for my readme builder
"""


def url_query_builder(query_dictionary):
    """
    :param query_dictionary: Dictionary with queries -> {paramName1: propertyValue1, paramName2: propertyValue2}
    """
    str_out = ''
    for key in query_dictionary:
        str_out += f'&{key}={urllib.parse.quote_plus(query_dictionary.get(key))}'
    return str_out[1:]


def count_files_in_dir(path_to_folder, extension_exclude_arr=None):
    count = 0
    for element in os.listdir(path_to_folder):
        if not os.path.isfile(element):
            if extension_exclude_arr is None:
                count += 1
            else:
                if not element.endswith(tuple(extension_exclude_arr)):
                    count += 1
    return count
