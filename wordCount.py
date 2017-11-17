############This code shows number of occurance of each word in array ####
############And also number of distinct words ########################
count = int(input("number of words: "))
inputArray = []
out=[]
check=[]

for i in range(count):
	userIn = str(input("Enter a word: "))
	inputArray.append(userIn)

for i in inputArray:
	repetation = inputArray.count(i)
	##print (i + str(repetation))	
	if i in check:
		##print(i + " is already counted")
		pass
	else:
		if repetation == 1:
			##print("add " + i)
			out.append(str(1))	
		else:
			##print("add " + i)
			out.append(str(repetation))
			check.append(i)
			
			

print("distinct words: "+ str(len(out)))
for i in out:
	print(i,end= " ")
