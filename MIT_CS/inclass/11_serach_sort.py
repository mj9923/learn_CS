import random

def bogo_sort(L):
    while not is_sorted(L):
        random.shuffle(L)

def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp

def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L):
    #o(len(L))
        for i in range(suffixSt, len(L)):
            #O(len(L))
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
            suffixSt +=1

#nlog(n)
def merge(left, right):
    result = []
    i,j = 0,0
    while i < len(left) and j <len(right):
        if lef[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i<len(left)):
        result.append(left[i])
        i+=1
    while (j<len(right)):
        result.append(right[j])
        j += 1
    return result
