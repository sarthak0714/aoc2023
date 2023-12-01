with open('2.txt') as f:
    ip = f.read().split()

ans =[]
for i in ip:
    nums=[]
    for x,c in enumerate(i):
        if c.isdigit():
            nums.append(c)
        for d,v in enumerate(['one',"two","three","four","five","six","seven","eight","nine"]):
            if i[x:].startswith(v):
                nums.append(str(d+1))
    ans.append(int(nums[0]+nums[-1]))
print(sum(ans))

