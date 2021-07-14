##########################################################
#
# ___________ | By cy3r-g0d                         
# Last Modified: 22/03/2016
#
##########################################################

import sys
import urllib.request, urllib.error

## the domain to scan
domain = input("Domain: ")
## read the dir text file
file = open("dir.txt")
dir = file.read()
## Split new lines
directory = dir.splitlines()
## creating an empty list
admin = []
## finding the directory that exist
for a in directory:
    url = f"https://{domain}/{a}"
    try:
        conn = urllib.request.urlopen(url)
     ## If page doesnot exist
    except urllib.error.HTTPError as e:
        ## do nothing && pass
        pass 
    ## If connection reffused by the site    
    except urllib.error.URLError as e:
        print('[!] Connection reffused to', f"{domain}")
        pass
    else:
        # export found profile page urls to a text file
        text_file = open(f"result/{domain}"".txt", "a")
        text_file.write(url)
        text_file.write("\n")
        text_file.close()  
        print("[+] Admin login found in", url)
        sys.exit(1)