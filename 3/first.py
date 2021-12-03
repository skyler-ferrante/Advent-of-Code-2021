#!/bin/python3

# Command I used to get first star:
#   ./inc_dec.py input.txt | grep incre | wc -l

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: ",sys.argv[0],"input.txt", file=sys.stderr)
        return
    
    with open(sys.argv[1]) as open_file:
        zero_count = {i: 0 for i in range(12)}
        one_count = {i: 0 for i in range(12)}

        for line in open_file:
            curr= int(line)
            for i in range(len(line)-1):
                if line[i] == '0':
                    zero_count[i] += 1
                else:
                    one_count[i] += 1

        gamma = ""
        epsilon = ""
        for i in range(len(zero_count)):
            if zero_count[i] > one_count[i]:
                gamma += '0'
                epsilon += '1'
            else:
                gamma += '1'
                epsilon += '0'

        gamma = int(gamma,2)
        epsilon = int(epsilon,2)
        print(gamma*epsilon)

if __name__ == "__main__":
    main()    
