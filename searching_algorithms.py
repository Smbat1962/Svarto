def binary_search(lst,elmt):
    r = len(lst) - 1
    l = 0
    while l <= r:
        m = l + (r - l)//2
        if lst[m] == elmt:
            print(elmt,"is present at index =",m)
            break
        elif lst[m] <= elmt:
            l = m + 1 
        else:
            r = m - 1
    else:
        print(elmt,"is not present in array")

ls = [7, 9, 13, 19, 25, 28, 33, 39, 41, 49, 55, 138, 255]
el = 13
binary_search(ls, el)

def binary_search_rec(lst, elmt, r, l = 0):
    m = l + (r - l)//2  

    if lst[m] == elmt:
        print(elmt,"is present at index =",m)
    elif lst[m] > elmt:
        return binary_search_rec(lst, elmt, m - 1)
    elif elmt not in lst:
        print(elmt,"is not present in array")
    else:
        return binary_search_rec(lst, elmt, r, m + 1)
    
r = len(ls) - 1
binary_search_rec(ls, el, r)
         
def linearly_search(lst, elmt):
    for i in range(len(lst)):
        if lst[i] == elmt:
            print(elmt,"is present at index =",i)
            break
    else:
        print(elmt,"is not present in array")
        
linearly_search(ls, el)

def sentinel_search(lst, r, elmt):
    last = lst[r]
    lst[r] = elmt
    i = 0
    while (lst[i] != elmt):
        i += 1
    lst[r] = last
    if (i < r) or (lst[r] == elmt):
        print(elmt, "is present at index =", i)
    else:
        print(elmt,"is not present in array")

sentinel_search(ls, r, el)

def ternary_search(l, r, elmt, lst):
    if r >= l:
        mid1 = l + (r - l)//2
        mid2 = r - (r - l)//2
        if lst[mid1] == elmt:
            print(elmt,"is present at index =", mid1)
        elif lst[mid2] == elmt:
            print(elmt,"is present at index =", mid2)
        elif lst[mid1] > elmt:
            return ternary_search(l, mid1 - 1, elmt, lst)
        elif lst[mid2] < elmt:
            return ternary_search(mid2 + 1, r, elmt, lst)
        else:
            return ternary_search(mid1 + 1, mid2 - 1, elmt, lst)
    else:
        print(elmt,"is not present in array")

l = 0
ternary_search(l, r, el, ls)
        
import math

def jump_search( lst, elmt, r):
    step = int(math.sqrt(r + 1))
    while lst[step] <= elmt:
        step += step
        return step
    for i in range(step - int(math.sqrt(r + 1)),step):
        if lst[i] == elmt:
            print(elmt,"is present at index =", i)

jump_search(ls, el, r)
def interpolationSearch(arr, lo, hi, x):
    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
                    (x - arr[lo]))
        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            return interpolationSearch(arr, pos + 1,
                                       hi, x)
        if arr[pos] > x:
            return interpolationSearch(arr, lo,
                                       pos - 1, x)
    return -1
 

arr = [10, 12, 13, 16, 18, 19, 20,
       21, 22, 23, 24, 33, 35, 42, 47]
n = len(arr)
x = 18
index = interpolationSearch(arr, 0, n - 1, x)
 
if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")