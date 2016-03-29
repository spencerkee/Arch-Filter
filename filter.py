#!/usr/bin/env python2.7
	
with open('inputsites') as f:
	websites = []
	for line in f:
		websites.append(line)
websites = [x.strip('\n') for x in websites] 

print websites
existingWebsites = open('testhosts').read()

with open("testhosts", "a") as myfile:
	for url in websites:
		if url not in existingWebsites:
			myfile.write('\n0.0.0.0 ' + url)
			myfile.write('\n0.0.0.0 www.' + url)

open('inputsites', 'w').close()