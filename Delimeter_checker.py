counter = 0
ls = []
lines = []
guess = " india "
# a list of keywords
gs = [" covid19 "," corona "," pandemeic "," coronawarriors "," india "," china "," modi "]
replace = ", ‚ . - ' ; : / ™ [ ] { } ( ) * - + & ! @ # $ % ^ _ = ` ‘ “ ~"
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
					size = 0
					for line in f:
						line = line.lower()
						line = line.decode('utf-8')
						# print(line)
						line = line.split(".")
						for word in line:
							size +=1
							# print(word)
							try:
								# word = word.decode('utf-8')
								for x in replace.split():
									if x in word:
										# print('g')
										word = word.replace(x,"")
								# print(word)
								# this is for the single word
								# outer loop for loop for x in guess:
								# if guess in word.lower():
								# 	# print(word)
								# 	counter+=1
								# for multiple words
								for c in gs:
									if c in word.lower():
										# print(word)
										counter +=1
							except:
								pass
				print(size)
				print(counter)
				ls.append(counter)
				lines.append(size)
				counter = 0
			except:
				pass
print(ls)
print(lines)
