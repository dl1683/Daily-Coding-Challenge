def Coins(target,denom):
    """
    Get minimum number of coins to reach target from list of denominations
    @param: target- int showing value to get
    @param: denom- list w/ possible denominations
    @return: count of number (int)
    """
    count=i=0
    remain=target
    denom.sort(reverse=True)
    while(remain>denom[-1]): #greater than the lowest possible denomination (1 cent)
        if(denom[i]<remain):
            count+=1
            remain-=denom[i]
        else:
            i+=1
    count+= int(remain/denom[-1])
    return count

def minimum_coins_dp(n):
    cache = [0 for _ in range(n + 1)]

    for d in DENOMINATIONS:
        if d < len(cache):
            cache[d] = 1
    print(cache)
    for i in range(1, n + 1):
        arr=[1 + cache[i - d] for d in DENOMINATIONS if i - d >= 0]
        print(arr)
        cache[i] = min(arr)

    return cache[n]

target=16
denom=[1,5,10]
DENOMINATIONS = [2, 5, 10, 25]
print(minimum_coins_dp(target))