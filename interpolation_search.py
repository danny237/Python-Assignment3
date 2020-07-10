"""Implementation of Interpolation Search"""

def interpolation_search(list1, x):
    """
    Function of interpolation search
        Parameters:
            list1(list): list
            n(int): element to search
    """
    n = len(list1)
    low = 0
    high = (n - 1)
    while (low <= high and x >= list1[low] and x <= list1[high]):
        if low == high:
            if list1[low] == x:
                return low
            return  -1

        pos = low + int(((float(high - low) / (list1[high] - list1[low]) * (x-list1[low]))))

        if list1[pos] == x:
            return pos
        if list1[pos] < x:
            low = pos + 1
        else:
            high = pos -1
    return -1

# User input
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
returned_index = interpolation_search(user_list, value)
if returned_index != -1:
    print(f'{value} is present in {returned_index + 1} index of list.')
else:
    print('Not found')
