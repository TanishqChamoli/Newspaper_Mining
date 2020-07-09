counter = 0
ls = []
guess = "covid19"
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
							if word.lower() == guess:
								# print(word)
								counter+=1
						except:
							pass
			print(counter)
			ls.append(counter)
			counter = 0

print(ls)
