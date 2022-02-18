import numpy as np
#matrixen als numpy array um sie zu addieren#
n= 5
def matrix():
    m1 = np.array([])
    for i in range(n):
        m2 = np.array([])
        for y in range(n):
            m2.append(i)
        return m2
        m1.append(m2)
    return m1

print(matrix())


#matrix = np.array([
 #   [x,y,y,y,y,y],
  #  [y,x,y,y,y,y],
   # [y,y,x,y,y,y],
    #[y,y,y,x,y,y],
    #[y,y,y,y,x,y],
    #[y,y,y,y,y,x]
#])

#x = 0


# matrix2 = np.array([
#     [0,1,0,0,1,1],
#     [1,0,1,0,0,0],
#     [1,0,0,1,0,0],
#     [0,1,0,0,1,1],
#     [1,0,1,0,0,0],
#     [0,1,0,0,1,0],
# ])

#matrix3 = matrix + matrix2

#n = 6
#new = [[random.radint(0,1) for i in range(6)] for i in range(6)]