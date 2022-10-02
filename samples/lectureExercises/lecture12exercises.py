import numpy as np

##exercise 1
v = np.array([2.,2.,4.])
e0 = np.array([1.,0.,0.])
e1 = np.array([0.,1.,0.])
e2 = np.array([0.,0.,1.])
answers = []
answers.append(v@e0)
answers.append(v@e1)
answers.append(v@e2)
print(answers)

##exercise 2
a = np.array([[6,-9,1],[4,24,8]])
print(2*a)
b = np.array([[1,0],[0,1]])
print(b.dot(a))
c = np.array([[4,3],[3,2]])
d = np.array([[-2,3],[3,-4]])
print(np.dot(c,d))

##exercise 3
def swap_rows(M, a, b):
    temp= M[a].copy()
    M[a]=M[b]
    M[b]=temp
    return M

def swap_cols(M, a, b):
    temp=M[:,a].copy()
    M[:,a]=M[:,b]
    M[:,b]=temp
    return M

print(swap_rows(a, 0, 1))
print(swap_cols(a, 0, 2))

##exercise 4
l = [1,2,3,4,5,6,7,8,9,0]

def set_array(L, rows, cols):
    matrix = np.zeros((rows,cols))
    for i in range(rows):
        for j in range(cols):
            matrix[i,j]=L[i*cols+j]
    return matrix

print(set_array(l, 2, 5))

#columns first
def set_array_cols(L, rows, cols):
    matrix = np.zeros((rows,cols))
    for j in range(cols):
        for i in range(rows):
            matrix[i,j]=L[j*rows+i]
    return matrix

print(set_array_cols(l, 2, 5))

#instead of one at a time, do the entire row at once
def set_array__(L, rows, cols):
    matrix = np.zeros((rows,cols))
    temp=0
    for i in range(rows):
        matrix[i]=L[temp:temp+cols]
        temp+=cols
    return matrix

print(set_array__(l, 2, 5))

#instead of one at a time, do the entire column at once
def set__array__(L, rows, cols):
    matrix = np.zeros((rows,cols))
    temp=0
    for i in range(cols):
        matrix[:,i]=L[temp:temp+rows]
        temp+=rows
    return matrix

print(set__array__(l, 2, 5))

##exercise 5
arr = np.array([[0,1,2,3,4,5],[10,11,12,13,14,15],[20,21,22,23,24,25],[30,31,32,33,34,35],[40,41,42,43,44,45],[50,51,52,53,54,55]])
print(arr)

blue = arr[:,1]
print(blue)

pink = arr[1,2:4]
print(pink)

green = arr[2:4,4:6]
print(green)

orange = np.array([[arr[2,0], arr[2,2], arr[2,4]] , [arr[4,0], arr[4,2], arr[4,4]]])
print(orange)