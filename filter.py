#!/usr/bin/env python2.7
import time
import os

hostsLocation = '/etc/hosts'
inputLocation = '/home/archie/Arch-Filter/inputsites'

def fileLength(fname):
	num_lines = sum(1 for line in open(fname))
	return num_lines

def firstBlockLineNumber(filename):
	existingLines = open(hostsLocation).read()
	if '0.0.0.0' in existingLines:
		with open(filename) as f:
			for i, l in enumerate(f):
				if '0.0.0.0' in l:
					return i
	else:
		return fileLength(hostsLocation)

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
					myfile.write('\n0.0.0.0 ' + url + '\n')
					myfile.write('\n0.0.0.0 www.' + url + '\n')
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
		time.sleep(60)