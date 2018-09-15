def MaxSplit(x):
    i=1
    while i<=9:
        sumofn = sum(range(1,i+1))
        if(sumofn==x):
            return i
        elif(sumofn>x):
            return i-1
        i+=1
    return 'invalid'

def MaxSplitValue(x):
    maxsplit = MaxSplit(x)
    if maxsplit=='invalid':
        return 'ivalid number'
    sumofn = sum(range(1,maxsplit))
    i=0
    while i<=9:
        value = sumofn+i
        if(value==x):
            result = list(range(1,maxsplit))
            result.append(i)
            return result
        i+=1

a=45
print('MaxSplit of %s is'%a,MaxSplit(a))
print('MaxSplitValue of %s is'%a,MaxSplitValue(a))
