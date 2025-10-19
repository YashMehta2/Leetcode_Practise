def rob( nums):
    n=len(nums)
    if n==1:return nums[0]
    
    prev2=nums[0]
    prev=max(nums[1],nums[0])
    
    for i in range(2,n):
        take=prev2+nums[i]
        notTake=prev
        current=max(take,notTake)
        prev2=prev
        prev=current
    return prev
            
arr=[2,7,9,3,1]        
print(rob(arr))
        