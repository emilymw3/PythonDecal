import numpy as np

#1 Hey Twin
arr = np.array([[1, 1, 1], [1, 2, 3], [2, 2, 2]])
def findEqual(sample):
    answer = []
    for row in sample:
        if np.all(row == row[0]):
            answer.append(row)
    return answer
print(findEqual(arr))


#2 Checkers- create 8x8 array with checkboard pattern of 0s/1s by slicing/striding
def checkerboard():
    arr = np.zeros((8, 8))
    arr[::2, ::2] = 1
    arr[1::2, 1::2] = 1
    return arr
print(checkerboard())


#3 I need some space
myarr = np.array(['python', 'is', 'cool!'])
def spaceBetween(arr):
    spacedout = []
    for i in arr:
        wspace = ' '.join(i)
        spacedout.append(wspace)
        return spacedout
print(spaceBetween(myarr))


#4 Everything is in order
np.random.seed(12345)
a = np.random.randint(1,50, (4,5))
print(a)
print(np.argsort(a))
