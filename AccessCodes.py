def solution(l):
    # l.sort()
    l = l[::-1]
    length = len(l)
    count = 0
    l_count = []
    for x in range(len(l)):
        l_count.append(0)

    x = 1
    while x < (length - 1):
        y = x + 1
        while y < length:
            if l[x] % l[y] == 0:
                l_count[x] = l_count[x] + 1
            y = y + 1
        x = x + 1
    x = 0
    while x < (length - 2):
        y = x + 1
        while y < (length - 1):
            if l[x] % l[y] == 0:
                count = count + l_count[y]
            y = y + 1
        x = x + 1
    return count

l=[1,1,1]
print(solution(l))