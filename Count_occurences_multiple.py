counter = 0
ls = []
# a list of keywords
gs = ["covid19","corona","pandemeic","coronawarriors","india","china"]
replace = ", . - ' ; : / ™ [ ] { } ( ) * - + & ! @ # $ % ^ _ = ` ~"
i = 0
max1 = 11
with open("C:/Users/LENOVO/Desktop/Internship/To_download_links.txt",'r') as t:
	x = t.read()
	for link in x.split():
		if i < max1: 
			i += 1
			link = link.split("/")[-1]
			print(link)
			try:
				with open("C:/Users/LENOVO/Desktop/Internship/Newpaper_Cleaned/"+link+'.txt','rb') as f:
					for line in f:
						line = line.lower()
						for word in line.split():
							# print(word)
							try:
								word = word.decode('utf-8')
								for x in replace.split():
									if x in word:
										# print('g')
										word = word.replace(x,"")
								# print(word)
								# for multiple words or hot keywords
								for c in gs:
									if c == word.lower():
										counter +=1
							except:
								pass
				print(counter)
				ls.append(counter)
				counter = 0
			except:
				pass

print(ls)
