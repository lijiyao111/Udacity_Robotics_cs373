# Policy is not correct
# need to work backward 

from util import PriorityQueue

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
# grid = [[1, 1, 1, 0, 0, 0],
#         [1, 1, 1, 0, 1, 0],
#         [0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 0, 1, 1],
#         [1, 1, 1, 0, 1, 1]]

# init = [4, 3, 0] # given in the form [row,col,direction]
#                  # direction = 0: up
#                  #             1: left
#                  #             2: down
#                  #             3: right
                
# goal = [2, 0] # given in the form [row,col]

# cost = [2, 1, 20] # cost has 3 values, corresponding to making 
#                   # a right turn, no turn, and a left turn
grid = [[0, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [4, 5, 1]
goal = [4, 3]
cost = [2, 1, 20]
# grid = [[1, 1, 1, 0, 0, 0],
#         [1, 1, 1, 0, 1, 0],
#         [0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 0, 1, 1],
#         [1, 1, 1, 0, 1, 1]]
# init = [4, 3, 0]
# goal = [2, 0]
# cost = [2, 1, 20]

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------
def childNode(grid, loc, delta, delta_name):
    Nr=len(grid)
    Nc=len(grid[0])
    child=[]
    x,y,head=loc
    for i in range(len(action)):
        move_id=(action[i]+head)%4 ## Actual move in global coordinate

        move=delta[move_id]
        newloc=[loc[0]+move[0], loc[1]+move[1], (head+action[i])%4]
        if loc[0]+move[0]>=0 and loc[0]+move[0]<Nr \
        and loc[1]+move[1]>=0 and loc[1]+move[1]<Nc \
        and grid[newloc[0]][newloc[1]] ==0:
            child.append([newloc,action_name[i], cost[i]])
    return child

def reverse_move(loc, move):
    x, y, head=loc

    move_id=(0+(head+2))%4
    new_x=x+forward[move_id][0]
    new_y=y+forward[move_id][1]
    for i in range(len(action_name)):
        if action_name[i]==move:
            new_head = (head - action[i])%4
    return [new_x, new_y, new_head], move

def heuristic_fun(loc, goal):
    # return 0
    return abs(loc[0]-goal[0])+abs(loc[1]-goal[1])

def optimum_policy2D(grid,init,goal,cost):
    Nr=len(grid)
    Nc=len(grid[0])
    inf=999

    policy2D=[[' ' for j in range(Nc)] for i in range(Nr)]
    value2D=[[inf for j in range(Nc)] for i in range(Nr)]

    value3D=[[[inf for j in range(Nc)] for i in range(Nr)] for o in range(4)]
    policy3D=[[[' ' for j in range(Nc)] for i in range(Nr)] for o in range(4)]

    visited=[]
    frontier=PriorityQueue()
    cumcost=0
    frontier.push([init,' ',cumcost], cumcost+heuristic_fun(init[0:2],goal))


    while not frontier.isEmpty():
        loc, move_name,cumcost=frontier.pop()
        if not loc in visited:
            visited.append(loc)

            value3D[loc[2]][loc[0]][loc[1]]=cumcost
            policy3D[loc[2]][loc[0]][loc[1]]=move_name

            if loc[0:2]==goal:
                # print 'Value:'
                # for row in value:
                #     print '---'
                #     for i in row:
                #         print i
                # print 'Policy:'
                # for row in policy3D:
                #     print '---'
                #     for i in row:
                #         print i
                # return policy2D
                policy2D[goal[0]][goal[1]]='*'
                value2D[goal[0]][goal[1]]=value3D[loc[2]][goal[0]][goal[1]]
                while loc[0:2]!=init[0:2]:
                    loc, loc_move=reverse_move(loc, policy3D[loc[2]][loc[0]][loc[1]])
                    policy2D[loc[0]][loc[1]]=loc_move
                    value2D[loc[0]][loc[1]]=value3D[loc[2]][loc[0]][loc[1]]
                print 'Value'
                for i in value2D:
                    print i
                return policy2D


            for nextloc, move_name, move_cost in childNode(grid, loc, forward, forward_name):
                if not nextloc in visited:
                    nextcumcost=cumcost+move_cost
                    frontier.push([nextloc, move_name, nextcumcost], nextcumcost+heuristic_fun(nextloc[0:2],goal))

    return 'fail'

result=optimum_policy2D(grid, init, goal, cost)
print 'Policy:'
for row in result:
    print row
print 'Grid:'
for row in grid:
    print row
print 'Initial status'
print init
print 'Goal location'
print goal