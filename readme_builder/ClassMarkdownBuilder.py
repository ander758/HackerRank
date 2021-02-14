import urllib.parse

"""
Class to build the markdown file
"""


def get_badge(label, message, color_hex='0000FF'):
    def url_query_builder(query_dictionary):
        """:param query_dictionary: Dictionary with queries -> {param:val, param2:val2}"""
        str_out = ''
        for key in query_dictionary:
            str_out += f'&{key}={urllib.parse.quote_plus(query_dictionary.get(key))}'
        return str_out[1:]

    return 'https://img.shields.io/static/v1?' + url_query_builder(
        {'label': label, 'message': message, 'color': color_hex})


def hex_color_by_pct(part, whole):
    def is_n_in_range(n, min, max):
        return min <= n <= max

    percentage = 100 * float(part) / float(whole)
    if is_n_in_range(percentage, 0, 30):
        return 'FF0000'
    elif is_n_in_range(percentage, 30, 90):
        return 'FFFF00'
    elif is_n_in_range(percentage, 90, 100):
        return '00FF00'


class MarkdownBuilder:
    def __init__(self):
        self.file_content = ''

    def write_content_to_file(self, path='./', file_name='README.md'):
        if self.file_content != '':
            f = open(path + file_name, 'w')
            f.write(self.file_content)
            f.close()
        else:
            print('No content when writing!')

    def add_img(self, img_url, name):
        self.append_line(f'![{name}]({img_url})')

    def append_line(self, str_in):
        self.file_content += str_in + '\n'

    def add_heading(self, str_in):
        self.append_line(f'# {str_in}')

    def add_drop_down(self, title, str_list):
        self.append_line(f'- {title}')
        for element in str_list:
            self.append_line(f'	 - {element}')

    def get_solution_badge(self, label, n_in_path, n_on_website, url_pointer):
        message = f'{n_in_path}/{n_on_website}'
        color_hex = hex_color_by_pct(n_on_website, n_on_website)
        return f'[![{label}]({get_badge(label, message, color_hex)})]({url_pointer})'

    def add_break_line(self):
        self.append_line('<br>')
