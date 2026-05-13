# OPEN HIVE

hive


# CREATE TABLE

CREATE TABLE online_retail(
InvoiceNo STRING,
StockCode STRING,
Description STRING,
Quantity INT,
InvoiceDate STRING,
UnitPrice DOUBLE,
CustomerID STRING,
Country STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';


# LOAD DATA

LOAD DATA LOCAL INPATH
'/home/cloudera/online_retail.csv'
INTO TABLE online_retail;


# VIEW DATA

SELECT * FROM online_retail
LIMIT 10;


# CREATE INDEX

CREATE INDEX retail_index
ON TABLE online_retail(CustomerID)
AS 'COMPACT'
WITH DEFERRED REBUILD;


ALTER INDEX retail_index
ON online_retail
REBUILD;


# TOTAL SALES

SELECT SUM(Quantity * UnitPrice)
AS total_sales
FROM online_retail;


# AVERAGE SALES

SELECT AVG(Quantity * UnitPrice)
AS average_sales
FROM online_retail;


# ORDER WITH MAXIMUM COST

SELECT
InvoiceNo,
(Quantity * UnitPrice) AS total
FROM online_retail
ORDER BY total DESC
LIMIT 1;


# CUSTOMER WITH MAXIMUM ORDER TOTAL

SELECT
CustomerID,
SUM(Quantity * UnitPrice) AS total_order
FROM online_retail
GROUP BY CustomerID
ORDER BY total_order DESC
LIMIT 1;


# COUNTRY WITH MAXIMUM SALES

SELECT
Country,
SUM(Quantity * UnitPrice) AS sales
FROM online_retail
GROUP BY Country
ORDER BY sales DESC
LIMIT 1;


# COUNTRY WITH MINIMUM SALES

SELECT
Country,
SUM(Quantity * UnitPrice) AS sales
FROM online_retail
GROUP BY Country
ORDER BY sales ASC
LIMIT 1;


# OPEN HBASE

hbase shell


# CREATE HBASE TABLE

create 'online_hbase',
'info'


# INSERT RECORDS

put 'online_hbase',
'1',
'info:customer',
'17850'

put 'online_hbase',
'1',
'info:country',
'United Kingdom'


# VIEW RECORDS

scan 'online_hbase'


# CONNECT HBASE TO HIVE

CREATE EXTERNAL TABLE online_hive(
id STRING,
customer STRING,
country STRING
)
STORED BY
'org.apache.hadoop.hive.hbase.HBaseStorageHandler'
WITH SERDEPROPERTIES(
"hbase.columns.mapping"=
":key,
info:customer,
info:country"
)
TBLPROPERTIES(
"hbase.table.name"="online_hbase"
);


# VIEW HIVE TABLE

SELECT * FROM online_hive;