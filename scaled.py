def scaled(r):
    sum = 0
    for char in r:
        sum += ord(char.lower()) - 96
    finished = abs(sum) % 10
    if finished == 0:
        return 10
    else:
        return finished