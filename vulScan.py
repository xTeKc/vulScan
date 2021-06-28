import requests
from BeautifulSoup import BeautifulSoup

def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

target_url = 'enter-webpage-url'
response = request(target_url)

parsed_html = BeautifulSoup(response.content)
forms_list = parsed_html.findAll('form-on-page')
print(forms_list)