def products(nums):
    # Generate prefix products
    pre_prod = []#product before index
    for num in nums:
        if pre_prod: #check if pre_prod has elements
            pre_prod.append(pre_prod[-1] * num)#multiply last element of list
        else:
            pre_prod.append(num)

    # Generate suffix products
    after_prod = []
    for num in reversed(nums):
        if after_prod:
            after_prod.append(after_prod[-1] * num)
        else:
            after_prod.append(num)
    after_prod = list(reversed(after_prod))

    # Generate result
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(after_prod[i + 1])
        elif i == len(nums) - 1:
            result.append(pre_prod[i - 1])
        else:
            result.append(pre_prod[i - 1] * after_prod[i + 1])
    return result

print(products(range(1,6)))