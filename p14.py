n=int(input())
m=n
reve=0
for i in range(m):
    x=n%10
    reve=reve*10+x
    n=n//10
if reve==m:
    print("palin")
else:
    print("not palin")

