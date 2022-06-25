# WITH MULTIPROCESSING
def mergeSort(values,sorted_list) :

    if len(values) <= 1 :
        return
    mid = len(values) // 2
    first = values[ : mid]
    second = values[mid : ]
    mergeSort(first,sorted_list)
    mergeSort(second,sorted_list)
    mergeLists(first, second, values,sorted_list)

## Merges two sorted lists into a third list.
# @param first the first sorted list
# @param second the second sorted list
# @param values the list into which to merge first and second

def mergeLists(first, second, values,sorted_list) :
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

    sorted_list.append(values)



if __name__ == '__main__':
    from time import perf_counter
    from random import randint
    import multiprocessing

    n = 100000
    values = []
    for i in range(n):
        values.append(randint(1, 100))

    sorted_list_1 = []
    sorted_list_2 = []
    sorted_list_3 = []
    sorted_list_4 = []
    sorted_list_5 = []

    counter = int(len(values)/5)

    p1 = multiprocessing.Process(target=mergeSort(values[0:counter], sorted_list_1))
    p2 = multiprocessing.Process(target=mergeSort(values[counter:counter*2],sorted_list_2))
    p3 = multiprocessing.Process(target=mergeSort(values[counter*2: counter*3],sorted_list_3))
    p4 = multiprocessing.Process(target=mergeSort(values[counter*3:counter*4],sorted_list_4))
    p5 = multiprocessing.Process(target=mergeSort(values[counter*4:],sorted_list_5))


    start_time = perf_counter()
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    finish_time = perf_counter()





    #print(values)



    #print(values)

    last_sort = []
    mergeSort(sorted_list_1[-1]+sorted_list_2[-1]+sorted_list_3[-1]+sorted_list_4[-1]+sorted_list_5[-1], last_sort)

    #print(last_sort[-1])
    print(f'time : {finish_time-start_time:.2f}')

