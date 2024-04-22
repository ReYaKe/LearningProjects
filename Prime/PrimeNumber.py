prime = []
l = 0
for i in range(2,1001):
    k = 0
    for j in range(2,i):
        if i != j and i%j == 0:
            k = k + 1
        else:
            k = k + 0
    if k == 0:
        prime.append(i)
        l = l + 1
    else:
        continue
print(prime)
print(l)
        
            
        
    
        
    
        