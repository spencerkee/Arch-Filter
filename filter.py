#!/usr/bin/env python2.7
import time
import os

hostsLocation = '/etc/hosts'
inputLocation = '/home/archie/Arch-Filter/inputsites'

def removeDuplicates(l):#takes in a list and returns it with no duplicates
	returnList = []
	for i in l:
		if i not in returnList:
			returnList.append(i)
	return returnList

def fileLength(fname):#takes in a file and returns the number of lines
	num_lines = sum(1 for line in open(fname))
	return num_lines

#takes in the hosts file and returns the line number at the end of the opening block
#which might look like :
# /etc/hosts: static lookup table for host names
#

#<ip-address>   <hostname.domain.org>   <hostname>
#127.0.0.1       localhost.localdomain   localhost
#::1             localhost.localdomain   localhost

def firstBlockLineNumber(filename):
	existingLines = open(hostsLocation).read()
	if '0.0.0.0' in existingLines:
		with open(filename) as f:
			for i, l in enumerate(f):
				if '0.0.0.0' in l:
					return i
	else:
		return fileLength(hostsLocation)

#reads in hosts file, saves the beginning block, sorts both groups of websites, and removes duplicate websites
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

	hosts = [x.replace('#', '') for x in hosts if x != '\n']#remove commented out websites
	sites_begining_with_www = []
	sites_not_beginning_with_www = []
	for i in hosts:
		if 'www' in i:
			sites_begining_with_www.append(i)
		else:
			sites_not_beginning_with_www.append(i)

	#sort and remove duplicates in both groups of websites
	sites_begining_with_www.sort()
	sites_begining_with_www = removeDuplicates(sites_begining_with_www)
	sites_not_beginning_with_www.sort()
	sites_not_beginning_with_www = removeDuplicates(sites_not_beginning_with_www)

	open(hostsLocation, 'w').close()#empty the hosts file
	with open(hostsLocation, 'w') as f:
		for i in beginningLines:
			f.write(i)
		for i in sites_begining_with_www:
			f.write(i)
		for i in sites_not_beginning_with_www:
			f.write(i)

#
def extract_urls_then_write():
	if os.stat(inputLocation).st_size != 0:#if input file is not empty
		with open(inputLocation) as f:#read in the websites
			websites = []
			for line in f:
				websites.append(line)
		websites = [x.strip('\n') for x in websites if x != '\n'] #strip new line characters
		existingWebsites = open(hostsLocation).read()
		duplicateUrls = []
		with open(hostsLocation, "a") as myfile:#write the 'www' and not 'www' versions to hosts
			for url in websites:
				if '0.0.0.0 ' + url not in existingWebsites:
					myfile.write('\n0.0.0.0 ' + url + '\n')
					myfile.write('\n0.0.0.0 www.' + url + '\n')
				else:
					duplicateUrls.append(url)
		open(inputLocation, 'w').close()#empty the input file
		with open(inputLocation, "a") as myfile:#write the duplicates (already exist in hosts) to the input file
			for url in duplicateUrls:
				myfile.write('\n' + url)
	sortHosts()

if __name__ == '__main__':
	while True:
		extract_urls_then_write()
		time.sleep(60)