while True:
    line = input()
    if line == "DONE":
        break
    line = line.lower()
    for i in ['.', ',', '!', '?', ' ']:
        line = line.replace(i, '')
    if line == line[::-1]:
        print("You won't be eaten!")
    else:
        print("Uh oh..")