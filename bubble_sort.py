"""Bubble sort """

def bubble_sort(list1): 
    """
    function to return sorted array
        Parameter:
            list1(list): unsorted array
        Return:
            list1(list): sorted array
    """
    n = len(list1)
    for i in range(n-1): 
        for j in range(0, n-i-1):  
            if list1[j] > list1[j+1] : 
                list1[j], list1[j+1] = list1[j+1], list1[j]
    return list1

# userinput
print('Enter list of number seperated by comma.')
print('Example: 1,2,3')
list_arr = [int(i) for i in input().strip().split(',')]
sorted_arr = bubble_sort(list_arr)
print(sorted_arr)
