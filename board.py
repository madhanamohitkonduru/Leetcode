import collections

board =  [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

#My soultion
result = 0

for i in range(0, 9, 1):
    dic = {'1': 0,   '2': 0,   '3': 0,   '4': 0,   '5': 0,   '6': 0,   '7': 0, '8': 0, '9':0, '.': 0}
    for j in range(0, 9, 1):
        dic[board[i][j]] = dic[board[i][j]] + 1
        if dic[board[i][j]] == 2 and board[i][j] != '.':
            result = 1
            print(i,j)
    del dic

for j in range(0, 9, 1):
    dic = {'1': 0,   '2': 0,   '3': 0,   '4': 0,   '5': 0,   '6': 0,   '7': 0, '8': 0, '9':0, '.': 0}
    for i in range(0, 9, 1):
        dic[board[i][j]] = dic[board[i][j]] + 1
        if dic[board[i][j]] == 2 and board[i][j] != '.':
            result = 1
            print(i, j)
    del dic

row_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
col_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

for row in row_list:
    for col in col_list:
        dic = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '.': 0}
        for i in row:
            for j in col:
                dic[board[i][j]] = dic[board[i][j]] + 1
                if dic[board[i][j]] == 2 and board[i][j] != '.':
                    result = 1
                    print(i, j)
        del dic

#Actual optimal solution
cols = collections.defaultdict(set)
rows = collections.defaultdict(set)
squares = collections.defaultdict(set)  # key = (r /3, c /3)

for r in range(9):
    for c in range(9):
        if board[r][c] == ".":
            continue
        if (
                board[r][c] in rows[r]
                or board[r][c] in cols[c]
                or board[r][c] in squares[(r // 3, c // 3)]
        ):
            result = 1
            print(r, c)
        cols[c].add(board[r][c])
        rows[r].add(board[r][c])
        squares[(r // 3, c // 3)].add(board[r][c])
        print('rows:', rows)
        print('cols:', cols)
        print('square', squares)
        print('__________________________________________')
print(rows)
print(cols)
print(squares)