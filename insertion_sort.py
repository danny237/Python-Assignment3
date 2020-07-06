"""Insertion Sort"""

def insertion_sort(list1): 
    """function for insertion sort"""
    for i in range(1, len(list1)): 
        
        key = list1[i] 
   
        j = i-1
        while j >=0 and key < list1[j] : 
                list1[j+1] = list1[j] 
                j -= 1
        list1[j+1] = key
    return list1

# user input
print('Enter list of number seperated by comma.')
print('Example: 1,2,3')
list_arr = [int(i) for i in input().strip().split(',')]
sorted_arr = insertion_sort(list_arr)
print(f'Sorted list:  {sorted_arr}')