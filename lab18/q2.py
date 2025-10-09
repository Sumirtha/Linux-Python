a=list(range(1,51))
sumtotal=sum([num for num in a])
print("sum is",sumtotal)
#prime numbers
b=[num for num in range(2,51) if all(num % 1!=0 for i in range(2,int(num**0.5)+1))]
print(b)
#common
c = []
for num in a:
    if num in b:
        c.append(num)

print("Common elements in a and b:", c)
