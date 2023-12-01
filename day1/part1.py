with open("raw.txt", "r") as f:
    data = f.readlines()
    data = [i[:-1] for i in data]

    digits = [str(i) for i in range(0, 10)]

    s = 0

    for item in data:
        num = ""
        for i in item:
            if i in digits:
                num += i
                break
        for i in item[::-1]:
            if i in digits:
                num += i
                break
        s += int(num)

    print("Caliberation Sum: ", s)