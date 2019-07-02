import random
def collect_coins2(matrix, r, c, sum):
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        is_bottom = r == num_rows - 1
        is_rightmost = c == num_cols - 1

        if is_bottom and is_rightmost:
            sum = matrix[r][c]
        elif is_bottom:
            sum = matrix[r][c] + collect_coins2(matrix, r, c + 1, sum)
        elif is_rightmost:
            sum = matrix[r][c] + collect_coins2(matrix, r + 1, c, sum)
        else:
            sum = matrix[r][c] + max(collect_coins2(matrix, r + 1, c, sum),
                                             collect_coins2(matrix, r, c + 1, sum))

        return sum

def collect_coins(matrix, r=0, c=0, cache=None):
    if cache is None:
        cache = {}

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    is_bottom = r == num_rows - 1
    is_rightmost = c == num_cols - 1

    if (r, c) not in cache:

        if is_bottom and is_rightmost:
            cache[r, c] = matrix[r][c]
        elif is_bottom:
            cache[r, c] = matrix[r][c] + collect_coins(matrix, r, c + 1, cache)
        elif is_rightmost:
            cache[r, c] = matrix[r][c] + collect_coins(matrix, r + 1, c, cache)
        else:
            cache[r, c] = matrix[r][c] + max(collect_coins(matrix, r + 1, c, cache),
                                             collect_coins(matrix, r, c + 1, cache))

    return cache[r, c]

mat = [[0]*3]*3 
for i in range(3):
    for j in range(3):
        mat[i][j]=random.randint(0,j+18)

print(mat)
print(collect_coins(mat,0,0,None))
print(collect_coins2(mat,0,0,0))