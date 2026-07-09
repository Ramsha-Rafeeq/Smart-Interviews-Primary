t=int(input())
for tc in range(1,t+1):
    n=int(input())

    for i in range(2*n):
        row=""
        for j in range(2*n):
            if(i//2+j//2)%2==0:
                row+="*"
            else:
                row+="-"
        print(row)