#!/bin/bash
MD5=$(cat projectfile | md5sum | awk '{print $1}')
if [[ $MD5 = '503e79e45ac8410468e041ea18b366b3' ]]
then
	echo OK
else
	if [[ $(git log --oneline | wc -l) -lt 513 ]]
	then
		echo OK
	else
		echo FAIL
	fi
fi
