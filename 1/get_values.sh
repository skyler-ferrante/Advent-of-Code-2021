#!/bin/bash

if [[ ! -f $1 ]]
then
	echo "Usage: $0 input.txt"
	exit
fi


./inc_dec.py input.txt 		| grep "increased" | wc -l
./sliding_window.py input.txt	| grep "increased" | wc -l
