import requests
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup

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

    def extract_form(self, url):
        response = self.session.get(url)
        parsed_html = BeautifulSoup(response.content)
        return parsed_html.findall("form")
    
    def submit_form(self, form, value, url):
        action = form.get("action")
        post_url = urljoin(url, action)
        method = form.get("method")
        
        inputs_list = form.findall("input")
        post_data = {}
        for input in inputs_list:
            input_name = input.get("name")
            input_type = input.get("type")
            input_value = input.get("value")
            if input_type == "text":
                input_value = value
                
            post_data[input_name] = input_value
        if method == "post":
            return self.session.post(post_url, data = post_data)
        return self.session.get(post_url, params = post_data)
    
    def run_scanner(self):
        for link in self.target_links:
            forms = self.extract_form(link)
            for form in forms:
                print(f"Testing form in {link}")
                
            if "=" in link:
                print(f"Testing {link}")
                