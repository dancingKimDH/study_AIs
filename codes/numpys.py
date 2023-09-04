py_list = [[1, 2],
           [3, 4],
           [5, 6]] # List

import numpy as np
np_array = np.array([[7, 8],
                      [9, 10],
                      [11, 12]]) # 행렬 = Array

# 병합 concatenate
np_array02 = np.array(py_list)

pass


# type(np_array)
# <class 'numpy.ndarray'>
# type(np_array)
# <class 'numpy.ndarray'>
# np.mean(np_array, axis = 1)
# array([ 7.5,  9.5, 11.5])

# 열 기준
# np.concatenate((np_array, np_array02), axis = 0)
# array([[ 7,  8],
#        [ 9, 10],
#        [11, 12],
#        [ 1,  2],
#        [ 3,  4],
#        [ 5,  6]])

# 행 기준
# np.concatenate((np_array, np_array02), axis = 1)
# array([[ 7,  8,  1,  2],
#        [ 9, 10,  3,  4],
#        [11, 12,  5,  6]])