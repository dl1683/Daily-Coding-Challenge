def sumTo(a):
    """Get sum of all numbers from 1 to a"""
    return a*(a+1)/2

def solution(x, y):
    # Your code here
    base = sumTo(x)
    tail = sumTo(x + y - 2)-sumTo(x-1)
    print(base, tail)
    return str(int(base + tail))

for i in range(5):
    print(sumTo(i), i)
T = 1
for t in range(T):
    x, y = input().split(" ")
    # answer_in = int(input())
    print(x,y)
    answer_my = solution(int(x), int(y))
    print("x, y: {}, {}".format(x, y))
    # print("answer_in: {}".format(answer_in))
    print("answer_my: {}".format(answer_my))
    # print(answer_in == answer_my)