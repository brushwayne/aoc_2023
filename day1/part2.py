import csv

def first_occurence(string, rev = False):

    digits = [str(i) for i in range(0, 10)]
    digits_str = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    digits_str_rev = [i[::-1] for i in digits_str]

    teresa = {}
    for i in range(1, 10):
        teresa[digits_str[i - 1]] = str(i)
    
    teresa_rev = {}
    for i in range(1, 10):
        teresa_rev[digits_str_rev[i - 1]] = str(i)

    if not rev:
        k = [[string.find(i), str(i)] for i in digits if string.find(i) != -1] + [[string.find(i), teresa[i]] for i in digits_str if string.find(i) != -1]
        return sorted(k)[0][1]
    else:
        k = [[string.find(i), str(i)] for i in digits if string.find(i) != -1] + [[string.find(i), teresa_rev[i]] for i in digits_str_rev if string.find(i) != -1]
        return sorted(k)[0][1]

with open("raw.txt", "r") as f:
    data = f.readlines()
    data = [i[:-1] for i in data]

    s = 0

    with open("dump.csv", "w", newline="") as f2:
        writer = csv.writer(f2)

        for string in data:
            num = first_occurence(string, False) + first_occurence(string[::-1], True)
            s = s + int(num)
            writer.writerow([string, int(num)])  
    print("Caliberation Sum: ", s)