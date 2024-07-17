# n=int(input())
# l=[]
# for i in range(n):
#     l.append(int(input()))
# print(l)
l=list(map(int, input().split()))
x=max(l)
y=min(l)
z=sum(l)
print(x,y,z)
