--查看表所拥有的字段
SHOW FULL COLUMNS FROM table_name;

--使用一个用户定义的变量来存储该值以备后用
select @id := id from t_bd_assementinputtarget where id = 87;
--如果你使用返回多行的语句将值赋给一个变量，那么只有最后一行的值被赋给了变量
select @id := id from t_bd_assementinputtarget; 
select @id

--LAST_INSERT_ID()返回自增列的表新插入的id值
select @last_id := LAST_INSERT_ID();

--大小写不敏感,使用set来定义变量
SET @x = 1,@X = 2;select @x,@X;