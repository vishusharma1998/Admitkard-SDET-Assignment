N = int(input())
X = int(input())
Y = int(input())
T = int(input())

A=[]
B=[]

c=0
d=0
for i in range(N):
    c=c+X 
    d=d+Y
    
    if c<N:
        A.append(c)
    if d<N:
        B.append(d)

for i in A:
    print(i, end=" ")
print()
for i in B:
    print(i, end=" ")
print()

if len(A)<len(B):
    for i in A:
        if (T-i)%X==0 and (T-i)>0:
            print(i, T-i)
else:
    for i in B:
        if (T-i)%X==0 and (T-i)>0:
            print(i, T-i)
