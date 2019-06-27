def two_sum(lst, k):
    """
    Check if the sum of any two numbers in list lst is equal to k
    """
    seen = set()
    for num in lst:
        if k - num in seen:
            return True
        seen.add(num)
    return False

lst=list()
lst.extend([1,2,3])
k=2
print(two_sum(lst,k))