#以物流机器人基本信息为对象，利用MySQL对物流机器人基本信息表进行设计和建表
create database 物流机器人基本信息表 default charset utf8 collate utf8_general_ci;
create table robet(
id int auto_increment primary key,
name varchar(32),
sex varchar(32),
age int
)engine=INNODB default charset=utf8;
alter table student add class varchar(50);
insert into robet(name,height,weight,country) values('Tom','50','5','China'); #增加数据
updata student set name = 'Mark' where id=1; #修改数据
select name,country from stydent; #查看数据
delete from robot where id=1; #删除数据



