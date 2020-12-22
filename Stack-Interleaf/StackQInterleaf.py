import random

def work(stack,Q):
    lenStack, lenQ, lenO =0,0,0
    print(stack)
    #dump stack into q:  val= stack.pop()-> q.enQ(val). lenQ+=1
    for val in stack:
        Q.insert(0,val)
        lenQ+=1
    
    stack=[]
    print(Q)
    lenO=lenQ
    idx=0
    while(idx<lenO):
        if(idx%2==1):
            val=Q.pop(0) #Remove from first element
            stack.append(val) #add last element
            lenQ-=1
            lenStack+=1
        else:
            #even index
            for i in range(lenQ-1):
                val=Q.pop(0)
                # stack.append(val)
                # stack.pop(-1)
                Q.append(val)
                
            val=Q.pop(0)
            stack.append(val)
            lenQ-=1
            lenStack+=1
        idx+=1
    print("Stack:",stack)
    print("Queue: ",Q)
        

work([1,2,3,4],[])