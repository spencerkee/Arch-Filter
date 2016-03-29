#!/usr/bin/env python2.7
import time
import os
print 'started'

def firstBlockLineNumber(filename):
	with open(filename) as f:
		for i, l in enumerate(f):
			if '0.0.0.0' in l:
				return i

def sortHosts():
	beginingSeperator = firstBlockLineNumber('/etc/hosts')
	hosts = []
	beginningLines = []
	with open('/etc/hosts') as f:
		websites = []
		index = 0
		for line in f:
			if index < beginingSeperator:
				beginningLines.append(line)
			else:
				hosts.append(line)
			index += 1
	hosts = [x.replace('#', '') for x in hosts if x != '\n']
	hosts.sort()
	open('/etc/hosts', 'w').close()
	with open('etc/hosts', 'w') as f:
		for i in beginningLines:
			f.write(i)
		for i in hosts:
			f.write(i)


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
		sortHosts()
		open('/home/archie/Arch-Filter/inputsites', 'w').close()
		with open("/home/archie/Arch-Filter/inputsites", "a") as myfile:
			for url in duplicateUrls:
				myfile.write('\n' + url)


if __name__ == '__main__':
	while True:
		extract_urls_then_write()
		time.sleep(60)