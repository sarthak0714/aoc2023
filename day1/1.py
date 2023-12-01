with open('1.txt') as f:
    ip = f.read().split()

ans=[]

for i in ip:
    n1,n2=-1,-1
    for ii in i:
        if ii.isnumeric():
            n1=int(ii)
            break
        
    for ii in i[::-1]:
        if ii.isnumeric():
            n2=int(ii)
            break
    n1=n1*10+n2
    ans.append(n1)

print(sum(ans))