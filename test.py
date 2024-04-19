board = [['']*3 for _ in range(3)]

def win():
    #For all the rows
    if (board[0][0] == board[0][1] == board[0][2]):
        return board[0][0]
    if (board[1][0] == board[1][1] == board[1][2]):
        return board[1][0]
    if (board[2][0] == board[2][1] == board[2][2]):
        return board[2][0]
    
    #For all the columns
    if (board[0][0] == board[1][0] == board[2][0]):
        return board[0][0]
    if (board[0][1] == board[1][1] == board[2][1]):
        return board[0][1]
    if (board[0][2] == board[1][2] == board[2][2]):
        return board[0][2]

    #For the diagnols
    if (board[0][0] == board[1][1] == board[2][2]):
        return board[0][0]
    if (board[0][2] == board[1][1] == board[2][0]):
        return board[0][2]
    return ''

def boardToString():
    boardString = ''
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                boardString += '_'
            else:
                boardString += board[i][j]
    return boardString
            

unused = set()
unused.add((0,0))
unused.add((0,1))
unused.add((0,2))
unused.add((1,0))
unused.add((1,1))
unused.add((1,2))
unused.add((2,0))
unused.add((2,1))
unused.add((2,2))
result = 0
hashMap = set()
def dfs(currentPlayer):
    global result
    if len(unused) == 0:
        result += 1
        return
    check = win()
    if check == 'X' or check == 'O':
        result += 1
        return
    if boardToString() in hashMap:
        return
    for cell in unused.copy():
        unused.remove(cell)
        board[cell[0]][cell[1]] = currentPlayer
        currentPlayer = 'X' if currentPlayer == 'O' else 'X'
        dfs(currentPlayer)
        unused.add(cell)
        board[cell[0]][cell[1]] = ''
        currentPlayer = 'X' if currentPlayer == 'O' else 'X'
    hashMap.add(boardToString())
    return

for i in range(3):
    for j in range(3):
        board[i][j] = 'X'
        unused.remove((i,j))
        dfs('O')
        unused.add((i,j))

print(result)