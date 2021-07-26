import vScanConf

#input target webpage url
target_url = 'http://crypto.com'
vuln_scanner = vScanConf.ScanV(target_url)
vuln_scanner.crawl()



