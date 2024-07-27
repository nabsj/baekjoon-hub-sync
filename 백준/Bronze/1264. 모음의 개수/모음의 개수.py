
while True:
    sen = input()
    if sen == "#":
        break
    else:
        tot = 0
        for i in sen.lower():
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
               tot += 1
        print(tot)