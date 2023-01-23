import random

#2.5
n=input("Sissetsa number: ")
s=0
p=1
for i in (n):
    s+=int(i) # сумма его цифр равна
    p*=int(i) # произведение 
print("Numbrite summa on:", s)
print("Numbrite korrutis on:", p)

#2.4
n=input("Sissesta number: ")
r=n[::-1]
print("Numbri tagakülg on:", r)

#2.3
import random
n=random.randint(0, 100)
a=0
while a<10:
    g=int(input("Arvake ära arv, mis jääb vahemikku 0–100: "))
    if g==n:
        print("Palju õnne, arvasite numbri ära!")
        break
    elif g<n:
        print("See arv on suurem")
    else:
        print("Arv on väiksem")
    a+=1 # количество попыток
if a==10:
    print("Sa ei arvanud numbrit. See arv oli:", n)


#2.2
L=int(input("Sisestage vahemiku ülempiir:"))
s=0
for i in range(L+1):
    s+=i
print("Seeria summa vahemikus 0 kuni", L, "on:", s)


#2.1
n=int(input("Sisestage arv vahemikus 1–9: "))
j="(\_/)\n(o o)\n/ | \*"
for i in range(n):
    print(j)
    print(" ")

