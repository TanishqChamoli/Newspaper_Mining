import wget
import os.path

# we are just using the basic command of linux for the exploitation of downloading the files

if __name__ == "__main__":
	counter = 0
	# to be changed as per the user
	download = 46
	# files from which we have to read the links and download the data
	with open("./To_download_links.txt",'r') as f:
	    x = f.read()
	    for link in x.split():
	    	if counter < download:
		    	# print(link)
		    	counter += 1
		    	check = link.split("/")[-1]
		    	# print(check)
		    	if os.path.isfile("./Newspaper_PDF/"+check):
		    		print("exists")
		    	else:
		    		print("Downloading the file " + check)
			    	filename = wget.download(link,"./Newspaper_PDF/"+check)
			    	print(filename)

	    # the data is around 3 gigs so be carefull vbefore downloading the files
	    # just did download the first 10 links and found the values..