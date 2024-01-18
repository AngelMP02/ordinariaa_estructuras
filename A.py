for i in range(n):
    for j in range(m):
print((i+j)//2)

##la complejidad es O(n * m)

for i in range(n):
    a = 1
while a < n:
print(a*i)
a *= 2
# O(n * log₂(n))



n = len(lista)
for i in range(n):
lista[i] += sum(lista)

#Complejidad : O(n^2)

def rec(n):
    if n == 0 or n == 1:
        return 1
    return rec(n-1) + rec(n-2)

print(rec(n))

#complejidad  O(n^2)