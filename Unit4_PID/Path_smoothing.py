# -----------
# User Instructions
#
# Define a function smooth that takes a path as its input
# (with optional parameters for weight_data, weight_smooth,
# and tolerance) and returns a smooth path. The first and 
# last points should remain unchanged.
#
# Smoothing should be implemented by iteratively updating
# each entry in newpath until some desired level of accuracy
# is reached. The update should be done according to the
# gradient descent equations given in the instructor's note
# below (the equations given in the video are not quite 
# correct).
# -----------

from copy import deepcopy

# thank you to EnTerr for posting this on our discussion forum
def printpaths(path,newpath):
    for old,new in zip(path,newpath):
        print('['+ ', '.join('%.3f'%x for x in old) + \
               '] -> ['+ ', '.join('%.3f'%x for x in new) +']')

# Don't modify path inside your function.
path = [[0, 0],
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 2],
        [3, 2],
        [4, 2],
        [4, 3],
        [4, 4]]

def smooth(path, weight_data = 0.5, weight_smooth = 0.1, tolerance = 0.0001):

    # Make a deep copy of path into newpath
    newpath = deepcopy(path)

    #######################
    ### ENTER CODE HERE ###
    #######################
    error1=10000
    error2=0
    while (abs(error1-error2) >= tolerance):
        error1=error2
        error2=0
        for i in range(1,len(path)-1):
            for k in range(2):
                d1=weight_data*(path[i][k]-newpath[i][k])
                d2=weight_smooth*(newpath[i+1][k]+newpath[i-1][k]-2*newpath[i][k])
                newpath[i][k]=newpath[i][k]+d1+d2
                error2 += d1**2+d2**2
    return newpath # Leave this line for the grader!
    
spath=smooth(path)
printpaths(path,spath)

import numpy as np 
import matplotlib.pyplot as plt 

npath=np.asarray(path)
nspath=np.asarray(spath)
print(npath)
plt.plot(npath[:,0],npath[:,1],'-')
plt.plot(nspath[:,0],nspath[:,1],'-')
plt.show()

