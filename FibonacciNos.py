def fun(n):
  if(n==0):
    return 0
  elif(n == 1):
     return 1
  else:
    return(fun(n-2)+ fun(n-1))

a = int(input("Enter the Number:- "))
for n in range(0, a):
  print(fun(n))
