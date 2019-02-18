def pal_test_iterative (string): 
	# stopping case, either we went through entire str or one letter left
	while (len(string) > 1): 
		# last letter == first letter?
		if (string[0] != string[-1]): 
			return False 
		string = string[1:-1] 
	return True 

# test cases taken from lecture slides 

s1 = "racecar"     # True
s2 = "speedboat"   # False
s3 = "deified"     # True
s4 = "abracadabra" # False
s5 = "sentences"   # False
s6 = "civic"       # True

pl = [s1, s2, s3, s4, s5, s6]

for p in pl:
    print(pal_test_iterative(p))