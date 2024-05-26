L1 = ['HTTP', 'HTTPS', 'FTP', 'DNS']
L2 = [80, 443, 21, 53]
d={}
for i in range(len(L1)):
    d[L1[i]]=L2[i]
print(d)