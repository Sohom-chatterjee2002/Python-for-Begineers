# -*- coding: utf-8 -*-
"""


@author: Sohom Chatterjee_CSE1_T25
"""



# Problem 1

import numpy
from numpy import random
x = random.randint(100,size=(3,3))
print(x)
# OUTPUT
#[[69 48 88]
# [23 73 21]
# [96 16 94]]

# Problem 2
import numpy
from numpy import random
x = random.randint(100,size=(3,3))
print(x)
a=numpy.diag(x)
print(a)
sum1=sum(a)
print(sum1)
y=x[::-1]
b=numpy.diag(y)
print(b)
sum2=sum(b)
print(sum2)

# OUTPUT
# [[95  8 91] 
#  [ 9 64 83] 
#  [37 75 75]]
# [95 64 75]
# 234       
# [37 64 91]
# 192    

#Problem 3
import numpy
from numpy import random
x = random.randint(100,size=(3,3))
print(x)
y = random.randint(100,size=(3,3))
print(y)
z=numpy.add(x,y)
print(z)

# OUTPUT
# [[11  5 17] 
#  [90 76 12] 
#  [85 43 29]]
# [[56 33 20]    
#  [ 7 48 32]    
#  [42 79 71]]   
# [[ 67  38  37] 
#  [ 97 124  44] 
#  [127 122 100]]

#Problem 4
import numpy as np
from numpy import random
x = random.randint(100,size=(3,3))
print(x)
y = random.randint(100,size=(3,3))
print(y)
z=np.multiply(x,y)
print(z)

# OUTPUT
# [[99 23  6] 
#  [13 25 12] 
#  [82  9 25]]
# [[82 13 78]       
#  [96 21 18]       
#  [81 69 79]]      
# [[8118  299  468] 
#  [1248  525  216] 
#  [6642  621 1975]]

#Problem 5
import numpy as np
from numpy import random
x = random.randint(100,size=(3,3))
print(x)
y = random.randint(100,size=(3,3))
print(y)
z=np.dot(x,y)
print(z)

#OUTPUT
# [[52 99 61]
#  [25 51 85]
#  [91 56 96]]
# [[ 8 42 78]
#  [51 23 67]
#  [80 52 23]]
# [[10345  7633 12092]
#  [ 9601  6643  7322]
#  [11264 10102 13058]]

#Problem 6
import numpy
from numpy import random
x = random.randint(100,size=(3,3))
print(x)
y=numpy.linalg.matrix_rank(x)
print("RANK =",y)

#OUTPUT
# [[17 68 26] 
#  [51 87 47] 
#  [20 69 13]]
# RANK = 3

#Problem 7
import numpy as np
from numpy import random
x = random.randint(100,size=(3,3))
print(x)
trace_of_matrix=x.trace()
print("Trace of your matrix is: ",trace_of_matrix)
#OUTPUT
# Your matrix:
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]
# Trace of your matrix is:  [[12]]

#Problem 8
import numpy
from numpy import random
x = random.randint(100,size=(3,3))
print(x)
y=numpy.linalg.det(x)
print("determinent =",y)

#output
# [[58 48 34] 
#  [ 2 13 14] 
#  [30 21 48]]
# determinent = 22860.0

#Problem 9
import numpy as np
# Suppose we take the equations as Ax+By=C
c=int(input("Enter the number of variables = "))
r=int(input("Enter the number of equations = "))
# Enter the variable coefficients
mat = [[int(input()) for x in range (c)] for y in range(r)]
A=np.array(mat)
print(A)
b=[int(input()) for z in range(r)]
B=np.array(b)
print(B)
X=np.linalg.inv(A).dot(B)
print(X)

# OUTPUT
# Enter the number of variables = 2
# Enter the number of equations = 2
# 4 
# 3
# -5
# 9
# [[ 4  3]
#  [-5  9]]
# 20
# 26
# [20 26]
# [2. 4.]
# # 


#Problem 10
import numpy as np
from scipy import stats
l=np.random.randint(100,size=(10))
print(l)
mean=np.mean(l)
median=np.median(l)
mode=stats.mode(l)
print(mean,median,mode)

# OUTPUT
# [47 55 24 38 17 63 51 95 52  1]
# 44.3 49.0 ModeResult(mode=array([1]), count=array([1]))

#Problem 11
import numpy as np
matrix=np.random.randint(100,size=(3,3))
result1=np.max(matrix,axis=1)  #Find row wise maximum number
result2=np.min(matrix,axis=0)  #Find Column wise minimum number
print(result1)
print(result2)

# OUTPUT
# [[99 35  5] 
#  [ 5 76 90] 
#  [99 70  8]]
# [99 90 99]
# [ 5 35  5]

#Problem 12
import numpy as np
a=np.array([9,-4,7])
b=np.array([8,0,5])
print("First input array:")
print(a)
print("Second input array:")
print(b)
result=np.subtract(a,b)
print("Output array:")
print(result)

# OUTPUT
# First input array:
# [ 9 -4  7]
# Second input array:
# [8 0 5]
# Output array:      
# [ 1 -4  2]

