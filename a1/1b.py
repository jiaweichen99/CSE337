def factorial_recur (n, ax): 
	if (n > 1): 
		return factorial_recur(n-1, ax * n) 
	else:
		return ax

print(factorial_recur(5, 1)) 	# 120
print(factorial_recur(6, 1)) 	# 720
print(factorial_recur(7, 1)) 	# 5040
#print(factorial_recur(1000,1)) # crashes 


def factorial_non_recur (n): 
	fact = 1
	for x in range (1,n+1):		# range (1,n+1) because range default includes 0 and stops before n
		fact = fact * x 
	return fact

print(factorial_non_recur(5)) 	# 120
print(factorial_non_recur(6)) 	# 720
print(factorial_non_recur(7)) 	# 5040
#print(factorial_non_recur(1000))  # DOES NOT CRASH, very large number

