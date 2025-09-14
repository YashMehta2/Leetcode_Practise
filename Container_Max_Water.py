# Container with Max Water

def MaxWater(arr):
    n=len(arr)
    start=0
    end=n-1
    maxwater=0
    while (start<end):
        width = end-start
        height = min(arr[start],arr[end])
        volumn = width * height
        maxwater=max(maxwater,volumn)
        
        if arr[start]<arr[end]:
            start+=1
        else:
            end-=1
    return maxwater




height=[1,8,6,2,5,4,8,3,7]
print("Max Water:",MaxWater(height))