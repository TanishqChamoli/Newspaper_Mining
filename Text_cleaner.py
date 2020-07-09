if __name__ == "__main__":
	with open('The_Hindu_07_Jul_2020.pdf.txt','rb') as f:
		x = f.read()
		# x[i].decode("utf-8")
		t = str(x)
		# print(type(t))
		# t = x[i].replace('\n',"")
		t = t.replace('\n','')
		t = t.encode("utf-8")
		with open("temp.txt",'wb') as s:
			s.write(t)
		# print(t)

		# not working properly