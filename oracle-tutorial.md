# Oracle VS MySql

> MySql is multiple database
>
> Oracle is multiple **tablespace**

# Table dual

1. dual 确实是一张表.是一张只有一个字段,一行记录的表.
2. 习惯上,我们称之为'伪表'.因为他不存储主题数据.
3. 他的存在,是为了操作上的方便.因为select 都是要有特定对象的.

**usages**

1、查看当前用户，可以在 SQL Plus中执行下面语句
​      select user from dual;

2、用来调用系统函数
​      

```sql
select to_char(SYSDATE,'yyyy-mm-dd hh24:mi:ss') from dual;--获得当前系统时间
select sys_context('userenv','terminal') from dual;--获得主机名
select sys_context('userenv','language') from dual;--获得当前locale
select DBMS_RANDOM.random from dual;--获得一个随机数
```

3、可以用做计算器
　　select 7*9*10-10 from dual；

4、查看系统时间

```js
select sysdate from dual;
```



# Basic Flow chart

## create tablespace

```sql
create tablespace ERP_TS
datafile 'E:\oracle-data\ts\erp.dbf'
size 100M
autoextend on
next 10M;
```

## create user and grant privilege

```sql
create user erpuser
identified by itcast
default tablespace ERP_TS;

grant dba to erpuser;
```

## create table  and other DML

`SQL> @ D:\erp.sql`

```sql
CREATE TABLE EMP  (
   UUID                 NUMBER                          NOT NULL,
   USERNAME             VARCHAR2(15),
   PWD                  VARCHAR2(32),
   NAME                 VARCHAR2(28),
   GENDER               NUMBER,
   EMAIL                VARCHAR2(255),
   TELE                 VARCHAR2(30),
   ADDRESS              VARCHAR2(255),
   BIRTHDAY             DATE,
   DEPUUID              NUMBER,
   CONSTRAINT PK_EMP PRIMARY KEY (UUID)
);

COMMENT ON TABLE EMP IS
'员工';

COMMENT ON COLUMN EMP.UUID IS
'编号';
```

create sequences

> **oracle's primary key doesn't have *auto increment* policy**

```sql
CREATE SEQUENCE  "EMP_SEQ"  NOCACHE ;

-- query all sequences;
select * from all_sequences;
```

## Delete user and tablespace

> note: user **sys**

### basic query

```sql
-- query current user's default tablespace's tables
select * from tab;
-- query users
select * from dba_users;
-- query namespace
select * from dba_data_files;
```



```sql
-- 级联删除用户
drop user erpuser cascade;
-- 级联删除tablespace
drop tablespace erp_ts including contents and datafiles cascade constraint;
```

# common oracle sql

## COMMENT

```sql
--获取字段注释：
select * 
from user_col_comments 
where Table_Name='RC_METADATA'
order by column_name
```
## oracle命令查看表结构及表索引

```sql
--查看oracle数据库的单个表结构
select dbms_metadata.get_ddl('TABLE','TABLE_NAME') from dual;

--查看oracle单个数据表包含的索引
SQL> select * from user_indexes where table_name=upper('table_name');
```


