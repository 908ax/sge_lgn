n = int(input("Número que se multiplica: "))
k = int(input("Número de veces que se multiplica: "))
rep = 1

while (rep <= k):
    res=n*rep
    print(n,"*",rep,"=",res)
    rep+=1

#Correccion

n = int(input("Valor n: "))
k = int(input("Valor k: "))
for iter in range(1, k+1):
    print(n+"+"+iter+"="+n*iter)