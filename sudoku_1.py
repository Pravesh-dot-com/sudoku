# -*- coding: utf-8 -*-

board = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9],
]

def print_board(brd):
    
    for i in range(len(brd)):
        if i%3 == 0 and i != 0:
            print('------------------------')
        
        for j in range(len(brd[i])):
            if j%3 == 0 and j != 0 :
                print(' | ',end ="")
            if j == 8:
                print(brd[i][j])
            else:
                print(str(brd[i][j])+ " ", end="")
                
                
 
def solve(brd):
    #print(brd)
    # base solution
    find = find_empty(brd)
    if not find:
        return True
    else:
        row, col = find
        
        
    for i in range(1,10):
        if valid(brd, i, (row,col)):
            brd[row][col] = i
        
            if solve(brd): # move on to the next empty space and try to solve
                return True     
            
            # if the above doesnt hold true i.e. the num doesnt fit, then mark the num as empty and try the next num
            brd[row][col] = 0
        
        
    return False # if nothing worked            



def find_empty(brd):
    
    for i in range(len(brd)):
        for j in range(len(brd[i])):
            if brd[i][j] == 0:
                return (i, j) #row, column
        
    return None
        


def valid(brd, num, pos):
    
    # check row
    for i in range(len(brd)):
        if brd[pos[0]][i] == num and pos[1] != i:
            return False
        
    # Check column
    for i in range(len(brd)):
        if brd[i][pos[1]] == num and pos[0] != i:
            return False
        
    # Check box
    box_x =  pos[1]//3
    box_y =  pos[0]//3
    
    for i in range(box_y*3, box_y*3 +3):
        for j in range(box_x*3, box_x*3 + 3):
            if brd[i][j] == num and (i, j) !=  pos:
                return False
    
    #if valid
    return True
        


print_board(board)
print('INput above----Solution below------')
solve(board)
print_board(board)