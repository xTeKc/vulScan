import vScanConf
import requests  #refactor remove?

#input target webpage url
target_url = input(f"Enter WebPage URL: ")
#links_to_ignore = [""]  #enter links to ignore for session

data_dict = {"username": "admin", "password": "password", "Login": "submit"}  #login session

vuln_scanner = vScanConf.ScanV(target_url)  #, links_to_ignore  #add links_to_ignore as arg
response = vuln_scanner.session.post(target_url, data = data_dict)  #response to session
#vuln_scanner.session.post(input(f"Enter WebPage URL: "), data = data_dict)  #refactored version

vuln_scanner.crawl()
vuln_scanner.run_scanner()  #run vuln scanner

#forms = vuln_scanner.extract_form(input(f"Enter WebPage URL: "))  #extract_form from webpage
#print(forms)  #print the forms from webpage
#response = vuln_scanner.submit_form(forms[0], "test-test", input(f"Enter WebPage URL: "))  #enter url
#print(response.content)  #print test-test into form on entered webpage

#replace with current response if needed
#response = vuln_scanner.test_xss_in_form(forms[0], input(f"Enter WebPage URL: "))  #enter url
#print(response)  #print response for xss form vulnerability testing

#replace with current response if needed
#response = vuln_scanner.test_xss_in_link(input(f"Enter WebPage URL: "))  #enter url
#print(response)  #print response for xss link vulnerability testing

