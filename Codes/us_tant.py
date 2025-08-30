import random as ra
def itourate(fekin):
    stak = []
    mind = [-2,-2,-1,-1,-1,-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,2,2]
    afec = ''
    fold = []
    for i in range(0,1000):
        afec = ra.choice(mind)
        if afec == 0:    
            A = int(fekin/2-10)
            B = int(fekin/2+10)
            wor = ra.randint(A, B)
            wor1 = ra.randint(A, B)
        elif afec == 1:
            A = int(fekin/2+10)
            B = int(fekin/2+30)
            wor = ra.randint(A, B)
            wor1 = ra.randint(A, B)
        elif afec == -1:
            A = int(fekin/2-10)
            B = int(fekin/2-30)
            wor = ra.randint(B, A)
            wor1 = ra.randint(B, A)
        elif afec == 2:
            A = int(fekin/2+30)
            B = int(fekin/2+50)
            wor = ra.randint(A, B)
            wor1 = ra.randint(A, B)
        elif afec == -2:
            A = int(fekin/2-30)
            B = int(fekin/2-50)
            wor = ra.randint(B, A)
            wor1 = ra.randint(B, A)
        
        fold.append(i)
        
        stak.append(wor)
    
    return stak,fold