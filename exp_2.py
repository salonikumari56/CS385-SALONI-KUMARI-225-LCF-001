num = int(input("enter a number")) 
for i in range(num): 
 for j in range(1,num-(i+1)): 
   print("* ",end=" ")     
print() 