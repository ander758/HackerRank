import os
import urllib.parse
import selenium_utils
from functions import get_badge
__author__ = "Anders Rubach Ese"
__version__ = "1.0.0"
__email__ = "anders.rubach.ese@hotmail.com"

chrome_driver = selenium_utils.ChromeDriver()

print(get_badge('Er Anders kul?', 'Ja!', 'FF0000'))

print(chrome_driver.count_string_occurrence_in_html_source(
    url='https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-introduction',
    string='js-track-click challenge-list-item'))

f = open("Output.txt", "w")
f.write('# HackerRank\n\n')
f.write('My HackerRank solutions [@hackerrank.com/Anders_Ese](https://www.hackerrank.com/Anders_Ese)\n')

subject_dict = {
    # '<language>': ['extension'] + sub paths
    'python': ['py'] + ([i for i in os.walk('../python')][0][1])
}

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

def percentage(part, whole):
  return 100 * float(part)/float(whole)

for key in subject_dict:
    f.write(f' - {key}\n')
    for sub_path in subject_dict.get(key)[1:]:
        label = sub_path
        count_my_sols = 1  # TODO: count files in subpath
        num_of_sols_on_HackerRank = 7  # TODO: Count files on HackerRank
        message = f'{count_my_sols}/{num_of_sols_on_HackerRank}'
        color = get_color_by_percentage(count_my_sols, num_of_sols_on_HackerRank)
        f.write(f'	 - [![{sub_path}]({get_badge(label, message, color)})](/{key}/{sub_path})\n')

f.close()
chrome_driver.close()

"""
Hackerrank query
prefix = https://www.hackerrank.com/domains/<programming language>?
        E.g.
            https://www.hackerrank.com/domains/python?
query  = &filters[subdomains][]=<programming language extension>-<subject>
        E.g.
            &filters[subdomains][]=py-introduction
            &filters[subdomains][]=py-basic-data-types
"""
# https://www.hackerrank.com/domains/python?filters[subdomains][]=py-introduction



