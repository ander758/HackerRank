from ClassMarkdownBuilder import MarkdownBuilder
from ClassDomain import Domain, sub_folders_in_folder
import ClassChromeDriver
import datetime

__author__ = "Anders Rubach Ese"
__version__ = "1.2.0"
__email__ = "anders.rubach.ese@hotmail.com"
# TODO: Implement opening n windows where all scroll at once using n available CPU threads. Or ALL windows at once if possible

chrome_driver = ClassChromeDriver.ChromeDriver()
markdown_builder = MarkdownBuilder()
markdown_builder.add_img(img_url='https://user-images.githubusercontent.com/1194257/65596422-1cef2080-df97-11e9-9abb-a225204d1805.png', name='HackerRank Logo')
markdown_builder.add_heading('HackerRank')
markdown_builder.append_line('My HackerRank solutions [@hackerrank.com/Anders_Ese](https://www.hackerrank.com/Anders_Ese).')

domains = []
for domain in sub_folders_in_folder(path='../', exclude=['venv', 'readme_builder', '.git', '.idea']):
    domains.append(Domain(name=domain, sub_folders=sub_folders_in_folder(path='../' + domain), root_path='../' + domain))


count_total_crawled = 0
count_total_done = 0
for domain in domains:
    drop_down_elements = []
    for subdomain in domain.subdomains:
        count_website = chrome_driver.count_str_occ_in_src(subdomain.query_url(), 'js-track-click challenge-list-item', seconds_to_scroll=1)  # increase 'seconds_to_scroll' if slow connection..
        count_done = subdomain.count_challenges_in_path()
        drop_down_elements.append(
            markdown_builder.get_solution_badge(
                label=subdomain.name,
                n_in_path=count_done,
                n_on_website=count_website,
                url_pointer=subdomain.root_path))
        count_total_crawled += count_website
        count_total_done += count_done
        print(f' ->{subdomain.root_path}: Found {count_done} in path and {count_website} on website')
    markdown_builder.add_drop_down(title=domain.name.title(), str_list=drop_down_elements)


markdown_builder.add_break_line()
markdown_builder.add_break_line()
markdown_builder.append_line(f'README.me built @{datetime.date.today()} from `/readme_builder/build.py`')
markdown_builder.add_break_line()
markdown_builder.append_line(f'In total {count_total_done} challenges found locally and {count_total_crawled} found available crawling HackerRank site')
markdown_builder.write_content_to_file(path='../', file_name='README.md')
chrome_driver.close()
