import vScanConf

#input target webpage url
target_url = input('Enter WebPage URL: ')
vuln_scanner = vScanConf.ScanV(target_url)
vuln_scanner.crawl()



