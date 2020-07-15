counter = 0
ls = []
rs = []
lines = []
guess = " india "
# a list of keywords
gs = [" covid19 "," corona "," pandemeic "," coronawarriors ",
	" incubation period ", " community spread ", " n95 ", " quarantine " ," isolation ",
	" epidemic "," flattenig the curve "," comorbidity "," social distancing "," hydroxychloroquine ",
	" aarogya setu app "," lockdown "," lockdown extension"," virus "," infection "," airborn "," cough "," fever ", " positive "]
replace = ", ‚ . - ' ; : / ™ [ ] { } ( ) * - + & ! @ # $ % ^ _ = ` ‘ “ ~"
i = 0
# change the value of this variable with the number of files that have been parsed
max1 = 43
number_pdf = 0
with open("C:/Users/LENOVO/Desktop/Internship/To_download_links.txt",'r') as t:
	x = t.read()
	for link in x.split():
		if i < max1: 
			i += 1
			link = link.split("/")[-1]
			print(link)
			try:
				# with open("C:/Users/LENOVO/Desktop/Internship/Newpaper_Cleaned/"+link+'.txt','rb') as f:
				# we have made a new cleaned file using the Text_cleaner program
				with open("C:/Users/LENOVO/Desktop/Internship/Better_cleaned/"+link+'.txt','rb') as f:
					size = 0
					rs.append(number_pdf)
					number_pdf +=1
					for line in f:
						line = line.lower()
						line = line.decode('utf-8')
						# print(line)
						line = line.split(".")
						# print(line)
						for word in line:
							# print(word)
							size +=1
							# print(word)
							if len(word.split()) > 2:
								try:
									# print(word.strip())
									# word = word.decode('utf-8')
									for x in replace.split():
										if x in word:
											word = word.replace(x,"")
											
									# this is for the single word
									# outer loop for loop for x in guess:
									# if guess in word.lower():
									# 	# print(word)
									# 	counter+=1
									# for multiple words
									for c in gs:
										if c in word.lower().strip():
											# print(word)
											counter +=1
								except:
									pass
				print(size)
				print(counter)
				print("Percentage = ",counter/size * 100)
				print()
				ls.append(counter)
				lines.append(size)
				counter = 0
			except:
				pass

# for i in range(max1):
# 	print(ls[i]/lines[i]*100)
print(ls)
print(lines)
ls.reverse()
print(ls,rs)
# this is the graph plotting section of the code
from pandas import DataFrame
import matplotlib.pyplot as plt

Data ={ 'Day_number':rs,'Occurences':ls}

df = DataFrame(Data,columns=['Day_number','Occurences'])
df.plot(x ='Day_number', y='Occurences', kind = 'line')
plt.show()
