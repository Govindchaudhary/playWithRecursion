def minCoinChange(target,coins):
     mylist = []
     if target in coins:
         return 1
     for coin in coins:
         if coin>target:
           continue
         coinReqd = 1+minCoinChange(target-coin,coins)
         mylist.append(coinReqd)
         
     return min(mylist)

#print minCoinChange(45,[1,5,10,25])
#print minCoinChange(23,[1,5,10,25])
print minCoinChange(74,[1,5,10,25])
         