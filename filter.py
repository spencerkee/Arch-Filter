#!/usr/bin/env python2.7
import time
import os
print 'started'
def extract_urls_then_write():
	if os.stat("/home/archie/Arch-Filter/inputsites").st_size != 0:
		with open('/home/archie/Arch-Filter/inputsites') as f:
			websites = []
			for line in f:
				websites.append(line)
		websites = [x.strip('\n') for x in websites if x != '\n'] 
		existingWebsites = open('/etc/hosts').read()
		duplicateUrls = []
		with open("/etc/hosts", "a") as myfile:
			for url in websites:
				if '0.0.0.0 ' + url not in existingWebsites:
					myfile.write('\n0.0.0.0 ' + url)
					myfile.write('\n0.0.0.0 www.' + url)
				else:
					duplicateUrls.append(url)
		open('/home/archie/Arch-Filter/inputsites', 'w').close()
		with open("/home/archie/Arch-Filter/inputsites", "a") as myfile:
			for url in duplicateUrls:
				myfile.write('\n' + url)
if __name__ == '__main__':
	while True:
		extract_urls_then_write()
		time.sleep(60)