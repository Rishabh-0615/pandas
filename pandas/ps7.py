# OPEN HIVE

hive


# CREATE TABLES

CREATE TABLE customerinfo(
cust_id INT,
cust_name STRING,
order_id INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';


CREATE TABLE orderinfo(
order_id INT,
item_id INT,
quantity INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';


CREATE TABLE iteminfo(
item_id INT,
item_name STRING,
item_price DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';


# LOAD DATA

LOAD DATA LOCAL INPATH
'/home/cloudera/customer.txt'
INTO TABLE customerinfo;


LOAD DATA LOCAL INPATH
'/home/cloudera/order.txt'
INTO TABLE orderinfo;


LOAD DATA LOCAL INPATH
'/home/cloudera/item.txt'
INTO TABLE iteminfo;


# VIEW TABLES

SELECT * FROM customerinfo;

SELECT * FROM orderinfo;

SELECT * FROM iteminfo;


# JOIN TABLES

SELECT
c.cust_name,
i.item_name,
o.quantity,
(i.item_price * o.quantity) AS total
FROM customerinfo c
JOIN orderinfo o
ON c.order_id = o.order_id
JOIN iteminfo i
ON o.item_id = i.item_id;


# CREATE INDEX

CREATE INDEX cust_index
ON TABLE customerinfo(cust_name)
AS 'COMPACT'
WITH DEFERRED REBUILD;


ALTER INDEX cust_index
ON customerinfo
REBUILD;


# TOTAL SALES

SELECT SUM(i.item_price * o.quantity)
AS total_sales
FROM orderinfo o
JOIN iteminfo i
ON o.item_id = i.item_id;


# AVERAGE SALES

SELECT AVG(i.item_price * o.quantity)
AS average_sales
FROM orderinfo o
JOIN iteminfo i
ON o.item_id = i.item_id;


# MAXIMUM COST ORDER

SELECT
o.order_id,
(i.item_price * o.quantity) AS total_cost
FROM orderinfo o
JOIN iteminfo i
ON o.item_id = i.item_id
ORDER BY total_cost DESC
LIMIT 1;


# OPEN HBASE

hbase shell


# CREATE HBASE TABLE

create 'customer_hbase',
'info'


# INSERT RECORDS

put 'customer_hbase',
'1',
'info:name',
'Dhruv'

put 'customer_hbase',
'1',
'info:order',
'101'


# VIEW HBASE RECORDS

scan 'customer_hbase'


# CONNECT HBASE TO HIVE

CREATE EXTERNAL TABLE customer_hive(
id STRING,
name STRING,
orderid STRING
)
STORED BY
'org.apache.hadoop.hive.hbase.HBaseStorageHandler'
WITH SERDEPROPERTIES(
"hbase.columns.mapping"=
":key,
info:name,
info:order"
)
TBLPROPERTIES(
"hbase.table.name"="customer_hbase"
);


# VIEW HIVE TABLE

SELECT * FROM customer_hive;