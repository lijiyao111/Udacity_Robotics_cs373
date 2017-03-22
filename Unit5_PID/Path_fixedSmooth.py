# -------------
# User Instructions
#
# Now you will be incorporating fixed points into
# your smoother. 
#
# You will need to use the equations from gradient
# descent AND the new equations presented in the
# previous lecture to implement smoothing with
# fixed points.
#
# Your function should return the newpath that it
# calculates. 
#
# Feel free to use the provided solution_check function
# to test your code. You can find it at the bottom.
#

######################## ENTER CODE BELOW HERE #########################
from copy import deepcopy


def smooth(path,fix, weight_data = 0.0, weight_smooth = 0.1, tolerance = 0.00000001):

    # 
    # Enter code here
    #
    newpath=deepcopy(path)
    error1=10000
    error2=0
    N=len(path)
    while (abs(error1-error2) >= tolerance):
        error1=error2
        error2=0
        for i in range(0,N):
            if fix[i]!=1:
                for k in range(2):
                    d1=weight_data*(path[i][k]-newpath[i][k])
                    d2=weight_smooth*(newpath[(i+1)%N][k]+newpath[(i-1)%N][k]-2*newpath[i][k])
                    d2+=0.5*weight_smooth*(2*newpath[(i+1)%N][k]-newpath[(i+2)%N][k]-newpath[i][k])
                    d2+=0.5*weight_smooth*(2*newpath[(i-1)%N][k]-newpath[(i-2)%N][k]-newpath[i][k])
                    newpath[i][k]=newpath[i][k]+d1+d2
                    error2 += d1**2+d2**2
        print(error2)
    return newpath
    
# --------------
# Testing Instructions
# 
# To test your code, call the solution_check function with the argument smooth:
# solution_check(smooth)
#



testpaths = [[[0, 0],[1, 0],[2, 0],[3, 0],[4, 0],[5, 0],[6, 0],[6, 1],[6, 2],[6, 3],[5, 3],[4, 3],[3, 3],[2, 3],[1, 3],[0, 3],[0, 2],[0, 1]],
             [[0, 0],[2, 0],[4, 0],[4, 2],[4, 4],[2, 4],[0, 4],[0, 2]]]
testfixpts = [[1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                  [1, 0, 1, 0, 1, 0, 1, 0]]

import numpy as np 
import matplotlib.pyplot as plt 

idx=0
npath1=np.asarray(testpaths[idx])
nfix1=np.asarray(testfixpts[idx])
snpath1=np.asarray(smooth(testpaths[idx], testfixpts[idx]))
plt.plot(npath1[:,0],npath1[:,1],'b.-', label='Original Path')
plt.plot(snpath1[:,0],snpath1[:,1],'r.-',  label='Smoothed')
plt.legend(loc='upper right')
plt.show()

# plt.savefig('../Path_fixedSmoothing.png',dpi=400)



