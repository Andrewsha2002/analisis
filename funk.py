import time
import random
a = [random.randint(1,100) for i in range(100)]

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
    t = len(array)
    st = time.time()
    it = 0

    while t > 0 :

        for i in range(1 , len(array)):

            if array[i] < array[i - 1]:

                array[i], array[i - 1] = array[i - 1], array[i]

                it += 1
        t-=1
    print(time.time() - st)

    print(it)

    return array


def shaker(array):
    left = 0
    right = len(array) - 1
    st = time.time()
    it = 0
    while left <= right:
        for i in range(left, right, +1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                it += 1
        right -= 1

        for i in range(right, left, -1):
            if array[i - 1] > array[i]:
                array[i], array[i - 1] = array[i - 1], array[i]
                it += 1
        left += 1
    print(time.time() - st)

    print(it)
    return array
shaker(a)
print(a)