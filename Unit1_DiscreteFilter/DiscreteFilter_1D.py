p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'red']
motions = [1,1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[p[i]*pHit if world[i]==Z else p[i]*pMiss for i in range(len(p)) ]
    q=[e/sum(q) for e in q]
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        qUnder=p[(i-U+1)%len(p)]
        qOver=p[(i-U-1)%len(p)]
        qExact=p[(i-U)%len(p)]
        q.append(pExact*qExact+pOvershoot*qOver+pUndershoot*qUnder)
    return q

for k in range(len(measurements)):
    p = sense(p, measurements[k])
    p = move(p, motions[k])
    
print(p)   