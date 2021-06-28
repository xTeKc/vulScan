import requests
import re

class vScan:
    def __init__(self, url):
        self.target_url = url
    
    def extract_links_from(self, url):
        response = requests.get(url)
        return re.findAll('(?:href=")(.*?)"', response.content)