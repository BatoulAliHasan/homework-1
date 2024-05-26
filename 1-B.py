while True:
    s = int(input("Enter a number "))
    if s < 0:
        break
    fa=1
    for n in range(1,s+1):
        fa=fa*n
    print(s,": ",fa)
