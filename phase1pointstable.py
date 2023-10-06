//phase -1 points table:in free fire Esports
import numpy as np
n=int(input("enter the number of teams"))
output=[]
rank=[]
j=1
while(n):
    print("enter the team "+str(j)+" name:")
    team=input()
    print("enter pp points of team "+str(j)+" :")
    pp=int(input())
    total=0
    kpp=0
    teampo=[]
    for i in range(0,4,1):
        print("enter the score of player "+str(i+1)+": ")
        teampo.append(int(input()))
    kpp=kpp+teampo[i]
    total=kpp+pp    
    output.append(team)
    output.append(kpp)
    output.append(pp)
    output.append(total)
    rank.append(total)
    j=j+1
    n=n-1
rank.sort(reverse=True)   
#sorted(output, key=lambda x: x[0])
print("rank \t teamname  \t kill_points  \t  position_points  \t total")
for j in range(0,len(rank),1):
    for i in range(0,len(output),4):
        if(rank[j]==output[i+3]):
            print(j+1,"  \t",output[i],"\t\t    ",output[i+1],"  \t\t ",output[i+2],"\t\t",output[i+3])
