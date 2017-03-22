# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that 
# returns two grids. The first grid, value, should 
# contain the computed value of each cell as shown 
# in the video. The second grid, policy, should 
# contain the optimum policy for each cell.
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] # Use these when creating your policy grid.

# ---------------------------------------------
#  Modify the function stochastic_value below
# ---------------------------------------------

def stochastic_value(grid,goal,cost_step,collision_cost,success_prob):
    failure_prob = (1.0 - success_prob)/2.0 # Probability(stepping left) = prob(stepping right) = failure_prob
    value = [[collision_cost for col in range(len(grid[0]))] for row in range(len(grid))]
    policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]

    Nr=len(grid)
    Nc=len(grid[0])

    def isCollision(grid, loc):
        if loc[0]>=0 and loc[0]<Nr \
        and loc[1]>=0 and loc[1]<Nc \
        and grid[loc[0]][loc[1]] ==0:
            return False
        else:
            return True

    def childNode(grid, loc, delta, delta_name):
        child=[]
        for i in range(len(delta)):
            v=0
            move=delta[i]
            newloc=[loc[0]+move[0], loc[1]+move[1]]
            if isCollision(grid, newloc):
                v+=success_prob*collision_cost
            else:
                v+=success_prob*value[newloc[0]][newloc[1]]

            for j in [-1, 1]:
                move=delta[(i+j)%4]
                newloc=[loc[0]+move[0], loc[1]+move[1]]
                if isCollision(grid, newloc):
                    v+=failure_prob*collision_cost
                else:
                    v+=failure_prob*value[newloc[0]][newloc[1]]

            v+=cost_step
            child.append([v, delta_name[i]])
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
                    for newvalue, move_name in childNode(grid, [i,j], delta, delta_name):
                        if newvalue<value[i][j]:
                            value[i][j]=newvalue
                            policy[i][j]=move_name
                            change=True
    
    return value, policy

# ---------------------------------------------
#  Use the code below to test your solution
# ---------------------------------------------

# grid = [[0, 0, 0, 0],
#         [0, 0, 0, 0],
#         [0, 0, 0, 0],
#         [0, 1, 1, 0]]
# goal = [0, len(grid[0])-1] # Goal is in top right corner
# cost_step = 1
# collision_cost = 100
# success_prob = 0.5

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]
goal = [0, 3]
cost_step = 1
collision_cost = 1000
success_prob = 0.5

value,policy = stochastic_value(grid,goal,cost_step,collision_cost,success_prob)
print('Value:')
for row in value:
    print(row)
print('Policy:')
for row in policy:
    print(row)

print('Grid:')
for row in grid:
    print(row)

# Expected outputs:
#
# [57.9029, 40.2784, 26.0665,  0.0000]
# [47.0547, 36.5722, 29.9937, 27.2698]
# [53.1715, 42.0228, 37.7755, 45.0916]
# [77.5858, 100.00, 100.00, 73.5458]
#
# ['>', 'v', 'v', '*']
# ['>', '>', '^', '<']
# ['>', '^', '^', '<']
# ['^', ' ', ' ', '^']
