#!/usr/bin/env python2.7
import time
import os

# hostsLocation = '/etc/hosts'
# inputLocation = '/home/archie/Arch-Filter/inputsites'
hostsLocation = '/home/archie/Arch-Filter/testhosts'
inputLocation = '/home/archie/Arch-Filter/inputsites'

def firstBlockLineNumber(filename):
	with open(filename) as f:
		for i, l in enumerate(f):
			if '0.0.0.0' in l:
				return i

def sortHosts():
	beginingSeperator = firstBlockLineNumber(hostsLocation)
	hosts = []
	beginningLines = []
	with open(hostsLocation) as f:
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
	print 'beginninglines', beginningLines
	print 'hosts', hosts
	open(hostsLocation, 'w').close()
	with open(hostsLocation, 'w') as f:
		for i in beginningLines:
			f.write(i)
		for i in hosts:
			f.write(i)

def extract_urls_then_write():
	if os.stat(inputLocation).st_size != 0:
		with open(inputLocation) as f:
			websites = []
			for line in f:
				websites.append(line)
		websites = [x.strip('\n') for x in websites if x != '\n'] 
		existingWebsites = open(hostsLocation).read()
		duplicateUrls = []
		with open(hostsLocation, "a") as myfile:
			for url in websites:
				if '0.0.0.0 ' + url not in existingWebsites:
					myfile.write('\n0.0.0.0 ' + url)
					myfile.write('\n0.0.0.0 www.' + url)
				else:
					duplicateUrls.append(url)
		open(inputLocation, 'w').close()
		with open(inputLocation, "a") as myfile:
			for url in duplicateUrls:
				myfile.write('\n' + url)
	sortHosts()

if __name__ == '__main__':
	while True:
		extract_urls_then_write()
		time.sleep(20)