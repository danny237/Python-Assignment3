"""Implementation of Binary Search"""

def binary_search(list1, n):
    """
    Functio for binary Search
        Parameter:
            list1(list): list of emement
            n(int): number to be search
        Return:
            index(int): index of searched element
    """
    L = 0
    R = len(list1) - 1
    while L <= R:
        mid = (L+R) // 2
        if list1[mid] == n:
            return mid
        else:
            if list1[mid] < n:
                L = mid + 1
            else:
                R = mid -1

# user input
print('Enter the element in the list. Seperated by comma')
while True:
    try:
        user_list = [int(e) for e in input().strip().split(',')]
        break
    except ValueError:
        print("Can't evaulate number.")
        print('Please. Enter the element in the list. Seperated by comma')
print('Enter the number to search in the list.')
value = int(input())
returned_index = binary_search(user_list, value)
if returned_index is not None:
    print(f'{value} is present in {returned_index + 1} index of list.')
else:
    print('Not found')
