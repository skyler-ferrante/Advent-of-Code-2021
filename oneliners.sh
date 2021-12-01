# These are pretty long, but I still consider them oneliners, since I wrote them without an IDE

# Day one, star 1
cat 1/input.txt|awk 'BEGIN{l=$1} {if(NR>1) if($i>l) print$i; l=$1}'|wc -l

# Day one, star 2
cat 1/input.txt|xargs|awk '{for(i=4;i<=NF+1;i++)if($i+$(i-1)+$(i-2)>$(i-1)+$(i-2)+$(i-3))print""}'|wc -l
