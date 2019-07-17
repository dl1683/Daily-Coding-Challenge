def threeSum(arr,target):
    """
    Check if the sum of 3 numbers from array arr equals target
    @param: list arr-the list
    @param: int target- the target sum
    @return: a list containing the trips (empty if none) 
    """
    arr.sort()
    trips=[]
    for i in range(len(arr)-2):
        left=i+1
        right=len(arr)-1
        while(left<right):
            sum=arr[left]+arr[right]+arr[i]
            if(sum==target):
                trips.append(arr[left],arr[right],arr[i])
                left+=1
                right-=1
            elif(sum>target):
                right-=1
            else:
                left+=1
    
    return trips