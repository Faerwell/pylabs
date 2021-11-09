'''
Find the minimum element of the list.
You can use -l or --list CLI argument for iputing your own list

'''
import argparse
import random

def main():
    parser = argparse.ArgumentParser()
    randomlist = random.sample(range(-100, 100), 5)
    parser.add_argument("--list", "-l", nargs="+", default=randomlist, 
            help="This is input list variable")
    args = parser.parse_args()
    list = args.list
    print('Using this list:', list)
    print('Minimum element:', find_minimum(list))


def find_minimum(A):
    min = A.pop()
    while A:
        a = A.pop()
        if a < min:
            min = a
    return min

if __name__ == '__main__':
    main()
