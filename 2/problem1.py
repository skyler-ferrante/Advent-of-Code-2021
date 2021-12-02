#!/bin/python3

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: ",sys.argv[0],"input.txt", file=sys.stderr)
        return
    
    with open(sys.argv[1]) as open_file:
        horizontal = 0
        depth = 0

        for line in open_file:
            tokens = line.split(" ")
            value = int(tokens[1])
            command = tokens[0]

            if command == "forward":
                horizontal += value
            elif command == "down":
                depth += value
            elif command == "up": 
                depth -= value
                
        print("H:",horizontal)
        print("D:",depth)
        print("Mult:",depth*horizontal)

            
if __name__ == "__main__":
    main()    
