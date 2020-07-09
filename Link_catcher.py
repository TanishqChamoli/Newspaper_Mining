from bs4 import BeautifulSoup 
import requests
import os

# In this we are supposed to redo this after sometime as the link chnages a lot.

if __name__ == "__main__":
    link_counter = 0
    # main url
    url = 'https://dailyepaper.in/the-hindu-pdf-newspaper-free-download/'
    re = requests.get(url).text
    soup = BeautifulSoup(re,'lxml')
    # list which we need for the storage of the link we have found
    l = []
    for link in soup.find_all('p'):
    	try:
    		link = link.a['href']
    		link_counter +=1
            # condtion observed by us
    		if link not in l and "hash" in link:
    			l.append(link)
    	except:
    		pass
    count = 0
    # now saving or updating the links we have found from the site
    with open("To_download_links.txt",'w') as f:
        for link in l:
            try:
                # as we have to go onle more level to find the exact pdf file so in the below given code we are just doing the same stuff
                re = requests.get(link).text
                soup = BeautifulSoup(re,'lxml')
                r = soup.find('iframe')
                r = r['src']
                ans =r.split('?')[0]
                print(ans)
                count +=1
                print("Saving--> {}".format(count))
                f.write(ans)
                f.write("\n")
            except:
                print('Passed--<')
                pass

