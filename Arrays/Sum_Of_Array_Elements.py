t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))

    total=0
    for element in arr:
        total+=element
    print(total)