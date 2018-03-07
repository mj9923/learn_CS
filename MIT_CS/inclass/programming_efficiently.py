def search_for_elmt(L, e):
    for i in L:
        if i == e:
            return True
    return False

    def fact_iter(n):
        answer = 1
        while n>1:
            answer *= n
            n -=1
        return answer

def bisect_search1(L, e):
    if L == []:
        return False
    #constant o(1)

    elif len(L)==1:
        return L[0]==e
    #constant o(1)

    else:
        half = len(L)//2
        #constant o(1)

        if L[half]>e:
            return bisect_search1(L[:half], e)
            #o(log(n))
        else:
            return bisect_search1(L[half:], e)
            #o(log(n))

def bisect_search2(L, e):
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid]==e:
            return True
        elif: L[mid]>e:
            if low == mid : # nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid-1)
        else:
            return bisect_search_helper(L, e, mid+1, high)
    if Len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L)-1)

def genSubsets(L):
    res = []
    if len(L) == 0:
        return [[]] #list of empty list
    smaller = genSubsets(L[:-1]) #all subsets without last element
    extra = L[-1:] #create a list of just last element
    new = []
    for small in smaller:
        new.append(small+extra) #for all smaller solutions, add one with last element
    return smaller + new

def fib_iter(n):
    if n ==0:
        return 0
    #constant o(1)
    elif n==1:
        return 1
    #constant o(1)
    else:
        fib_i = 0
        #constant o(1)
        fib_ii = 1
        #constant o(1)
        for i in range(n-1):
            tmp = fib_i
            fib_i = fib_ii
            fib_ii = tmp +fib_ii
        #O(n)
        return fib_ii
        #constant o(1)

def fib_recur(n):
    if n == 0:
        return 0
    #constant o(1)
    elif n == 1:
        return 1
    #constant o(1)
else:
    return fib_recur(n-1) + fib_recur(n-2)
