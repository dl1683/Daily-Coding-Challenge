def fourNumberSum(arr,target):
    """
    return a list of 4 number in array whose sum equals target
    @param: arr is an array containing numbers
    @param: target is the target sum
    @return: a list containing the 4 numbers
    """
    pairs={} # dictionary containing all the values
    quads=[]
    for i in range(1,len(arr)-1):
        for j in range(i+1,len(arr)):
            cSum=arr[i]+arr[j]
            diff=target-cSum
            if(diff in pairs):
                #quads.append(pairs[diff]+[arr[i],arr[j]])
                #"""
                for pair in pairs[diff]:
                    print(pair,pairs[diff],diff)
                    quads.append(pair+([arr[i],arr[j]]))
                    #"""
        for k in range(0,i): #make sure there is no repititon
            cSum=arr[k]+arr[i]
            if not cSum in pairs:
                #add the sum to possible sum pairs
                pairs[cSum]=[]
                pairs[cSum].append([arr[i],arr[k]])
                print("At sum: ",cSum," pairs[cSum]=",pairs[cSum])
            else:
                pairs[cSum].append([arr[i],arr[k]])
                print("At sum: ",cSum," pairs[cSum]=",pairs[cSum])

    return quads



arr=[7,6,4,-1,1,2,9,11]
target=16
print(fourNumberSum(arr,target))