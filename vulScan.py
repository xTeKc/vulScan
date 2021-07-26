import vScanConf

#input target webpage url
target_url = 'http://duckduckgo.com'
vuln_scanner = vScanConf.ScanV(target_url)
vuln_scanner.crawl(target_url)



