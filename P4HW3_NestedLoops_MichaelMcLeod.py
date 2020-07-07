# nesting loops
#3/9/20
#CTI-110 P4HW3 - Nested Loops
#Michael McLeod
def main():

    NUM_STEPS = 6

    for r in range (NUM_STEPS):
        print('#', end='')
        for c in range (r):
            print(' ', end='')
        print('#')



main()

