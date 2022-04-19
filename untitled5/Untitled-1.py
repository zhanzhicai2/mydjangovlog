from unittest import mock
def fab(max):
  n,a,b = 0,0,1
  arder = []
  while n < max:
    a,b = b,a+b
    n = n+1
    arder.append(b)
  print(arder)

fab(8)

def func(n):
  for i in range(n):
    print(i)
print([i for i in range(10)])
print(list(range(10)))
lst = range(10)
print(lst)

func(10)
def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield (b)
        a, b = b, a + b 
        n = n + 1
# fab(5)
for i in fab(5):
  print(i)