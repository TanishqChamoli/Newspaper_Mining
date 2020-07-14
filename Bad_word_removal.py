stop_words = "i me my myself we our ours ourselves you your yours yourself yourselves he him his himself she her hers herself it its itself they them their theirs themselves what which who whom this that these those am is are was were be been being have has had having do does did doing a an the and but if or because as until while of at by for with about against between into through during before after above below to from up down in out on off over under again further then once here there whenwhere why how all any both eachfew more most other some such no nor not only own same so than too very s t can will just don should now "

ls = []
# a list of keywords
gs = ["covid19","corona","pandemeic","coronawarriors",
       "incubation period", "community spread", "n95", "quarantine " ,"isolation",
       "epidemic","flattenig the curve","comorbidity","social distancing","hydroxychloroquine",
       "aarogya setu app","lockdown","lockdown extensio","virus","infection","airborn","cough","fever","masks","mask"]
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
					counter = 0
					for line in f:
						line = line.lower().decode('utf-8')
						# print(line)
						line  = line.split()
						# print(line)
						for word in line:
							try:
								for x in replace.split():
									if x in word:
										word = word.replace(x,"")

								# bad word removal in this step
								if word in stop_words:
									# print(word)
									pass
								else:
									total_words +=1

								# for multiple words or hot keywords
								for c in gs:
									c = c.strip()
									if c == word.lower():
										# print(c)
										counter +=1
										# print(counter)
							except:
								pass
				f.close()
				print(counter)
				print(total_words)
				ls.append(counter)
				counter = 0
			except:
				pass

print(ls)
