## Arch-Filter

Python program to automate blocking of websites/urls through the hosts file.

## Motivation

I found blocking websites individually through the hosts file to be tiresome and made me less likely to do so, even if it would boost my productivity. This program is a quick way to add, format, and sort urls in the hosts file without acting on it directly. This allows you to block 

## Usage

For total effective url blocking, change your root password to something long that you can't remember and give it to someone you trust. Then run: 

```bash
sudo chown root:root /path/to/filter.py
sudo chmod 700 /path/to/filter.py
```

And use visudo to remove root acess to all but essential commands. 
