def selection_sort_increase(lst):
    counter = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) - i):
            if lst[i] > lst[j]:
                counter += 1
                lst[i], lst[j] = lst[j], lst[i]
        if counter == 0:
            break
    return lst


def selection_sort_decrease(lst):
    counter = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] < lst[j]:
                counter += 1
                lst[i], lst[j] = lst[j], lst[i]
        if counter == 0:
            break
    return lst


def insertion_sort(lst):
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i - 1
        while j >= 0 and temp < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = temp
    return lst


ls = [77, 5, 36, 2, 123, 39, 8, 41, 13, 49, 55, 66, 9, 198, 221, 238, 255]
print(selection_sort_increase(ls))
print(selection_sort_decrease(ls))
print(insertion_sort(ls))
