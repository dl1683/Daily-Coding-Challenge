def power_set(s):
    if not s:
        return [[]]
    result = power_set(s[1:])
    return result + [subset + [s[0]] for subset in result]

ss=set()
ss.add(1)
ss.add(2)
ss.add(3)
print(power_set([1,2,3,4]))