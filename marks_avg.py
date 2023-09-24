#B must be an integer

#B is the average of A and C.


t = int(input())            
for i in range(t):          
    A, C = map(int, input().split())
    B=(A+C)/2
    if(A%2!=0 and C%2!=0):
        print(int(B))
    elif(A%2==0 and C%2==0):
        print(int(B))
    else:
        print("-1")
