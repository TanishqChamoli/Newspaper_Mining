counter = 0
ls = []
# a list of keywords
gs = [" covid19 "," corona "," pandemeic "," coronawarriors ",
	" incubation period ", " community spread ", " n95 ", " quarantine " ," isolation ",
	" epidemic "," flattenig the curve "," comorbidity "," social distancing "," hydroxychloroquine ",
	" aarogya setu app "," lockdown "," lockdown extension"," virus "," infection "," airborn "," cough "," fever "]
replace = ", . - ' ; : / ™ [ ] { } ( ) * - + & ! @ # $ % ^ _ = ` ~"
i = 0
# change the value of this variable with the number of files that have been parsed
max1 = 11
with open("C:/Users/LENOVO/Desktop/Internship/To_download_links.txt",'r') as t:
	x = t.read()
	for link in x.split():
		if i < max1: 
			i += 1
			link = link.split("/")[-1]
			print(link)
			try:
				# with open("C:/Users/LENOVO/Desktop/Internship/Newpaper_Cleaned/"+link+'.txt','rb') as f:
				with open("C:/Users/LENOVO/Desktop/Internship/Better_cleaned/"+link+'.txt','rb') as f:
					total_words = 0
					for line in f:
						line = line.lower()
						for word in line.split():
							# print(word)
							total_words +=1
							try:
								word = word.decode('utf-8')
								for x in replace.split():
									if x in word:
										# print('g')
										word = word.replace(x,"")
								# for multiple words or hot keywords
								for c in gs:
									c = c.strip()
									# print(c)
									if c == word.lower():
										# print(c)
										counter +=1
							except:
								pass
				print(counter)
				print(total_words)
				ls.append(counter)
				counter = 0
			except:
				pass

print(ls)
