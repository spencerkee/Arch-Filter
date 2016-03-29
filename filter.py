#!/usr/bin/env python2.7
import time
def extract_urls_then_write():
	with open('inputsites') as f:
		websites = []
		for line in f:
			websites.append(line)
	websites = [x.strip('\n') for x in websites] 
	existingWebsites = open('testhosts').read()
	with open("testhosts", "a") as myfile:
		for url in websites:
			if '0.0.0.0 ' + url not in existingWebsites:
				myfile.write('\n0.0.0.0 ' + url)
				myfile.write('\n0.0.0.0 www.' + url)
	open('inputsites', 'w').close()
if __name__ == '__main__':
	while True:
		extract_urls_then_write()
		time.sleep(60)