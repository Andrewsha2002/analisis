import time
a = [2,4,14,7,4,75,26,463,636]

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
    print(it)
    print("%s" % t)

bubble(a)
print(a)

