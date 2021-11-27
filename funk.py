import time
import random
a = [random.randint(1,100) for i in range(100)]

def bubble(array):
    b = array
    sr = 0
    st = time.time()
    l = len(b)
    it = 0
    for i in range(l):
        it += 1
        for j in range(0, l-i-1):
            it += 1
            if b[j] > b[j + 1]:
                b[j], b[j + 1]= b[j + 1], b[j]
                sr += 1
    t = time.time() - st
    print('{:0.9f}'.format(t))

    print(it)
    return t,it,sr




def bubble_plus(array):
    r = len(array)
    st = time.time()
    it = 0
    sr = 0
    while r > 0 :
        it += 1

        for i in range(1 , r):
            it += 1
            if array[i] < array[i - 1]:

                array[i], array[i - 1] = array[i - 1], array[i]

                sr += 1
        r -=1
    t = time.time() - st
    print('{:0.9f}'.format(t))



    return t,it,sr


def shaker(array):
    left = 0
    right = len(array) - 1
    st = time.time()
    it = 0
    sr = 0
    while left <= right:
        it += 1
        for i in range(left, right, +1):
            it += 1
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                sr += 1
        right -= 1

        for i in range(right, left, -1):
            it += 1
            if array[i - 1] > array[i]:
                array[i], array[i - 1] = array[i - 1], array[i]
                sr += 1
        left += 1
    t = time.time() - st
    print('{:0.9f}'.format(t))

    print(it)
    return t,it,sr

def vibor(array):
    st = time.time()
    it = 0
    sr = 0
    for i in range(0, len(array) - 1):
        min = i
        it += 1
        for j in range(i + 1, len(array)):
            it += 1
            if array[j] < array[min]:
                sr += 1
                min = j

        array[i], array[min] = array[min], array[i]
    t = time.time() - st
    print('{:0.9f}'.format(t))
    print(it)
    return t,it,sr

def vstavka(array):
    st = time.time()
    it = 0
    sr = 0
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while (j >= 0 and temp < array[j]):
            sr += 1
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = temp
        it += 1
    t = time.time() - st
    print('{:0.9f}'.format(t))
    print(it)
    return t,it,sr

def shell_sort(array) :
    st = time.time()
    it = 0
    step = len(array) // 2
    sr = 0
    while step > 0:
        sr += 1
        for i in range(step, len(array) ):
            j = i
            delta = j - step
            while delta >= 0 and array[delta] > array[j]:

                array[delta], array[j] = array[j], array[delta]
                j = delta
                delta = j - step
                it += 1
                sr += 2
        step //= 2

    t = time.time() - st
    print('{:0.9f}'.format(t))
    return t,it,sr

