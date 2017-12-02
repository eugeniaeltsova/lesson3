def wordscounter(file):
	with open (file, "r", encoding = "utf-8") as f:
		counter = 0
		lst = []
		for line in f:
			lst = line.split(" ")
			counter += len(lst)

	print (counter)


wordscounter("referat.txt")		


