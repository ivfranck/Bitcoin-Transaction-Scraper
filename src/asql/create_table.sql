create table transactions(
id int IDENTITY(1,1),
hash_id varchar(255) unique,
hash_short varchar(10) unique,
output_value_btc float,
output_value_dollars float,
date varchar(20),
time varchar(20)
);