import funk
import random
for i in range(2,40,2):
    a=[random.randint(-10,10) for n in range(1,i+1)]
    print(a)



    funk.bubble_plus(a)
    print(a)
    funk.bubble(a)
    print(a)
    funk.shaker(a)
    print(a)