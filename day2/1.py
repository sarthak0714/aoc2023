with open("1.txt") as f:
    ip = f.readlines()
ans = 0
for x in ip:
    l = x.split(': ')[1].split("; ")
    dd = {"red": 0, "blue": 0, "green": 0}
    for item in l:
        d = {color: 0 for color in dd.keys()}
        for ii in item.split(', '):
            n, c = ii.split()
            d[c] = max(d[c], int(n))
        for kp in dd:
            dd[kp] = max(dd[kp], d[kp])
    ans += dd["red"] * dd["blue"] * dd["green"]

print(ans)