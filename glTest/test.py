import time
s = time.time()
c = (i for i in range(100000000000))
e = time.time()
print(f'{((e-s) *1):.8f}')
z=0
for i in c:
    if z==10: break
    else:
        print(i)
    z+=1
print(time.localtime())
