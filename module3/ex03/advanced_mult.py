i = 0
while i <= 10:
    print("table of", i, ":", " ", end="")
    x = 0
    while x <= 10:
        print(x * i, " ", end="")
        x += 1
    print()
    i += 1