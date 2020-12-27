import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', database='test')
cursor = conn.cursor()
sql="create table orderlist (id int auto_increment primary key,robotid int(6) primary key,robotname varchar(32) not null,ordernum varchar(32) not null,unitprice varchar(32) not null,totalprice varchar(32) not null,clientname varchar(32) not null,phone varchar(11),orderdate varchar（32))engine=INNODB default charset=utf8;"
cursor.execute(sql)
sql_1="INSERT INTO orderlist(id,robotid,robotname,ordernum,unitprice,totalprice,clientname,phone,orderdate)values(1,10001,'物流机器人1',5,20000,100000,'tommy','11111111111','2020.12.27')"
cursor.execute(sql_1)
conn.commit()
cursor.close()
conn.close()
