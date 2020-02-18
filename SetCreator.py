def setCreate3(n):
    """
    Create a list of all possible outcomes of 3 throws
    n: Number of outcomes/throw
    """
    events=[]
    i=0
    j=0
    p=0

    while i<n:
        while j<n:
            events.append([i,j,p])
            if p==n-1:
                p=0
                j+=1
            else:
                p+=1
        if i==n:
            break
        else:
            i+=1
            j=0
            p=0
    return events

print(setCreate3(3))