import requests
from BeautifulSoup import BeautifulSoup

def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

#get html from webpage
target_url = 'enter-webpage-url'
response = request(target_url)
#print(response.content)

#parse diff elements of html on webpage
parsed_html = BeautifulSoup(response.content)
#find specific element in html
forms_list = parsed_html.findAll('form-on-page')

#get nested elements inside specified element ^
for form in forms_list:
    action = form.get('action-nested-elem')
    print(action)
    method = form.get('method-nested-elem')
    print(method)

    inputs_list = form.findAll('input-nested-elem')
    for input in inputs_list:
        input_name = input.get('name')
        print(input_name)