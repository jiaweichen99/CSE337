# helper function
# checks for number of /, hence indicating depth
def calc_depth(str):
	# count = str.split("/")
	count = len(str.split("/"))
	return count


filename = input ("Please enter filename: ")
f = open(filename)

fileStr = f.read()
# split into different sections
splitFileStr = fileStr.split("\n\n") 

returnDct = {}

for i in splitFileStr: 
	# split so you can read line by line
	tempList = i.split("\n")
	depth = calc_depth(tempList[0])
	count = len(tempList[2:])

	# if value defined in dictionary, add on to existing count 
	# else create a new dictionary entry
	if depth in returnDct: 
		returnDct[depth] = returnDct[depth] + count
	else: 
		returnDct[depth] = count

# print out our finalized list
print(returnDct)

f.close()