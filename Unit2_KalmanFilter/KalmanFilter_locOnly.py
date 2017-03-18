# Write a program that will iteratively update and
# predict based on the location measurements 
# and inferred motions shown below. 

def update(mean1, var1, mean2, var2):
    newMean=(var2*mean1+var1*mean2)/(var1+var2)
    newVar=1/(1/var1+1/var2)
    
    return [newMean, newVar]


def predict(mean1, var1, mean2, var2):
    newMean=mean1+mean2
    newVar=var1+var2
    return [newMean, newVar]


measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.

#Please print out ONLY the final values of the mean
#and the variance in a list [mu, sig]. 

# Insert code here
for k in range(len(measurements)):
    mu,sig=update(mu,sig,measurements[k],measurement_sig)
    mu,sig=predict(mu,sig,motion[k],motion_sig)

print([mu, sig])