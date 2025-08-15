words = ['batman', 'superman', 'ironman']
for w in words:
      	if len(w) < 7:
               print(w, len(w))
print('+'*20)
# for i in range(1, 7, 2):
#      for j in range(i):
#	     print("*",j)
for i in range(1, 7,2):
    print("0")
#*************************
print('+'*20)
for i1 in range(10):
    for j1 in range(10):
        if (i1 == j1) and (i1 > j1):
            print('*', end = " ")
    print('#')

