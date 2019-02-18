*** TO DO: 
	- polish up all answers (2, 6- 7)
	- test on a CS machine? 
*************************** 

Jiawei Chen 
111537808 

1a) This version uses a while loop to go through the given input string. It continuously checks and chops off the first and the last letter until we either find a mismatch or go through the entire string to conclude that it's a palindrome.

1b) Using an accumulator here changes the order in which the multiplication for the result is computed. However, in the grand scheme of things, there will still be approximately the same number of recursive calls, meaning that the upper limit runtime for this version is basically the same as before. Instead of building up multiplication that will 
get evaluated at the end of all the recursion calls, you will have the product passed on from call to call.

As we can see, the loop version will hold out whereas the recursion version will crash a lot faster. This is because the recursive version holds a lot of stack memory, and repeated calls to the same function will stack up extremely fast and cause a stack overflow error. However, the loop version only needs to worry about keeping track of the updated running factorial product, which is magnitudes easier than 
an ever growing stack. 

3a) 	lst = [1,2,3]
	lst * 3 -> [1, 2, 3, 1, 2, 3, 1, 2, 3]
	[ lst ] * 3 -> [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

	The multiplication operator is used to produce multiple copies of the elements lst and put them in a new list. The only difference is that in the third expression, [ lst ] takes place first to create an extra set of brackets around [1, 2, 3], resulting in the behavior shown as above. 

3b) 	>>> lst = [1, 2, 3]
	>>> arr = [ lst ] * 3
	>>> lst[1] = 7
	>>> arr -> [[1, 7, 3], [1, 7, 3], [1, 7, 3]]

	As we can see, changes in lst are also reflected across arr, as changing lst[1] changed the corresponding three values in arr. This is because we created a shallow copy of lst (aka a direct reference) in the second line, and the multiplication operator inherently copies over those pointers. 

	If we replace line 3 with “arr[1][1] = 7”, we'll note the exact same output in arr as before. This is because since we're essentially just using three pointers to lst, changing arr[1][1] is essentially modifying lst, and modifying lst will reflect appropriately in its other references. 

3c) 	>>> lst = [1, 2, 3]
	>>> arr = [ lst[:] ]* 3
	>>> arr[1][1] = 7
	>>> arr -> [[1, 7, 3], [1, 7, 3], [1, 7, 3]]
	
	Attempting to use slicing to get around the problem will not work, as we see that the output of arr still isn't what we want. This is because even though using [ lst[:] ] produces a deep copy independent of lst, the problem with how the multiplication inherently works is still there. The multiplication operator simply duplicates pointers, so while changing lst will no longer reflect accordingly in arr, changes in arr are making changes to our three references of lst's copy (lst[:]) and will be reflected accordingly.
	
3d) The workaround to this, so that “arr[0][1]” and “arr[2][1]” are not affected is to change "arr = [ lst[:] ]* 3" to "arr = [lst[:] for i in range (3)]". The for loop combined with the slice creates deep copies, which is exactly what we're looking for. 

4a) n = 0 and r = 0

	Since n is equal to r, continue will be called, resulting the loop being called again with n being equal to 1 this time, since it loops through range(4). 

Executed Lines: if n == r: continue 
		print (n) 
		r = randrange(0,4)  

4b) n = 1 and r = 2 

	Since n is less than r, "x" will be printed and it will go back to looping.

Executed Lines: print ("x")
		print (n)
		r = randrange(0,4)  

4c) n = 2 and r = 0
	
	Since n is greater than r, the loop will break. n is not less than 2, so the last statement will not print. 

Executed Lines: if n>r: break 

4d) n = 3 and r = 3
	
	Since n is equal to r, continue will run. However, since that was the last iteration of the loop, the program moves onto the else statement and prints "Wow, you are lucky". 

Executed Lines: if n == r: continue 
		print ("Wow, you are lucky\n")

5a) i) ZeroDivisionError, you can get this error by attempting to divide by zero ( e.g. print (4 // 0) ) 

    ii) KeyError, you can get this error by trying to access a key that doesn't exist ( e.g. I create a dictionary and define dct["name"] = "Jiawei", but then try to print out dct["age"] )

    iii) IndexError, you can get this error by accessing a value greater than or equal to the length of the list ( e.g. defining lst = [1,2,3], then trying to print lst[3] ) 

6) The idea behind this program is to parse the output file into different parts and evaluate each chunk. First, we split the entire file by "\n\n", since each directory is separated by two new lines. We will then go through each one of our directories, now in a convenient string form. The first line is the directory, and we can determine the depth the by the number of folders we have to go through, or aptly represented by the number of "/" in the directory name. The number of files per directory is fairly simple to count, and we accumulate all this information in a dictionary to be returned at the end.

































