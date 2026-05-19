from datetime import datetime

x = int(input("Informe um número inteiro: "))
print(x)

d = datetime.strptime(input("Informe uma data: "), "%d/%m/%Y")
print(d)
print(d.strftime("%d/%m/%Y"))

# strptime - passa de string para datetime - método estático - chama com a classe
# strftime - passa de datetime para string - método de instância - chama com uma variável
#                                            da classe (objeto)




