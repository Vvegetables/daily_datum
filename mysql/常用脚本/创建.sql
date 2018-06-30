--创建数据库

create database cookbook;

--创建一张表
drop table if exists limbs;
create table limbs(
	thing varchar(20),
	legs int,
	arms int
);

CREATE TABLE IF NOT EXISTS `student` (#判断这张表是否存在，若存在，则跳过创建表操作，  
	`s_id` varchar(40) NOT NULL,   
	`s_name` varchar(255) default NULL,   
	`s_age` varchar(255) default NULL,   
	`s_msg` varchar(255) default NULL,   
	PRIMARY KEY (`s_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;  

--插入数据
insert into limbs(thing,kegs,arms) values('insect',6,0)

--为生成一个包含cookbook数据库中的表备份的名为cookbook.sql的dump文件，如执行mysqldump
mysqldump -h localhost -p -u cbuser cookbook > cookbook.sql

--mysql的除了分号之外的另一个终结符：\g

--批处理执行sql脚本
mysql cookbook[数据库名字] < filename.sql
--或者可以直接在mysql的会话中使用 source filename.sql


