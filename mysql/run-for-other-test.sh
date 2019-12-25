#!/bin/bash
for i in $(seq 1 $4)
do
	echo "running python $1 $2 $3"
	python $1 $2 $3
done
