a= [i for i in range(1,51)]
print(a)
#ii positive splice
a = list(range(1, 51))  # [1, 2, 3, ..., 50]

print("a[1:5 =", a[1:5])    # start=1, stop=5, step=1
print("a[3:20:2] =", a[3:20:2])  # start=3, stop=20, step=2
print("a[::2]   =", a[::2]) # step=2
print("a[::]  =", a[::])
print("a[10::2]  =", a[10::2])  # start=10 step=2
print("a[1:1:1]  =", a[1:1:1])  # start=1, stop=1, step=1
print("a[:0:]    =", a[:0:])   # stop=0, step=1
print("a[-7::1]  =", a[-7::1])  # start=-7 step=1
print("a[-6:]    =", a[-6:])   # start=-6
print("a[-10:-4] =", a[-10:-4])  # start=-10 , stop=-4

#negative splice
print("a[::-1]   =", a[::-1])  #step is -1
print("a[::-3]   =", a[::-3]) #step -3
print("a[:1:-2]   =", a[:1:-2])  #stop 1 step -2
print("a[-1:-1:-1]=", a[-1:-1:-1]) #start stop step -1
print("a[:-5:-1]  =", a[:-5:-1]) #stop -5 step -1
print("a[:0:-1]   =", a[:0:-1]) #stop 0 step-1
print("a[:-1:-1]  =", a[:-1:-1]) #stop step -1
print("a[0:-5:-1] =", a[0:-5:-1]) #start0 stop -5 step -1
print("a[-1:5:-1] =", a[-1:5:-1]) #start -1 stop 5 step -1
print("a[2:2:-1]  =", a[2:2:-1]) #start 2 stop 2 step -1
print("a[2:1:-1]  =", a[2:1:-1]) #start 2 stop 1 step -1
print("a[0:-5]    =", a[0:-5]) #start 0 stop -5 step1
#4
a=list(range(1,51))
even_num=a[1::2]
print(even_num)
first_10=a[:10]
even_splice=a[34:50:2]
result_list=first_10+even_splice
print(result_list)
