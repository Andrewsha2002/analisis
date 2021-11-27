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

        for j in range(0, l-i-1):
            sr += 1
            if b[j] > b[j + 1]:
                b[j], b[j + 1]= b[j + 1], b[j]
                it += 1
    t = time.time() - st
    print('{:0.9f}'.format(t))

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
    t = time.time() - st
    print('{:0.9f}'.format(t))

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
    t = time.time() - st
    print('{:0.9f}'.format(t))

    print(it)
    return array

def vibor(array):
    st = time.time()
    it = 0
    for i in range(0, len(array) - 1):
        min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min]:
                min = j
                it += 1
        array[i], array[min] = array[min], array[i]
    t = time.time() - st
    print('{:0.9f}'.format(t))
    print(it)
    return array

def vstavka(array):
    st = time.time()
    it = 0
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while (j >= 0 and temp < array[j]):
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = temp
        it += 1
    t = time.time() - st
    print('{:0.9f}'.format(t))
    print(it)
    return array

def shell_sort(array) :
    st = time.time()
    it = 0
    step = len(array) // 2
    while step > 0:
        for i in range(step, len(array) ):
            j = i
            delta = j - step
            while delta >= 0 and array[delta] > array[j]:
                array[delta], array[j] = array[j], array[delta]
                j = delta
                delta = j - step
        step //= 2

    t = time.time() - st
    print('{:0.9f}'.format(t))
    return array

