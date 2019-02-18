lst = [1, 2, 3]
arr = [lst[:] for i in range (3)]
arr[1][1] = 7 
print (arr)