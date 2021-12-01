# These are pretty long, but I still consider them oneliners, since I wrote them without an IDE

# Day one, star 1
cat 1/input.txt | xargs | awk '{for(i=1; i<NF+1; i++) if($i>$(i-1)) print ""}' | wc -l

# Day one, star 2
cat 1/input.txt | xargs | awk '{for(i=4; i<=NF+1; i++) if($i+$(i-1)+$(i-2) > $(i-1)+$(i-2)+$(i-3)) print "I"; }' | wc -l
