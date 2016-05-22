## Arch-Filter

Python program to automate blocking of websites/urls through the hosts file.

## Motivation

I found blocking websites individually through the hosts file to be tiresome and made me less likely to do so, even if it would boost my productivity. This program is a quick way to add, format, and sort urls in the hosts file without acting on it directly. This allows you to block in batches quickly and easily. 

## Getting Started

**For total effective url blocking, change your root password to something long that you can't remember and give it to someone you trust. **

Then give root only rights to the program by running: 

```bash
sudo chown root:root /path/to/filter.py
sudo chmod 700 /path/to/filter.py
```

And use visudo to remove root acess to all but essential commands. 

## Usage

Whenever you want to restrict access to a websites, add the domain names to the inputsites file on different lines and save. Ex. If you want to block 'http://www.cnn.com/' and 'https://www.opendns.com/' then add this: 

```bash
cnn.com
opendns.com
```

After 60 seconds the urls will be removed from the input file (unless they already exist in the hosts file) and are added to etc/hosts.
