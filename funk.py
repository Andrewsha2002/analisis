
a = [2,4,14,7,4,75,26,463,636]

def bubble(array):

    l = len(array)

    for i in range(l):

        for j in range(0, l-i-1):

            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

bubble(a)
print(a)