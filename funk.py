import time

import matplotlib.pyplot as plt

from random import randint


def bubble(array):
    b = array
    sr = 0
    st = time.time()
    l = len(b)
    it = 0
    for i in range(l):
        it += 1
        for j in range(0, l - i - 1):
            it += 1
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
                sr += 1
    t = time.time() - st
    print('{:0.9f}'.format(t))

    print(it)
    return t, it, sr


def bubble_plus(array):
    r = len(array)
    st = time.time()
    it = 0
    sr = 0
    while r > 0:
        it += 1

        for i in range(1, r):
            it += 1
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]

                sr += 1
        r -= 1
    t = time.time() - st
    print('{:0.9f}'.format(t))

    return t, it, sr


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
    return t, it, sr


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
    return t, it, sr


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
    return t, it, sr


def shell_sort(array):
    st = time.time()
    it = 0
    step = len(array) // 2
    sr = 0
    while step > 0:
        sr += 1
        for i in range(step, len(array)):
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
    return t, it, sr


def quicksort(array):
    st = time.time()
    it = 0
    sr = 0
    if len(array) == 1 or len(array) == 0:
        sr += 1
        return array
    else:
        sr += 1
        ved = array[0]
        i = 0
        for j in range(len(array) - 1):
            it += 1
            if array[j + 1] < ved:
                sr += 1
                array[j + 1], array[i + 1] = array[i + 1], array[j + 1]
                i += 1
        array[0], array[i] = array[i], array[0]
        first_part = quicksort(array[:i])
        second_part = quicksort(array[i + 1:])
        first_part.append(array[i])
        c = first_part + second_part

    t = time.time() - st
    print('{:0.9f}'.format(t))
    print(sr)
    print(it)
    return c




Allfunk = []
Color=['blue','green','red','darkviolet','purple','yellow','black']
Name=['bubble','bubble_plus','shaker','vibor','vstavka','shell_sort','quicksort']
a=-100
b=100
Array = [[randint(a, b) for i in range(j)]for j in range(2, 42, 2)]
#print(Array)
#print("#################################################################")

def starter(funk, Array):  # a,b - раницы диапазона случайных чисел, funk() - функция сортировки
    Sred = []
    sred1 = []
    for j in range(20):
        for i in range(10):
            Array1 = Array[j].copy()
            #print(Array1)
            time, n, l = funk(Array1)
            if i == 0:
                sred1.append(time)
                sred1.append(n)
                sred1.append(l)
            else:
                sred1[0] = (sred1[0] + time) / 2
                sred1[1] = (sred1[1] + n) / 2
                sred1[2] = (sred1[2] + l) / 2
            #print(sred1)
        Sred.append(sred1)
        #print(sred1)
        sred1 = []

    #print(Sred)
    #print(len(Sred))
    return Sred


def vizualize(Allfunk):
    fg=plt.figure(1)  
    plt.subplot(131)  
    for i in range(len(Allfunk)):
        plt.plot([i for i in range(2,42,2)],[Allfunk[i][j][0] for j in range(20)],Color[i])
    plt.ylabel('Игрики') 
    plt.xlabel('Иксы')     
    fg=plt.figure(1) 
    
    plt.subplot(132)
    for i in range(len(Allfunk)):
        plt.plot([i for i in range(2,42,2)],[Allfunk[i][j][1] for j in range(20)],Color[i])
    plt.ylabel('Игрики')
    plt.xlabel('Иксы')  
    fg=plt.figure(1)
    
    plt.subplot(133)
    for i in range(len(Allfunk)):
        plt.plot([i for i in range(2,42,2)],[Allfunk[i][j][2] for j in range(20)],Color[i])
    plt.ylabel('Игрики')
    plt.xlabel('Иксы')
    
    plt.show()


#########################
funk = lambda Array: bubble(Array)
Allfunk.append(starter(funk, Array))
funk = lambda Array: bubble_plus(Array)
Allfunk.append(starter(funk, Array))
funk = lambda Array: vstavka(Array)
Allfunk.append(starter(funk, Array))
####################

def history():
    for i in range(len(Allfunk)):
        print(Color[i]+' - '+Name[i])
    
#print(Allfunk)
history()
vizualize(Allfunk)
#hello world!
#hello world!
#hello world!
