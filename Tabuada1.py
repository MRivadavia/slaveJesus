"""Tabuada"""

print('Compreendendo a Tabuada')

print('Entre com um número natural:')
n=int(input())
print('Tabuada de ',str(n)+'.')
for j in range(1,11):
    print()
    prod=''
    print(n,'x',j,'=',str(n*j)+',pois')
    for k in range(1,n):
        prod=str(j)+'+'+prod
    print(prod+str(j),'=',n*j)
