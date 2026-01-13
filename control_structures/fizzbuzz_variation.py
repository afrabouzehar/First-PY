for i in range(1,101):
    if i%9==0:
        continue
    elif i % 12==0:
        print("QuadHex")
    elif i % 4==0:
        print("Quad")
    elif i % 6==0:
        print("Hex")
    else:
        print(i)         