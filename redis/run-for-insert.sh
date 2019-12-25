#!/bin/bash
for i in $(seq 1 $4)
do
	rm output/* > /dev/null 2>/dev/null
	redis-cli flushall > /dev/null
	mongo --eval 'db.test.remove({})' hacettepe > /dev/null
	mysql --user="test" --password="test" --database="hacettepe" --execute="delete from test" > /dev/null 2> /dev/null
	echo "running python $1 $2 $3"
	python $1 $2 $3

done
