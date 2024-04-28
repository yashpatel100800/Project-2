def contains_zero_square(matrix):
    n = len(matrix)
    
    def is_zero_square(row, col, size):
        if row + size > n or col + size > n:
            return False, []
        
        corners = []
        
        if matrix[row][col] == 0:
            corners.append((row, col))
        else:
            return False, []
        if matrix[row][col + size - 1] == 0:
            corners.append((row, col + size - 1))
        else:
            return False, []
        if matrix[row + size - 1][col] == 0:
            corners.append((row + size - 1, col))
        else:
            return False, []
        if matrix[row + size - 1][col + size - 1] == 0:
            corners.append((row + size - 1, col + size - 1))
        else:
            return False, []
        
        for i in range(1, size - 1):
            if matrix[row][col + i] != 0 or matrix[row + size - 1][col + i] != 0:
                return False, []
            if matrix[row + i][col] != 0 or matrix[row + i][col + size - 1] != 0:
                return False, []
        
        return True, corners
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                for k in range(2, n - max(i, j) + 1):
                    is_square, corners = is_zero_square(i, j, k)
                    if is_square:
                        return True, corners
    
    return False, []

# Sample input matrix
matrix = [
    [1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1]
]

# Call the function and print the result
result, corners = contains_zero_square(matrix)
print("Contains square with zero border:", result)
print("Indexes of corner zeros:", corners)
s = set()
t = set()
for i in corners:
    s.add(i[0])
    t.add(i[1])
print(s,t)

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if(((i in s)  and (min(t)<=j<=max(t))) or ((j in t) and (min(s)<=i<=max(s)) )):
            print("0,",end="")
        else:
            print(" ,",end="")
    print("\n",end="")