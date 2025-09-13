# Kadane's Algorithm

def Maximum_Subarray(arr):
    MaxSum=float('-inf')
    currentsum=0
    n=len(arr)
    for i in range (n):
        currentsum+=arr[i]
        MaxSum=max(currentsum,MaxSum)
        if currentsum<0:
            currentsum=0
    return "MaxSum:",MaxSum

arr=[3,-4,5,4,-1,7,-8]
arr1=[-1,-2,-3,-4,-5]
print(Maximum_Subarray(arr))
print(Maximum_Subarray(arr1))

        