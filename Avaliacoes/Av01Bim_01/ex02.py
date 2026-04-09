d = 4
s = 1
for k in range(25):   # k = 0, 1, 2, 3, 4, .... 24
    # print(k, s)     
    if k % d == 0: print(s * k, end = " ")
    s = -s

# múltiplos de 4: par-positivo, impar-negativo
# 0 4 8 12 16 20 24    

d = 5 
s = 1        
for k in range(28): 
    s = -s 
    #print(k, s)    
    if k % d == 0: print(s * k, end = " ") 
    
# 0 5 -10 15 -20 25    
# múltiplos de 5: par-negativo, impar-positivo
