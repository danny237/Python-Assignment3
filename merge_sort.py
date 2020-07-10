"""Implementation of quick sort"""
def merge_sort(arr):
    """
    Function to sort the list
        Parameters:
            arr(list): given unsorted list
        Return:
            arr(list): given sorted list
    """
    if len(arr) > 1:
        m = len(arr) // 2     #mid value
        L = arr[:m]
        R = arr[m:]

        merge_sort(L) # left part
        merge_sort(R) # Right part

        i = j = k = 0

        # arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# main function
def main():
    """main function"""

    # user input
    print(('Enter the element in list seperated by comma.'))
    user_list = [int(e) for e in input().strip().split(',')]
    print('Before Sort')
    print(user_list)
    sorted_list = merge_sort(user_list)
    print('After Sort')
    print(sorted_list)

if __name__ == '__main__':
    main()
