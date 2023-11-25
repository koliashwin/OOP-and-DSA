# An Array is a collection of items of same data type stored at contiguous memory locations

# declaration
arr = [0,0,0]
print("initial : ", arr)
arr[0] = 10
arr[1] = 20

print("updated : ",arr) # check results first 2 elements are updated
print("element at perticular index : ",arr[1]) # accessing element at index 1

for i in arr:   #array traversal or searching element in array
    print(i)

# 2D array
arr_2D = []     # declare single array

# try adding multiple arrays inside it
arr_2D.append(arr)
arr_2D.append([253,658,987,321])

print("whole array :",arr_2D) 
print("access specific array : ", arr_2D[1])
print("access specific element : ", arr_2D[1][2])