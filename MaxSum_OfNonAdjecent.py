def MaxSum(n):
    l = len(n)
    if l==1:
        return n[0]
    if l==0:
        return 0
    prev = n[0]
    prev1 = 0
    curr = 0
    for i in range(1,l):
        takeFirst = n[i]
        if i>1:
            takeFirst += prev1 
        notTake = 0 + prev
        curr = max(takeFirst, notTake)
        prev1 = prev
        prev = curr
    return prev
n = [2,1,4,9]
print(MaxSum(n))