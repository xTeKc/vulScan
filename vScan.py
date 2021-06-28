import requests
import re
import urlparse

class ScanV:
    def __init__(self, url):
        self.target_url = url
        self.target_links = []
    
    def extract_links_from(self, url):
        response = requests.get(url)
        return re.findAll('(?:href=")(.*?)"', response.content)

    def crawl(self, url):
        href_links = self.extract_links_from(self, url)
        for link in href_links:
            link = urlparse.urljoin(url, link)

            if '#' in link:
                link = link.split('#')[0]

            if self.target_url in link and link not in self.target_links:
                self.target_links.append(link)
                print(link)
                self.crawl(link)

