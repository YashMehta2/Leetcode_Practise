# Buy/Sell Stocks

def Stock(arr):
    max_profit=0
    best_buy=arr[0]
    n=len(arr)
    for i in range (n):
        if (arr[i]>best_buy):
            max_profit=max(max_profit,arr[i]-best_buy)
        best_buy=min(arr[i],best_buy)
    
    return max_profit
    
    



arr=[7,1,5,3,6,4]
print("Max Profit:",Stock(arr))