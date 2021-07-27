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



