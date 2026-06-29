#29th-06-2026
#MORNING SESSION
#DATA SCIENCE
#numpy - general purpose array processing package. 
#very fundamental package for scientific computing in python
# import numpy as np
# print(np.__version__)


#numpy arrays
#A numpy array is a collection of elements of the sama data type stored in a multidimensional structure
#Arrays provide an efficient way of storing and performing operations on numeric data
#Elements are accessed using square brackets[]
#Arrays are commonly created from python lists.


#create a numpy Array
#Arrays are created using np.array() function

#0ne dimensional array from a list
# import numpy as np
# array1 = np.array([100,300,340])
#print(array1)

#two dimensional array from list
#array2 = np.array([[200,12,25],[12,36,78]])
#print(array2)


#one dimesional array from a tuple

# array3 = np.array((23,45,67,89))
# print(array3)

#how to access an element in an array
# import numpy as np
# array1 = np.array([100,300,340])

# array2 = np.array([[200,12,25],[12,36,78]])
# for array in array2:
#     print(array2[1])
# for array in array1:
#     print(array2[0])


#Array operations
import numpy as np
w = np.array([[12,34,56,78],[2,4,5,6]])

p = np.array([[4,5,6,7],[3,2,5,67]])

# print('Adding 2 to every element: \n', w + 2)
# print('Subtracting 1 to every element: \n', p - 1)
# print('Array sun: \n', w + p)

#sum of all array elements in w
# print('sum of all array elements: ', w.sum())
# print('sum of all array elements: ', p.sum())


#Data types in Numpy.
#Every Numpy array has a data type

import numpy as np

# z = np.array([7,10])
# print(z.dtype)

# m = np.array([2.1,3.4,5.6])
# print(m.dtype)
# print(type(m))

# p = np.array([2.1,3,5.6])
# print(p.dtype)                                #combining an int and a float you get a float


#Numpy functions

#np.array() function converts a python list, tuples or sequence into an array
import numpy as np
# m = np.array([5,3,2,])
# print(m)

#np.zeros() - creates an array filled with zeros

# zero_array = np.zeros((3,4))            # 3 represents the No of zeros rows and 4 represents the no of zeros columns
# print(zero_array)

#random array
# random_array = np.random.rand(3,4)
# print(random_array)

#mathematical and statistical functions

# f = np.array([3,4,5])
# total = np.sum(f)
# print(total)

#EVENING SESSION
#Introduction to machine learning
