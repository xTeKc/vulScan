import vScanConf
import requests

#input target webpage url
target_url = input(f"Enter WebPage URL: ")
data_dict = {"username": "admin", "password": "password", "Login": "submit"}

vuln_scanner = vScanConf.ScanV(target_url)
response = vuln_scanner.session.post(target_url, data = data_dict)

vuln_scanner.crawl()



