# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------
from utils import Stack, Queue, PriorityQueue

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
# goal = [len(grid)-1, len(grid[0])-1]
goal = [0, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def print_maze(grid):
    for e in grid:
        print(e)

def compute_policy(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    Nr=len(grid)
    Nc=len(grid[0])
    inf=99
    value=[[inf for j in range(Nc)] for i in range(Nr)]
    policy=[[' ' for j in range(Nc)] for i in range(Nr)]


    def childNode(grid, loc, delta, delta_name):
        child=[]
        for i in range(len(delta)):
            move=delta[i]
            newloc=[loc[0]+move[0], loc[1]+move[1]]
            if loc[0]+move[0]>=0 and loc[0]+move[0]<Nr \
            and loc[1]+move[1]>=0 and loc[1]+move[1]<Nc \
            and grid[newloc[0]][newloc[1]] ==0:
                child.append([newloc,delta_name[i]])
        return child



    change = True
    while change:
        change=False
        for i in range(Nr):
            for j in range(Nc):
                if i==goal[0] and j==goal[1]:
                    if value[i][j]>0:
                        value[i][j]=0
                        policy[i][j]='*'
                        change=True
                elif grid[i][j]==0:
                    for newloc, move_name in childNode(grid, [i,j], delta, delta_name):
                        if value[newloc[0]][newloc[1]]+cost<value[i][j]:
                            value[i][j]=value[newloc[0]][newloc[1]]+cost
                            policy[i][j]=move_name
                            change=True

    
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    return policy 

result=compute_policy(grid, goal, cost)
print('Policy:')
print_maze(result)
print('Grid:')
print_maze(grid)
