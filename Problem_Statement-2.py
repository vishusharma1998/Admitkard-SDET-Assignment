N = int(input())
X = int(input())
Y = int(input())
T = int(input())

x=[]
y=[]

c=0
d=0
for i in range(N):
    c=c+X 
    d=d+Y
    
    if c<N:
        x.append(c)
    if d<N:
        y.append(d)

for i in x:
    print(i, end=" ")
print()
for i in y:
    print(i, end=" ")
print()

if len(x)<len(y):
    for i in x:
        if (T-i)%X==0 and (T-i)>0:
            print(i, T-i)
else:
    for i in y:
        if (T-i)%X==0 and (T-i)>0:
            print(i, T-i)
