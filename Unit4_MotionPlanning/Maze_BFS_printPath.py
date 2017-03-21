# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

from util import Queue

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
# grid = [[0, 1],
#         [0, 0]]
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
    # insert code here
    # ----------------------------------------
    Nr=len(grid)
    Nc=len(grid[0])
    expand=[[-1 for j in range(Nc)] for i in range(Nr)]
    policy=[[' ' for j in range(Nc)] for i in range(Nr)]
    path=[[' ' for j in range(Nc)] for i in range(Nr)]
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
    frontier.push([init,' ',0])

    while not frontier.isEmpty():
        loc, mov, rlen=frontier.pop()
        if not loc in visited:
            visited.append(loc)
            policy[loc[0]][loc[1]]=mov

            if loc==goal:
                path[goal[0]][goal[1]]='*'
                while loc!=init:
                    x,y=loc
                    if policy[x][y]=='v':
                        loc=[x-1,y]
                        path[loc[0]][loc[1]]='v'
                    elif policy[x][y]=='^':
                        loc=[x+1,y]
                        path[loc[0]][loc[1]]='^'
                    elif policy[x][y]=='>':
                        loc=[x,y-1]
                        path[loc[0]][loc[1]]='>'
                    elif policy[x][y]=='<':
                        loc=[x,y+1]
                        path[loc[0]][loc[1]]='<'

                return path

            for nextloc, move_name in childNode(grid, loc, delta, delta_name):
                if not nextloc in visited:
                    frontier.push([nextloc,move_name, rlen+cost])
    return 'fail'

    # return result

exp_maze=search(grid, init, goal, cost)
for row in exp_maze:
    print row
for row in grid:
    print row

