import vScanConf

#input target webpage url
target_url = 'webpage-url'
vuln_scanner = vScanConf.ScanV(target_url)
vuln_scanner.crawl(target_url)



