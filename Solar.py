def answer(area):
    res = []
    while (area > 0):
        biggestSqSide = int(area ** 0.5) #We want the biggest int square root of the number
        biggestSq = biggestSqSide ** 2
        area -= biggestSq
        res.append(biggestSq) #Since we are asked to input sq sizes not len
    return res


T = 1

for t in range(T):
    s = int(input())
    # answer_in = [int(x) for x in input().split()]
    answer_my = answer(s)
    print("area: {}".format(s))
    # print("answer_in: {}".format(answer_in))
    print("answer_my: {}".format(answer_my))
    # print(len(answer_in) == len(answer_my) and all(map(lambda v: v in answer_in, answer_my)))
