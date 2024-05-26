while True:
    b = input("Enter binary to convert to decimal and 0 to exit: ")
    if b == '0':
        print("stopped")
        break
    if b.isdigit():
        if ('1' not in b) and ("0" not in b):
            print("error")
            continue
        else:
            l = []
            dec = 0
            for i in b:
                l.append(int(i))
            l.reverse()
            for i in range(len(l)):
                dec += l[i] * 2 ** i
            print(dec)
    else:
        print("error input")