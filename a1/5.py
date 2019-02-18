# i. Division by zero 
try: 
	print (4 // 0)
except ZeroDivisionError: 
	print ("No dividing by zero!")
else: 
	print ("Everything seems fine!")

# ii. Using an improper key with a dictionary
dct = {}
dct["name"] = "Jiawei"
# print (dct["name"])
try: 
	print (dct["age"])
except KeyError: 
	print ("Invalid key!")
else: 
	print ("Everything seems fine!")

# iii. Indexing a list with an illegal value
lst = [1,2,3]
# print (lst[2])
try: 
	print (lst[3])
except IndexError: 
	print ("Invalid index!")
else: 
	print ("Everything seems fine!")
