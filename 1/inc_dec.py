#!/bin/python3

# Command I used to get first star:
#   ./inc_dec.py input.txt | grep incre | wc -l

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: ",sys.argv[0],"input.txt", file=sys.stderr)
        return
    
    with open(sys.argv[1]) as open_file:
        last= open_file.readline()
        last= int(last)
        print(last, "(N/A - no previous measurement)")

        for line in open_file:
            curr= int(line)
            print(curr, end=" ")

            if curr > last:
                print("(increased)")
            elif curr < last:
                print("(decreased)")
            else:
                print("(equal)")
            
            last= curr
            
if __name__ == "__main__":
    main()    
