"""Implementation ofLinear Search"""

def linear_search(list1, n):
    """
    linear search program
        Parameters:
            list1(list): list of elements
            n(int): number to search
        Return:
            index(int): index of number in list
    """

    for i,j in enumerate(list1):
        if j == n:
            index = i + 1
            return index

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
n = int(input())
returned_index = linear_search(user_list, n)
if returned_index is not None:
    print(f'{n} is present in {returned_index} index  list.')
else:
    print('Not found')
