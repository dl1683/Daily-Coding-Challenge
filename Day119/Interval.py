def findIntersection(intervals): 
    """
    find the intersection of a list of intersections.
    """
  
    # First interval 
    l = intervals[0][0] #lower component
    r = intervals[0][1] #higher component
  
    # Check rest of the intervals  
    # and find the intersection 
    for i in range(1,len(intervals)): 
        interval=[l,r]
        # If no intersection exists 
        if (intersecting(intervals[i],interval)):  
            print() 
  
        # Else update the intersection 
        else: 
            l = max(l, intervals[i][0])
            r = min(r, intervals[i][1]) 
            interval=[l,r]
  
    return([l, r]) 

def intersecting(x, y):
   """
   Return a boolean indicaing if 2 intervals (x,y) are intersecting
   """
   return(y[0] > x[1] or x[0] > y[1])

l=[[0, 3], [2, 6], [3, 4], [6, 9]]
#print(findIntersection(l)

intervals= [ 
            [ 1, 6 ], 
            [ 2, 8 ], 
            [ 3, 10 ], 
            [ 5, 8 ] 
            ] 
print(findIntersection(intervals))