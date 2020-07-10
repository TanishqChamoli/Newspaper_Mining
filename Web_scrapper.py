from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
	counter = 0
	link = 'https://currentaffairs.gktoday.in/page/'
	for i in range(10):
		source = requests.get(link+str(i)).text
		soup = BeautifulSoup(source,'lxml')
		main = soup.find_all('div',class_ = 'post-content')
		article_size = 0
		guess = ["covid19","corona","pandemeic","coronawarriors","india"]
		for p in main:
			x = p.text
			to_change= ", . - ' ; : / ™ [ ] { } ( ) * - + & ! @ # $ % ^ _ = ` ~ ’ ‘"
			x = x.replace("\n","")
			x = x.rstrip()
			x = x.split(".")
			# print(x)
			for sentence in x:
				# print(w)
				for word in guess:
					# print(word)
					for p in to_change.split():
						if p in sentence:
							sentence = sentence.replace(p,"")
					if word in sentence.lower():
						# print(word)
						# print(sentence)
						counter +=1
						continue
			article_size +=len(x)
		print("The page numebr is ->", i+1)
		print("Length of the article is--> ",article_size)
		print("Number of sentence which contain the words are----> ",counter)
		counter = 0

