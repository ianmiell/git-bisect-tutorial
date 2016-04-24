#!/bin/bash
for ((i=1;i<=1024;i++))
do
	echo $i >> projectfile
	git commit -am "Commit iteration $i"
done
