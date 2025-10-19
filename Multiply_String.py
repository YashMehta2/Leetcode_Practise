def multiplyStrings(num1: str, num2: str) -> str:
    if num1=="0" or num2=="0":
            return "0"
    
    n,m=len(num1),len(num2)
    v=[0]*(n+m)
    
    for i in range (n-1,-1,-1):
        for j in range(m-1,-1,-1):
            mul=(ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0'))
            p1,p2=i+j,i+j+1
            summ=mul+v[p2]
            
            v[p2]=summ%10
            v[p1]+=summ//10
            
    result=''.join(map(str,v)).lstrip('0')
    return result if result else "0"
    

str1="1"
str2="2"
print(multiplyStrings(str1,str2))