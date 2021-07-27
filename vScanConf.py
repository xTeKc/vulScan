import requests
import re
from urllib.parse import urljoin

class ScanV:
    def __init__(self, url):  #, ignore_links  #add ignore_links as arg
        self.session = requests.Session()  #add session
        self.target_url = url
        self.target_links = []
       #self.links_to_ignore = ignore_links  #access list by calling
    
    def extract_links_from(self, url):
        response = self.session.get(url)  #get session
        return re.findall('(?:href=")(.*?)"', response.text)
    
    def crawl(self, url=None):  #set default <url> value to <None>
        if url == None:
            url = self.target_url
        href_links = self.extract_links_from(url)
        for link in href_links:
            link = urljoin(url, link)

            if '#' in link:
                link = link.split('#')[0]

            if self.target_url in link and link not in self.target_links:  #and link not in self.links_to_ignore
                self.target_links.append(link)                             #add to use links_to_ignore during crawl
                print(link)
                self.crawl(link)

