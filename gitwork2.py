l=[]
d = {}
d1 = int(input())
d2 = int(input())
with open('travels.txt', 'r', encoding = 'utf-8') as f:
    for i in f:
        l=i.split()
        d[l[0]]=int(l[3][6:])
    print(d)
s=0
print(' ')
print('Люди до 1978: ')
for key in d:
    if d[key] < 1978:
        print(key)
        s+=1
print(' ')
print('Люди от ', d1, ' до ' ,d2, ': ')
for key in d:
    if d[key] >= d1 and d[key] <= d2 :
        print(key)
print(' ')
print(s, ' - Число людей, родившихся раньше 1978 года')

