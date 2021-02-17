from ClassMarkdownBuilder import MarkdownBuilder
import datetime
import selenium_crawler
from utils import *

__author__ = "Anders Rubach Ese"
__version__ = "1.1.0"
__email__ = "anders.rubach.ese@hotmail.com"
# TODO: Implement opening n windows where all scroll at once using n available CPU threads. Or ALL windows at once if possible
# TODO: Add custom tag in existing but unfinished challenges in path and dont count them

chrome_driver = selenium_crawler.ChromeDriver()
builder = MarkdownBuilder()
builder.add_img(img_url='https://user-images.githubusercontent.com/1194257/65596422-1cef2080-df97-11e9-9abb-a225204d1805.png', name='HackerRank Logo')
builder.add_heading('HackerRank')
builder.append_line('My HackerRank solutions [@hackerrank.com/Anders_Ese](https://www.hackerrank.com/Anders_Ese).')
subject_dict = {
    # '<language>': ['extension'] + sub paths
    'python': ['py-'] + ([i for i in os.walk('../python')][0][1]),
    'algorithms': [''] + ([i for i in os.walk('../algorithms')][0][1]),
    'sql': [''] + ([i for i in os.walk('../sql')][0][1]),
}
extensions_exclude = ['png', 'jpg']

num_of_challenges_crawled = 0
num_of_challenges_done = 0

for key in subject_dict:
    elements = []
    for sub_path in subject_dict.get(key)[1:]:
        n_in_path = count_files_in_dir(f'../{key}/{sub_path}', extensions_exclude)
        url = f'https://www.hackerrank.com/domains/{key}?'
        query = url_query_builder({'filters[subdomains][]': subject_dict.get(key)[0] + sub_path.replace(' ', '-')})
        n_on_website = chrome_driver.count_str_occ_in_src(url + query, 'js-track-click challenge-list-item', seconds_to_scroll=5)
        print(f' -> \'{key}/{sub_path}\': Found {n_in_path} in path and {n_on_website} on website')
        elements.append(builder.get_solution_badge(
            label=sub_path, n_in_path=n_in_path, n_on_website=n_on_website, url_pointer=f'/{key}/{sub_path}'))
        num_of_challenges_crawled += n_on_website
        num_of_challenges_done += n_in_path

    builder.add_drop_down(title=key.title(), str_list=elements)

builder.add_break_line()
builder.add_break_line()
builder.append_line(f'README.me built @{datetime.date.today()} from `/readme_builder/builder.py`')
builder.add_break_line()
builder.append_line(f'In total {num_of_challenges_done} challenges found locally and {num_of_challenges_crawled} found available crawling HackerRank site')
builder.write_content_to_file(path='../', file_name='README.md')
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
