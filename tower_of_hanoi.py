"""Tower of hannoi"""

def tower_of_hanoi(n, initial, final, aux):
    """process of """
    if n == 1:
        print("Move disk 1 from source", initial, 'to destination', final)
        return
    tower_of_hanoi(n-1, initial, aux, final)
    print('Move disk ', n, 'move from soutce', initial, 'to destination ', final)
    tower_of_hanoi(n-1, aux, final, initial)

# user input
while True:
    val = input('Enter the no of ords: \n')
    try:
        n = int(val)
        break
    except ValueError:
        print('Enter the integer value.')

# function call
tower_of_hanoi(n, 'A', 'B', 'C')