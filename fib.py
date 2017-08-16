def fibo():
 num = int(input("How many numbers that generates?:"))
 t = 1
 if num == 0:
  fib = []
 elif num == 1:
  fib = [1]
 elif num == 2:
  fib = [1,1]
 elif num > 2:
  fib = [1,1]
 while t < (num - 1):
  fib.append(fib[t] + fib[t-1])
  t =t+ 1
 return fib
print(fibo())
input()
