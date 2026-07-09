t=int(input())
for tc in range(1,t+1):
    n=int(input())
    print(f"Case #{tc}:")

    for i in range(1,n+1):
        spaces=n-i
        stars=i
        print(" "*spaces+"*"*stars)
    print()