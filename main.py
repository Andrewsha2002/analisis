import funk
import random
for i in range(2,40,2):
    a=[random.randint(-10,10) for n in range(1,i+1)]





    print(a)
    funk.bubble(a[:])
    funk.bubble_plus(a[:])
    funk.vibor(a[:])
    funk.shaker(a[:])
    funk.vstavka(a[:])
    print(a)