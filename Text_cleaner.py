import os
# This code removes the problems which were occuring before and now we have better clean and parsed data
replace = ", ‚ ' ; : / ™ [ ] { } ( ) * - + & ! @ # $ % ^ _ = ` ‘ “ ~"

if __name__ == "__main__":
	i = 0
	# change the value of this variable with the number of files that have been parsed
	max1 = 80
	with open("./To_download_links.txt",'r') as t:
		x = t.read()
		for link in x.split():
			if i < max1: 
				i += 1
				link = link.split("/")[-1]
				print(link)
				try:
					s = 0
					# print(link)
					if os.path.isfile("./Better_cleaned/"+link+'.txt'):
						print("The file has already been parsed")
						print()

					else:
						with open('./Newpaper_Cleaned/'+link+'.txt','rb') as f:
							x = f.read()
							x = x.decode("utf-8")
							t = str(x)
							for r in replace.split():
								t = t.replace(r,'')
							t = t.replace("\n"," ")
							t = t.replace("-","")
							s = t
						with open('./Better_cleaned/'+link+'.txt','wb') as f:
							f.write(s.encode("utf-8"))
						f.close()
				except:
					pass	