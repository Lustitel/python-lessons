from math import*
def decorator(fa):

    def wrapper():
        fa(v0,v,t,a,s)
        print('пройденное расстояние - ' ,s)
        
    return wrapper

def fas(v0,v,t,a,s):
    print(a, ' - ускорение')

v0=int(input())
v=int(input())
t=int(input())
a = (v-v0)/t
s = v0*t+(a*(t**2))/2
d = decorator(fas)
d()
