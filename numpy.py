# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 19:34:16 2020

@author: NEERATI GANESH
"""


"""import numpy"""
import numpy as np

""""creating 1D a array"""
a=np.array([1,2,3,4,5,6,7,8,9])

print(a)


"""numpy version"""
print(np.__version__)


"""creating 2D array"""
aa=np.array([[1,2,3,4],[5,6,7,8]])


print(aa)

print(aa[0][1])


"""creating 3D"""
aaa=np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])

print(aaa[1][1][3])

"""printing dimensions"""

print(a.ndim)
print(aa.ndim)
print(aaa.ndim)


"""negtive indexing"""
print(aaa[-2][-1][-3])
    

"""array sicing need to check again"""

"""1d"""
print(a[2:3])

print(a[2:5:2])
"""2d"""
print(aa[0:2,2:])

"""3d"""


print(aaa[1:3,1:3,1:3])
"""numpy datatypes"""
b=np.array([1,2,3,4,5])
print(b.dtype)


"""creating array with specifide datatype"""
bb=np.array([1,2,3,4,5],dtype='S')
print(bb.dtype)

"""conveting existing datatype with other"""

b1=bb.astype('i')
print(b1.dtype)


"""float to int"""

b2=np.array([1.1,2.2,3.3])
print(b2.dtype)

b22=b2.astype(int)
print(b22.dtype)
print(b22)
""""shape of array"""
print(a.shape)
a.reshape(3,3)
print(a)



aa.reshape(4,2)

aaa.shape

aaa.reshape(4,2,2)
"""flattening array"""
aaa.reshape(-1)

"""array copy and view"""

a1=aa.copy()
print(a1)


a1[1:]=100
print(a1)
print(aa)


a2=aa.view()
print(a2)

a2[0:2,2:]=100
print(a2)
print(aa)

""""iterating arrays"""

for x in aa:
    for y in x:
        print(y)
for x in a:
    print(x)

"""iterating 3d"""

for a in aaa:
    for b in a:
        for c in b:
            print(c)
            
            
"""simple way iterate arrays"""

for x in np.nditer(aaa):
    print(x)
    
"""joining arrays"""

a111=np.array([1,5,3])
a222=np.array([2,5,6])

arr=np.concatenate((a111,a222))
print(arr)

"""for 2D arrays"""

arr1=np.array([[1,5,7],[9,8,7]])
arr2=np.array([[5,9,7],[3,5,9]])

arr3=np.concatenate((arr1,arr2),axis=1)
print(arr3)


""""searching in array"""

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)
"""filter arrays"""

aaaaaa=np.array([5,8,7,8,7,8,7,8,7,8,8,7])
aaa=aaaaaa>7
print(aaa)
a1=aaaaaa[aaa]
 


