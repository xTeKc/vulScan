import vScan

#input target webpage url
target_url = 'webpage-url'
vuln_scanner = vScan.ScanV(target_url)
vuln_scanner.crawl(target_url)



