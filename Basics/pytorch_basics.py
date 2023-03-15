# -*- coding: utf-8 -*-
"""PyTorch_Basics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gSj9Xr5bO2lke-HmseTsdskLK9_gjWVG
"""

import torch
import numpy as np

# Creating an empty tensor

x = torch.empty(1) #Scalar value without initializing
print(x)

# 1D vector with three elements 

x = torch.empty(3) 
print(x)

# 2D matrix 

x = torch.empty(2,3)
print(x)

# 3D 

x = torch.empty(2,2,3)
print(x)

# Creating a tensor with random values 

x = torch.rand(2,2)
print(x)

# Tensor with zeros / ones

x = torch.zeros(2,2)
print(x)

# With datatype 

x = torch.ones(2,2, dtype=torch.int)
print(x.dtype)

# Size 

print(x.size())

"""***Some basic Operations with tensors***"""

# Element wise addition 

x = torch.rand(2,2)
y = torch.rand(2,2)

print(x)
print(y)

z = x+y
z = torch.add(x,y) # Same as before
print(z)

"""**In pytorch trailing underscore will do an in-place operation so this will modify the variable that it is applied on**"""

# In place addition 

y.add_(x)
print(y) # It will modify our y and add all of the elements of x to our y

"""**Slicing Operations**"""

x = torch.rand(5,3)

print(x)

# All rows but only one column

print(x[:,0])

"""***Reshaping an tensor***"""

x = torch.rand(4,4)
print(x)

y = x.view(16) 
print(y)

print(y.size())

"""***Numpy to torch***"""

a = torch.ones(5)
print(a)

b = a.numpy()
print(type(b))

# Torch to numpy

a = np.ones(5)
print(a)

b = torch.from_numpy(a)
print(b)

a+=1
print(a)
print(b) # Tensor is on GPU
