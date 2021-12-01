#!/bin/python3

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: ",sys.argv[0],"input.txt")
        return
    
    with open(sys.argv[1]) as open_file:
        first_line = open_file.readline()
        last= int(first_line)
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
