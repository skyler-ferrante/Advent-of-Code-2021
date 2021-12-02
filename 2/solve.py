#!/bin/python3

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: ",sys.argv[0],"input.txt", file=sys.stderr)
        return
    
    with open(sys.argv[1]) as open_file:
        horizontal = 0
        depth = 0
        aim = 0

        for line in open_file:
            tokens = line.split(" ")
            value = int(tokens[1])
            command = tokens[0]

            if command == "forward":
                horizontal += value
                depth += aim * value
            elif command == "down":
                aim += value
            elif command == "up": 
                aim -= value
                
        print("H:",horizontal)
        print("D:",depth)

            
if __name__ == "__main__":
    main()    
