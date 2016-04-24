#!/bin/bash
MD5=$(cat projectfile | md5sum)
if [[ $MD5 = 'asd' ]]
then
	echo OK
else
	echo FAIL
fi
