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

from utils import PriorityQueue

# grid = [[0, 1, 0, 0, 0, 0],
#         [0, 1, 0, 0, 0, 0],
#         [0, 1, 0, 0, 0, 0],
#         [0, 1, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0]]
grid = [[0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0,]]
heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]
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

def heuristic_fun(loc, goal):
    return abs(loc[0]-goal[0])+abs(loc[1]-goal[1])

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
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
    frontier=PriorityQueue()
    gv=0+heuristic_fun(init, goal)
    frontier.push([init,0], gv)

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
                    gv=rlen+heuristic_fun(nextloc, goal)
                    frontier.push([nextloc, rlen+cost], gv)
    return 'fail'

    # return result

exp_maze=search(grid, init, goal, cost)
for row in exp_maze:
    print(row)

