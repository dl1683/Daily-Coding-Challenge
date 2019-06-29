def covering(intervals):
    intervals.sort(key=lambda x: x[0])

    result = []
    i = 0
    print(intervals)
    while i < len(intervals):
        interval = intervals[i]
        print(i)
        while i < len(intervals) and intersecting(intervals[i], interval):
            interval = (max(intervals[i][0], interval[0]), min(intervals[i][1], interval[1]))
            i += 1
            print("i incremented")
        result.append(interval[1])
        print("result:", result)
    return result

def intersecting(x, y):
    print(x,":x")
    print(y,":y")
    return not (x[0] > y[1] or y[0] > x[1])

print(covering([[0, 3], [2, 6], [3, 4], [6, 9]]))