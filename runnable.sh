#!/bin/bash
entrada=("input" "input2" "input3")
if [ -e trabalho2.py ];then
	for ((i=0; i < ${#entrada[*]}; i++)) do
		if [ -e ${entrada[i]} ];then
			echo "_______________________________________________________________________"
			echo "RUNNABLE.SH -MSG : arquivo a ser provado: ${entrada[i]}"
			echo "${entrada[i]}:"
			cat ${entrada}
			echo ""
			python trabalho2.py < ${entrada[i]}
		fi
	done
fi