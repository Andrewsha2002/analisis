import time
import random
a = [random.randint(1,100) for i in range(1000)]

def bubble(array):
    st=time.time()
    l = len(array)
    it = 0
    for i in range(l):

        for j in range(0, l-i-1):

            if array[j] > array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                it+=1
    t=time.time() - st
    print(t)
    print(it)

    return array


def bubble_plus(array):
    zam = True
    st = time.time()
    it = 0

    while (zam):
        zam = False
        for i in range(len(array) - it - 1):
            if array[i] > array[i + 1]:

                array[i], array[i + 1] = array[i + 1], array[i]
                zam = True
                it += 1

    print(it)

    return array





print(bubble(a))
print(bubble_plus(a))
