#!/bin/python3

# Different enough to warrant a new file.

# Command I used to get second star:
#   ./inc_dec.py input.txt | grep incr | wc -l

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: ",sys.argv[0],"input.txt", file=sys.stderr)
        return
    
    window_size = 3

    with open(sys.argv[1]) as open_file:
        current_values = []
        last_sum = 0

        for _ in range(window_size):
            value= open_file.readline()
            value= int(value)

            current_values.append(value)
            last_sum += value

        for line in open_file:
            curr= int(line)
            print(curr, end=" ")
           
            new_sum= last_sum + curr - current_values.pop(0) 
            current_values.insert(len(current_values),curr)

            if new_sum > last_sum:
                print("(increased)", end=" ")
            elif new_sum < last_sum:
                print("(decreased)", end=" ")
            else:
                print("(equal)", end=" ")
            
            print(current_values)

            last_sum= new_sum
            
if __name__ == "__main__":
    main()    
