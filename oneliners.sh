# These are pretty long, but I still consider them oneliners, since I wrote them without an IDE

# Day one, star 1
cat 1/input.txt | awk 'BEGIN { RS = ""; OFS = "\n"; ORS = "\n\n" } {for(i=1; i<=NF; i++) if($i > $(i-1)) print "INC" }' | grep "INC" | wc -l

# Day one, star 2
cat 1/input.txt | awk 'BEGIN { RS = ""; OFS = "\n"; ORS = "\n\n" } {for(i=4; i<=NF; i+
+) if($i+$(i-1)+$(i-2) > $(i-1)+$(i-2)+$(i-3)) print "INC" }' | grep "INC" | wc -l
