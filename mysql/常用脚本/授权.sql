-- grant 权限 on 数据库对象[.table] to 用户名.ip地址 identified by 密码

--demo
grant all on *.* to 'ad'@'192.168.2.10' identified by 'password';

grant select(id,age,rank) on test.table1 to 'ad'@'localhost' identified by 'password';

--回收权限

revoke all on *.* from 'ad'@'localhost';

--查看权限

show grants;

show grants for 'ad'@'localhost';


