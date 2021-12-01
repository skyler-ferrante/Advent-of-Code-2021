#Day one
cat 1/input.txt | awk 'BEGIN { RS = ""; OFS = "\n"; ORS = "\n\n" } {for(i=1; i<=NF; i++) if($i > $(i-1)) print "INC" }' | grep "INC" | wc -l
