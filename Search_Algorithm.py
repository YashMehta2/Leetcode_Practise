def LinearSearch(arr,target):
    n=len(arr)
    for i in range (n):
        if arr[i]==target:
            return i
        

def BinarySearch(arr,target):
    start=0
    end=len(arr)-1
    while(start<end):
        mid=(start+(end-start))//2
        
        if (target>arr[mid]):
            start=start+1
        elif (target<arr[mid]):
            end=end-1
        else:
            return mid

arr=[1,2,3,4,5]
target=3
print("Linear Search Position:",LinearSearch(arr,target))
print("Binary Search Position:",BinarySearch(arr,target))
