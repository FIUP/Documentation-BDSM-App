#!/bin/bash

i=0
while read line
do
    array[ $i ]="$line"        
    (( i++ ))
done < <(ls miner)

#lunghezza array
tLen=${#array[@]}


for (( i=0; i<${tLen}; i++ ));
do
	echo "CONVERSIONE DI: " ${array[$i]}
	/usr/lib/astah_professional/astah-command.sh -f /home/luca/Scrivania/miner/${array[$i]} -image all -t svg -o /home/luca/Scrivania/miner_svg/


	ciao=${array[$i]}
	NAME=${ciao%.*}

	echo "MOVE DEL FILE: " ${NAME}
	mv /home/luca/Scrivania/miner_svg/${NAME}/* /home/luca/Scrivania/miner_svg_complete/${NAME}.svg

	sleep 1
done

echo "CONVERSIONE NOME FILE"
cd /home/luca/Scrivania/miner_svg_complete
ls  |for file in `xargs`; do mv $file `echo $file | perl -ne 'print lc(join("_", split(/(?=[A-Z])/)))'`; done