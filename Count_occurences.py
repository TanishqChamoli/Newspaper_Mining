counter = 0
ls = []
rs = []
guess = "pakistan"
replace = ", . - ' ; : / ™ [ ] { } ( ) * - + & ! @ # $ % ^ _ = ` ~"
i = 0
# change the value of this variable with the number of files that have been parsed
max1 = 43
number_pdf = 0
with open("./To_download_links.txt",'r') as t:
	x = t.read()
	for link in x.split():
		if i < max1: 
			i += 1
			link = link.split("/")[-1]
			print(link)
			try:
				with open("./Better_cleaned/"+link+'.txt','rb') as f:
					number_pdf +=1
					rs.append(number_pdf)
					for line in f:
						line = line.lower()
						total_words = 0
						for word in line.split():
							# print(word)
							try:
								word = word.decode('utf-8')
								total_words +=1
								for x in replace.split():
									if x in word:
										# print('g')
										word = word.replace(x,"")
								# print(word)
								# outer loop for loop for x in guess:
								if word.lower() == guess:
									# print(word)
									counter+=1
							except:
								pass
				print(counter)
				print(total_words)
				print("Percentage = ",counter/total_words * 100)
				print()
				ls.append(counter)
				counter = 0
			except:
				pass

# print(ls)
ls.reverse()
print(len(ls),len(rs))
# this is the graph plotting section of the code
from pandas import DataFrame
import matplotlib.pyplot as plt

Data ={ 'Day_number':rs,'Occurences':ls}

df = DataFrame(Data,columns=['Day_number','Occurences'])
df.plot(x ='Day_number', y='Occurences', kind = 'line')
plt.show()


# convert file to excel thne to csv for R