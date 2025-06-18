#Taking the transpose of a matrix using numpy    
import numpy as np
order=input("Enter the order of the matrix.\n")
r,c=map(int,order.lower().split('x'))
a=[]
for i in range(r):
    row=[]
    for j in range(c):
        temp=int(input("Enter the element.\n"))
        row.append(temp)
    a.append(row)
a=np.array(a)    
print(a.T)        
