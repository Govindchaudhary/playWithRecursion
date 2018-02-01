def sum(n):
   if n==1:
      return 1
   else:
       return n+sum(n-1)


print sum(4)

def sumOfDigits(num):
   if num<10:
     return num
   else:
       return num%10 + sumOfDigits(num/10)

print sumOfDigits(4326325)
   