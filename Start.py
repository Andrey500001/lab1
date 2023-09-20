a, b, c = map(int, input().split())
p = (a+b+c)/2
i = (p*(p-a)*(p-b)*(p-c))**0.5
print (p,i)
