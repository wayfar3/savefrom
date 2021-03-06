import random

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BrowserFactory:
    @staticmethod
    def create_browser(user_agent=None):
        opts = Options()
        # opts.add_argument('--disable-infobars')
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        if user_agent:
            opts.add_argument('user-agent={}'.format(user_agent))
        br = webdriver.Chrome(chrome_options=opts, executable_path='./chromedriver.exe')
        return br

    @staticmethod
    def fake_useragent():
        useragents = [
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2',
            'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6',
            'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1']
        return random.choice(useragents)
