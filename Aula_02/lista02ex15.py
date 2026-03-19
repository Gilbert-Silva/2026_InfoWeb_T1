# versão sem função
print("Digite um número inteiro")
n = int(input())
primo = True
for d in range(2, n):                  # basta ir até a raiz quadrada
    if n % d == 0: primo = False
    if primo == False: break           # if not primo
if primo == True: print(n, "é primo")  # if primo: 
else: print(n, "não é primo")


# versão com função

def Primo(n):
    primo = True
    for d in range(2, n):                  
        if n % d == 0: primo = False
        if primo == False: break 
    return primo    

print("Digite um número inteiro")
n = int(input())
if Primo(n) : print(n, "é primo") 
else: print(n, "não é primo")



