import requests
from BeautifulSoup import BeautifulSoup
import urlparse

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
    #join two urls
    post_url = urlparse.urljoin(target_url, action)
    #print(post_url)

    method = form.get('method-nested-elem')
    #print(method)

    inputs_list = form.findAll('input-nested-elem')
    post_data = {}
    for input in inputs_list:
        #get input name that is nested in input
        input_name = input.get('name-nested-input')
        #print(input_name)
        input_type = input.get('type-nested-input')
        input_value = input.get('value-nested-input')
        if input_type == 'text':
            input_value = 'test'

        post_data[input_name] = input_value
    result = requests.post(post_url, data=post_data)
    print(result.content)