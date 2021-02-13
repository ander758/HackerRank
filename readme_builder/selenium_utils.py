from selenium import webdriver
from selenium.webdriver.chrome.options import Options

__author__ = "Anders Rubach Ese"
__version__ = "1.0.0"
__email__ = "anders.rubach.ese@hotmail.com"

"""
Selenium/Chromium driver for my readme builder
"""


class ChromeDriver:
    # Helper class for extracting from HackerRank
    def __init__(self, executable_path='chromedriver_88.0.4324.27.exe', window_size='800,600', headless=False):
        """
        :param executable_path: Path to chromedriver.exe. Get current version of your Chromium browser ->https://chromedriver.chromium.org/downloads
        :param headless: True if no window to be launched, may wrong results
        """
        chrome_options = Options()
        if headless:
            chrome_options.add_argument('--headless')
        chrome_options.add_argument(f'--window-size={window_size}')
        self.webdriver_chrome = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)

    def count_string_occurrence_in_html_source(self, url, string, get_source_after_js_onload=True):
        """
        Returns occurrence of a string in entire HTML source of an url
        :param get_source_after_js_onload: True returns html source after JavaScript is loaded.
                                            May give bad source if set to False"""
        self.webdriver_chrome.get(url)
        if get_source_after_js_onload:
            html_source = self.webdriver_chrome.execute_script('return document.documentElement.innerHTML;')
        else:
            html_source = self.webdriver_chrome.page_source()
        return html_source.count(string)

    def close(self):
        """
        Closes driver
        """
        self.webdriver_chrome.close()
