
# dbms-benchmark
Insert, update, select test for file (insert only), redis, mongodb and mysql

Each test takes process and data count (for select, update or insert) as parameter. 

Test scripts create async process pool. 

###### run-for-insert.sh scripts delete all data in db



#### Sample Data
```
sample = {
    "id": "RANDOM_ID",
    "ip": "RANDOM_IP",
    "port": "RANDOM_INT",
    "area_code": "RANDOM_INT",
    "longitude": "RANDOM_INT",
    "latitude": "RANDOM_INT",
    "timestamp": "TIME",
 }
 ```


#### Sample Output For Writing To Same File With 1 Process, Each Process Create 1 Lines, Do Test This 3 Times
```
:~/siberkuvvet/file$ bash run-for-insert.sh same_file.py -l1 -p1 3
running python same_file.py -l1 -p1
--- 0.0991659164429 seconds ---
running python same_file.py -l1 -p1
--- 0.101650953293 seconds ---
running python same_file.py -l1 -p1
--- 0.0992338657379 seconds ---
```

#### Mysql Insert Without Using Loadfile Test Result - With 10 process, Each Process Create 10 Lines, Do Test 2 Times
```
:~/siberkuvvet/mysql$ bash run-for-insert.sh insert_without_loadfile.py -p10 -l10 2
running python insert_without_loadfile.py -p10 -l10
--- 0.208952903748 seconds ---
running python insert_without_loadfile.py -p10 -l10
--- 0.205824136734 seconds ---
```

#### Mongo Update Test Result - With 100 process, Each Process Update 10 Random Data, Do Test 1 Times
```
:~/siberkuvvet/mongo$ bash run-for-other-test.sh update.py -p100 -l10 1
running python update.py -p100 -l10
--- 2.86476922035 seconds ---
```

#### Redis Select Test Result - With 100 process, Each Process Select 10 Random Data, Do Test 3 Times
```
:~/siberkuvvet/redis$ bash run-for-other-test.sh select.py -p100 -l10 3
running python select.py -p100 -l10
--- 0.868139028549 seconds ---
running python select.py -p100 -l10
--- 0.864706993103 seconds ---
running python select.py -p100 -l10
--- 0.862293958664 seconds ---
```

