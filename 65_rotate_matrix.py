#Rotate matrix
# Using brute force method
M = 3
N = 3
matrix = [[12, 23, 34],
         [45, 56, 67],
         [78, 89, 91]]
def rotateMatrix(self,N,M,K,Mat):
    #code here
    temp = [0] * M
    K %= M
    for i in range(0, N):
        for t in range(0, K):
            temp[t] = Mat[i][t]
        for j in range(K, M):
            Mat[i][j - K] = Mat[i][j]
        for j in range(M - K, M):
            Mat[i][j] = temp[j - M + K]
    return Mat

def displayMatrix():
    global M, N, matrix
    for i in range(0, N):
        for j in range(0, M):
            print("{}" .format(matrix[i][j]), end = " ")
        print()

#Driver code
k = 2
rotateMatrix(k)
displayMatrix()