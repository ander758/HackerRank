import datetime
import selenium_utils
from functions import *

__author__ = "Anders Rubach Ese"
__version__ = "1.0.0"
__email__ = "anders.rubach.ese@hotmail.com"

chrome_driver = selenium_utils.ChromeDriver()

f = open("../README.md", "w")
f.write('# HackerRank\n\n')
f.write('My HackerRank solutions [@hackerrank.com/Anders_Ese](https://www.hackerrank.com/Anders_Ese)\n')

subject_dict = {
    # '<language>': ['extension'] + sub paths
    'python': ['py-'] + ([i for i in os.walk('../python')][0][1]),
    'algorithms': [''] + ([i for i in os.walk('../algorithms')][0][1])
}

for key in subject_dict:
    f.write(f' - {key.title()}\n')
    for sub_path in subject_dict.get(key)[1:]:
        label = sub_path
        count_my_sols = count_files_in_dir(f'../{key}/{sub_path}')

        url = f'https://www.hackerrank.com/domains/{key}?'
        query = url_query_builder({'filters[subdomains][]': subject_dict.get(key)[0] + sub_path.replace(' ', '-')})
        num_of_challenges_on_HackerRank = chrome_driver.count_string_occurrence_in_html_source(url + query,
                                                                                               'js-track-click challenge-list-item')
        print(url + query)
        message = f'{count_my_sols}/{num_of_challenges_on_HackerRank}'
        color = get_color_by_percentage(count_my_sols, num_of_challenges_on_HackerRank)
        print(f'q={url}{query}')
        print(f'label={label}')
        print(f'message={message}')
        print(f'color={color}')
        f.write(f'	 - [![{sub_path}]({get_badge(label, message, color)})](/{key}/{sub_path})\n')

f.write(f'\n<br /><br />README.me built @{datetime.date.today()} from `/readme_builder/builder.py`')
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
