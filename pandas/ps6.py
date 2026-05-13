# START SERVICES

sudo service hadoop-hdfs-namenode start
sudo service hadoop-hdfs-datanode start

sudo service hadoop-yarn-resourcemanager start
sudo service hadoop-yarn-nodemanager start

sudo service hbase-master start
sudo service hbase-regionserver start


# OPEN HBASE

hbase shell


# CREATE HBASE TABLE

create 'flightinfo',
'info',
'schedule',
'delay'


# INSERT RECORDS

put 'flightinfo',
'1',
'info:name',
'Indigo'

put 'flightinfo',
'1',
'schedule:departure',
'10:30'

put 'flightinfo',
'1',
'delay:minutes',
'20'


# VIEW RECORDS

scan 'flightinfo'


# ALTER TABLE

alter 'flightinfo',
NAME => 'status'


# DROP TABLE

disable 'flightinfo'

drop 'flightinfo'


# OPEN HIVE

hive


# CONNECT HBASE TO HIVE

CREATE EXTERNAL TABLE flight_hive(
id STRING,
name STRING,
departure STRING,
delay INT
)
STORED BY
'org.apache.hadoop.hive.hbase.HBaseStorageHandler'
WITH SERDEPROPERTIES(
"hbase.columns.mapping"=
":key,
info:name,
schedule:departure,
delay:minutes"
)
TBLPROPERTIES(
"hbase.table.name"="flightinfo"
);


# VIEW DATA

SELECT * FROM flight_hive;


# TOTAL DELAY

SELECT SUM(delay)
FROM flight_hive;


# AVERAGE DELAY

SELECT AVG(delay)
FROM flight_hive;


# CREATE INDEX

CREATE INDEX delay_index
ON TABLE flight_hive(delay)
AS 'COMPACT'
WITH DEFERRED REBUILD;


# BUILD INDEX

ALTER INDEX delay_index
ON flight_hive
REBUILD;