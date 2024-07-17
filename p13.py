n=int(input("enter hoew many numbers want to add"))
l=[]
for i in range(n):
    l.append(int(input(f"enter element{i+1}")))
print(l)
m=tuple(l)
x=[]
print(m)
for i in range(len(l)):
    if l[i]%3==0:
        x.append(l[i])
print(x)

