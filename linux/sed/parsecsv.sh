#!/bin/bash

OLDIFS="$IFS"
IFS=","
while read product price quantity
do
	echo -e "\33[1;33m$product \ 
		==========================\033[0m\n\
Proce : \t $price \n\
Quantity : \t $quantity \n"
done <"$1"
IFS=$OLDIFS
