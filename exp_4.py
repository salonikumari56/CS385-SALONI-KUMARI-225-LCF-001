# Python program to print list 
a = [1, 2, 3, 4, 5]
# printing the list using loop 
for x in range(len(a)):
 print(a[x]) 
print("\n") 
# using the sep parameter in print() 
# printing the list using * operator separated by comma  print("using the sep parameter")
print(*a) 
# printing the list using * and sep operator print("printing lists separated by commas")
print(*a, sep = ", ")  
print("printing lists in new line") 
print(*a, sep = "\n") 
print("\n") 
# convert a list to a string for display print("convert a list to astring for display") 
a =["Geeks", "for", "Geeks"] 
# print the list using join function() 
print(' '.join(a)) 
# print the list by converting a list
# integers to string  
a = [1, 2, 3, 4, 5] 
print(str(a)[1:-1]) 
print("\n") 
# using map() function
print("using map() function")
a = [1, 2, 3, 4, 5] 
print(' '.join(map(str, a))) 
print("in new line") 
print('\n'.join(map(str, a)))
print("\n")
 # using list comprehension
print("use list comprehension")
a = [1, 2, 3, 4, 5] 
[print(i, end=' ') for i in a]
print("\nIn new line") 
[print(i) for i in a] 
print("\n") 
# using indexing and slicing print('using indexing and slicing') 
list = [1, 2, 3, 4, 5, 6] 
print(list[:])  #method 1
print(list[0:])     #method 2
print(list[0:len(list)])#method3 
