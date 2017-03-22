# -----------
# User Instructions:
# 
# Modify the function search so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# Make sure that the initial cell in the grid 
# you return has the value 0.
# ----------
from utils import Queue
        
grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    Nr=len(grid)
    Nc=len(grid[0])
    expand=[[-1 for j in range(Nc)] for i in range(Nr)]
    count=0

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

    visited=[]
    frontier=Queue()
    frontier.push([init,0])

    while not frontier.isEmpty():
        loc, rlen=frontier.pop()
        if not loc in visited:
            visited.append(loc)
            expand[loc[0]][loc[1]]=count
            count += 1

            if loc==goal:
                return expand

            for nextloc, move_name in childNode(grid, loc, delta, delta_name):
                if not nextloc in visited:
                    frontier.push([nextloc, rlen+cost])
    return 'fail'

exp_maze=search(grid,init,goal,cost)
if exp_maze=='fail':
    print(exp_maze)
else:
    print('Expanded sequence:')
    for row in exp_maze:
        print(row)
print('Grid:')
for row in grid:
    print(row)
