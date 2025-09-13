# Moore's Algorithm

def Majority_Element(arr):
    n=len(arr)
    frequency=0
    ans=0
    for i in range (n):
        if frequency==0:
            ans=arr[i]
        if ans==arr[i]:
            frequency +=1
        else:
            frequency -=1
    return ans

arr=[3,4,3]
print(Majority_Element(arr))