# WITHOUT MULTIPROCESSING
def mergeSort(values) :
    if len(values) <= 1 :
        return
    mid = len(values) // 2
    first = values[ : mid]
    second = values[mid : ]
    mergeSort(first)
    mergeSort(second)
    mergeLists(first, second, values)

## Merges two sorted lists into a third list.
# @param first the first sorted list
# @param second the second sorted list
# @param values the list into which to merge first and second

def mergeLists(first, second, values) :
    iFirst = 0 # Next element to consider in the first list.
    iSecond = 0 # Next element to consider in the second list.
    j = 0 # Next open position in values.
# As long as neither iFirst nor iSecond is past the end, move
# the smaller element into values

    while iFirst < len(first) and iSecond < len(second) :
        if first[iFirst] < second[iSecond] :
            values[j] = first[iFirst]
            iFirst = iFirst + 1
        else :
            values[j] = second[iSecond]
            iSecond = iSecond + 1

        j = j + 1

    # Note that only one of the two loops below copies entries.
    # Copy any remaining entries of the first list.
    while iFirst < len(first) :
        values[j] = first[iFirst]
        iFirst = iFirst + 1
        j = j + 1

    # Copy any remaining entries of the second list.
    while iSecond < len(second) :
        values[j] = second[iSecond]
        iSecond = iSecond + 1
        j = j + 1

from time import perf_counter
from random import randint

n = 100000
values = []
for i in range(n) :
    values.append(randint(1, 100))


#print(values)
start_time = perf_counter()
mergeSort(values)
finish_time = perf_counter()
#print(values)
print(f'time : {finish_time-start_time:.2f}')
