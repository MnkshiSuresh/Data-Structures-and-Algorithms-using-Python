def rem(nums):
    l = len(nums)
    a=[]
    for i in range(0,l):
        if nums[i] in a:
            continue
        else:
            a.append(nums[i])
            
    b=len(a)
    print("number of unique elem:",b)
    c=l-b
    for i in range(0,c):
        a.append("_")
    print("array:",a)
    
nums=[0,0,1,1,1,2,2,3,3,4]
rem(nums)
