import PyPDF2
import os.path

loop = 0
dowloaded = 30
with open("To_download_links.txt","r") as p:
	# this will read the file names by exracting the last parts of the file and we will be able to get the files easily
	x = p.read()
	for link in x.split():
		# the main spltiing adn the conformation of checking
		if loop < dowloaded:
			loop +=1
			link = link.split("/")[-1]
			file_name = link
			try:
				if os.path.isfile("./Newpaper_Cleaned/"+file_name+'.txt'):
					print("The file has already been parsed")
				else:
					# the pdf reader is being used in this
					pdfFileObj = open("./Newspaper_PDF/" + file_name, 'rb')
					# the object is assigned to the reader
					pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
					# print(pageObj.extractText())
					# making a file with the same name of the file
					with open("./Newpaper_Cleaned/" + file_name + '.txt','wb') as f:
						# the pages are being traversed
						for page_num in range(pdfReader.getNumPages()):
							pageObj = pdfReader.getPage(page_num)
							try:
								# trying to read from the file and get the text from the specifed page in the pdf
								print("Reading from the file " + str(loop) + " The page we are at is " +str(page_num))
								txt = pageObj.extractText()
							except:
								pass
							print("Writing into a file " + str(loop)+ " The page we are at is " + str(page_num))
							# writing the data into the file whicah has the same name as the pdf
							f.write(txt.encode("utf-8"))
							print("We have written into the file.")

					# closing the files as we dont want to hold onto the resources
					f.close()
					pdfFileObj.close()
			except:
				print("File not found!!")

