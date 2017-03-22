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
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def print_maze(grid):
    for e in grid:
        print (e)

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    Nr=len(grid)
    Nc=len(grid[0])
    inf=99
    value=[[inf for j in range(Nc)] for i in range(Nr)]

    locs=[[i,j] for i in range(Nr) for j in range(Nc) if grid[i][j]==0]

    Nloc=len(locs)

    visited=[]

    value[goal[0]][goal[1]]=0

    def minlocV(locs):
        minV=inf
        idx=0
        idy=0
        for loc in locs:
            if not loc in visited:
                if minV>value[loc[0]][loc[1]]:
                    minV=value[loc[0]][loc[1]]
                    idx,idy=loc
        if minV==inf:
            return []
        else:
            return [idx, idy]


    def childNode(grid, loc, delta):
        child=[]
        for move in delta:
            newloc=[loc[0]+move[0], loc[1]+move[1]]
            if loc[0]+move[0]>=0 and loc[0]+move[0]<Nr \
            and loc[1]+move[1]>=0 and loc[1]+move[1]<Nc \
            and grid[newloc[0]][newloc[1]] ==0:
                child.append(newloc)
        return child


    # while not isequal(explored, locs):


    while len(visited)!=Nloc:
        # print 'Here'
        currentloc=minlocV(locs)
        if len(currentloc)==0:
            break
        visited.append(currentloc)

        for newloc in childNode(grid, currentloc, delta):
            if not newloc in visited and value[newloc[0]][newloc[1]]>cost+value[currentloc[0]][currentloc[1]]:
                value[newloc[0]][newloc[1]]=cost+value[currentloc[0]][currentloc[1]]
    
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    return value 

result=compute_value(grid, goal, cost)
print('Value:')
print_maze(result)
print('Grid:')
print_maze(grid)
