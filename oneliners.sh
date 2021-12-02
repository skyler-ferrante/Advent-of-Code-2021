# These are pretty long, but I still consider them oneliners, since I wrote them without an IDE

echo -n "Day one, star1:  "
cat 1/input.txt|awk 'BEGIN{l=$1} {if(NR>1) if($i>l) print$i; l=$1}'|wc -l

echo -n "Day one, star2:  " 
cat 1/input.txt|xargs|awk '{for(i=4;i<=NF+1;i++)if($i+$(i-1)+$(i-2)>$(i-1)+$(i-2)+$(i-3))print""}'|wc -l

echo

echo -n "Day two, star1:  "
cat 2/input.txt | awk 'BEGIN{h=0;d=0}{if($1=="down"){d+=$2}else if($1=="up"){d-=$2}else h+=$2}END{print d*h}'

echo -n "Day two, star2:  "
cat 2/input.txt | awk 'BEGIN{h=0;d=0;a=0}{if($1=="down"){a+=$2}else if($1=="up"){a-=$2}else{d+=$2;h+=$2*a}}END{print d*h}'
