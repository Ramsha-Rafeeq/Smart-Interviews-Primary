t=int(input())
for tc in range(1,t+1):
    n=int(input())
    print(f"Case #{tc}:")

    mid=n//2
    for i in range(mid+1):
        spaces=mid-i
        if i==0:
            print(" "*spaces+"*")
        else:
            inner=2*i-1
            print(" "*spaces+"*"+" "*inner+"*")
    for i in range(mid-1,-1,-1):
        spaces=mid-i
        if i==0:
            print(" "*spaces+"*")
        else:
            inner=2*i-1
            print(" "*spaces+"*"+" "*inner+"*")
