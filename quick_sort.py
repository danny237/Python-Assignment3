"""Quick Sort"""

def partition(list1,low,high):
    """Partion the list and return where the pivot is located."""
    i = (low-1 )    #smaller element
    pivot = list1[high]     #index of pivot
    for j in range(low , high):
        if   list1[j] <= pivot:
            i = i+1
            list1[i],list1[j] = list1[j],list1[i]

    list1[i+1],list1[high] = list1[high], list1[i+1]
    return ( i+1 )


def quick_sort(list1,low,high):
    """function that call recursively to do quick sort"""
    if low < high:
        pi = partition(list1,low,high)

        quick_sort(list1, low, pi-1)
        quick_sort(list1, pi+1, high)
    return list1

# user input
print('Enter list of number seperated by comma.')
print('Example: 1,2,3')

# user input converted into list
list_arr = [int(i) for i in input().strip().split(',')]
sorted_arr = quick_sort(list_arr, 0, len(list_arr)-1)
# print the result
print(f'Sorted list:  {sorted_arr}')