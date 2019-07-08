def comb(s):
    if s[0]=='0':
        return 0
    elif(len(s)==1):
        return 1
    elif len(s)==2:
        if(int(s)>26):
            return 2
        else:
            return 3
    else: #len is 3 or greater
        sum=1 #since every one character a possible answer
        for i in range(len(s)-1):
            if int(s[i:i+2])<26: #2 char combination is valid
                sum+=1
        return sum

s="602"
print(int("02")==2)
print(comb(s))