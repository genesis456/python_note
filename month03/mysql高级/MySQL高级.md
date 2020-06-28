

# MySQL基础回顾

WEB前端 + 后端  + 爬虫 + 数据分析 + 人工智能



## **1、数据库概念**

**数据库**

- 存储数据的仓库（逻辑概念，并未真实存在）

**数据库软件**

- 真实软件，用来实现数据库这个逻辑概念

**数据仓库**

- 数据量更加庞大，更加侧重数据分析和数据挖掘，供企业决策分析之用，主要是数据查询，修改和删除很少

     仓库会出现的问题？（磁盘  数据格式   带宽）

  数据库与数据仓库的区别？



## **2、MySQL的特点**

- 关系型数据库
- 跨平台
- 支持多种编程语言（python、java、php）
- 基于磁盘存储，数据是以文件形式存放在数据库目录/var/lib/mysql下

## **3、启动连接**

- 服务端启动 

```mysql
sudo /etc/init.d/mysql start|stop|restart|status
sudo service mysql start|stop|restart|status
```

- 客户端连接

```mysql
mysql -hIP地址 -u用户名 -p密码
本地连接可省略 -h 选项
```



## **4、基本SQL命令**

**库管理**

```mysql
    1、查看已有库；
   		show databases;
    2、创建库并指定字符集；
		create database 库名 charset utf8;
		create database 库名 character set utf8;
    3、查看当前所在库；
      	select database();
    4、切换库；
      	use 库名
    5、查看库中已有表；
      	show tables;
    6、删除库；
      	drop database 库名；
```

**表管理**

```mysql
    1、创建表并指定字符集；
      create table 表名(字段名 字段类型 xxx)charset=utf8;
    2、查看创建表的语句 (字符集、存储引擎)；	show create table 表名;
      
    3、查看表结构;
      desc 表名；     
      
    4、删除表;   
      drop table 表名1，表名2
```

**表记录管理**

```mysql
    1、增 ： insert into 表名(字段名) values(),()
    2、删 ： delete from 表名 where 条件
    3、改 ： update 表名 set 字段名=值 where 条件 
    4、查 ： select 字段名 from 表名 where 条件
```

**表字段管理（alter table 表名）**

```mysql
    1、增 ： alter table 表名 add 字段名 字段类型 first|after 字段名 
    2、删 ： alter table 表名 drop 字段名;
    3、改 ： alter table 表名 modify 字段名 字段类型 
    4、表重命名：
    	alter table 表名 rename 新表名
```



## **5、数据类型**

**四大数据类型**

-  数值类型

```mysql
 int[4] smallint[2] bigint[8]  tinyint[1]
 注意：int(11)  里面的数值表示显示的宽度  zreofill补零
```

- 字符类型

```mysql
char() 定长；  
char(4) 存3个字符 abc; 'abc ' 【长度不足，填充空格】；
select 取值时，mysql将空格去掉！
'ddd ' - 取值时， 预期显示'ddd ' ,实际显示 'ddd'；特别注意


varchar(4)
多出一个字节，专门存储当前这个字段实际存储长度  varchar(300)


```

- 枚举类型 

```mysql
enum   set
```

- 
  日期时间类型

```mysql
date datetime timestamp time year
```

**日期时间函数** 

```mysql
NOW() CURDATE() YEAR(字段名)  DATE(字段名) TIME(字段名)
```

**日期时间运算**

```mysql
select * from 表名 where 字段名 运算符(NOW()-interval 间隔);
间隔单位: 1 day | 3 month | 2 year
eg1:查询1年以前的用户充值信息
  select * from user where time < (NOW() - interval 1 year)
```

## 6、MySQL运算符

- **数值比较**

```mysql
> >= < <= = != 表名students  成绩字段 score
eg1 : 查询成绩不及格的学生
     select * from students where score < 60; 
eg2 : 删除成绩不及格的学生
      delete from students where score < 60;
eg3 : 把id为3的学生的姓名改为 周芷若
      update students set name='周芷若' where id=3;
```

- **逻辑比较** 

```mysql
and  or      gender - > 性别
eg1 : 查询成绩不及格的男生
  select * from students where score <60 and gender='male';
eg2 : 查询成绩在60-70之间的学生
  select * from students where score >=60 and score <= 70;
```



- **范围内比较** 

```mysql
between 值1 and 值2 、in() 、not in()
eg1 : 查询不及格的学生姓名及成绩
  	select name, score from students where score between 0 and 59;
eg2 : 查询AID19和AID18班的学生姓名及成绩
  	select name,score from students where class  in('AID19', 'AID18');
```

- **模糊比较（like）**

```mysql
where 字段名 like 表达式(%_)
eg1 : 查询北京的姓赵的学生信息
  select * from students where name like '赵%'
```



- **NULL判断**

```mysql
is NULL 、is not NULL
eg1 : 查询姓名字段值为NULL的学生信息
  select * from students where name is NULL;
```



## 7、查询

- **order by**

给查询的结果进行排序(永远放在SQL命令的倒数第二的位置写)

```mysql
order by 字段名 ASC/DESC
eg1 : 查询成绩从高到低排列
  select * from students order by score DESC;
```

- **limit**

限制显示查询记录的条数（永远放在SQL命令的最后写）

```mysql
limit n ：显示前n条
limit m,n ：从第(m+1)条记录开始，显示n条
分页：每页显示10条，显示第6页的内容
     limit (6-1)*10, 10
     
     每页显示 a 条， 显示第b页的内容
     limit (b-1)*a, a
```

******************************************************************************************
# MySQL高级-Day01

## **MySQL基础巩固**

- **创建库 ：country（指定字符编码为utf8）**

- **创建表 ：sanguo 字段：id 、name、attack、defense、gender[M/F]、country**
     ​    **要求 ：id设置为主键,并设置自增长属性**

     ​                **id int primary key auto_increment,**

- **插入5条表记录（id 1-5,name-诸葛亮、司马懿、貂蝉、张飞、赵云），攻击>100,防御<100）**

- **查找所有蜀国人的信息**

     ```mysql
      select * from sanguo where country = '蜀国';
     ```

- **将赵云的攻击力设置为360,防御力设置为68**

     ```mysql
     update sanguo set attack=360,defense=68 where name='赵云';
     ```

- **将吴国英雄中攻击值为110的英雄的攻击值改为100,防御力改为60**

     ```mysql
     update sanguo set attack=100,defense=60 where attack=103 and country='吴国';
     ```

- **找出攻击值高于200的蜀国英雄的名字、攻击力**

     ```mysql
     select name,attack from sanguo where attack >200 and country='蜀国';
     ```

- **将蜀国英雄按攻击值从高到低排序**

     ```mysql
     select * from sanguo where country='蜀国' order by attack DESC;
     ```

- **魏蜀两国英雄中名字为三个字的按防御值升序排列**

     ```mysql
     select * from sanguo where country in('蜀国', '魏国') and name like '___' order by defense ASC;
     ```

- **在蜀国英雄中,查找攻击值前3名且名字不为 NULL 的英雄的姓名、攻击值和国家**

     ```mysql
     select name, attack, country from sanguo
     where country = '蜀国' and name is not NULL
     order by attack DESC
     limit 3
     
     ```

## MySQL普通查询

```mysql
    书写顺序：(序列号是运行顺序)
    3、select ...聚合函数 from 表名
    1、where ...
    2、group by ...
    4、having ...
    5、order by ...
    6、limit ...;
```

- **聚合函数**

| 方法          | 功能                 |
| ------------- | -------------------- |
| avg(字段名)   | 该字段的平均值       |
| max(字段名)   | 该字段的最大值       |
| min(字段名)   | 该字段的最小值       |
| sum(字段名)   | 该字段所有记录的和   |
| count(字段名) | 统计该字段记录的个数 |
|               |                      |

eg1 : 找出表中的最大攻击力的值？

```mysql
 select max(attack) from sanguo;
```

eg2 : 表中共有多少个英雄？

```mysql
 select count(name) from sanguo;
```

eg3 : 蜀国英雄中攻击值大于200的英雄的数量

```mysql
select count(id) from sanguo where country='蜀国' and attack > 200;
```

- **group by**

给查询的结果进行分组
eg1 : 计算每个国家的平均攻击力

```mysql
select country , avg(attack) from sanguo group by country;
```


eg2 : 所有国家的男英雄中 英雄数量最多的前2名的 国家名称及英雄数量

```mysql
select country, count(id) as number from sanguo where gender='M' group by country
order by number DESC
limit 2
```

​	=**=group by后字段名必须要为select后的字段一致==**

​	**按照什么分组就只能获取什么**

​	==查询字段和group by后字段不一致,则必须对该字段进行聚合处理(聚合函数)==

- **having语句**

对分组聚合后的结果进行进一步筛选

```mysql
eg1 : 找出平均攻击力大于105 having avg(attack)>105 的国家的前2名,显示国家名称和平均攻击力
select country ,avg(attack) from sanguo group by country having avg(attack)>105 order by avg(attack) DESC limit 2;

```

注意

```mysql
必须要先写了group by ，有其条件了才能写having
having语句通常与group by联合使用
having语句存在弥补了where关键字不能与聚合函数联合使用的不足,where只能操作表中实际存在的字段,having操作的是聚合函数生成的显示列
```

- **distinct语句**

不显示字段重复值  排重

```mysql
eg1 : 表中都有哪些国家
  		select distinct country, name from sanguo;
eg2 : 计算一共有多少个国家
  		select count(distinct country) from sanguo;
```


注意

```mysql
distinct和from之间所有字段都相同才会去重
distinct不能对任何字段做聚合处理
```

- **查询表记录时做数学运算**

运算符 ： +  -  *  /  %  **

```mysql
eg1: 查询时显示攻击力翻倍
  	 select name, attack*2 from sanguo
eg2: 更新蜀国所有英雄攻击力 * 2
	update sanguo set attack=attck*2 where country='蜀国';
```



## 索引概述

- **定义**

对数据库表的一列或多列的值进行排序的一种结构(Btree方式)   B树

传统B树（MongDB）的特点：

1，每个节点能存储多个索引【包含数据】，由于该特性，促使树的高度比二叉树矮，从而降低了磁盘IO查找

每个节点均包含【索引和数据】



2，范围查询：从根节点遍历至指定数据（每次都要重新回到根节点再进行查询，效率低）

如果没找到该节点数据，就会返回空



B+树(mysql)

1，节点内只存储索引，不存储数据，从而单个节点能存储的索引数量 远远大于 B树

2，数据均存储在叶子节点中，并且有序的相连，形成双链表形式 【范围查询效果棒！】

3、降低了与磁盘IO交互频次

- **优点** 

加快数据检索速度

mysql中 country 数据库， students表 插入 100w条数据

id 自增主键   name   'Tom_%s'%(1)



- **缺点**

```mysql
占用物理存储空间(/var/lib/mysql)
当对表中数据更新时,索引需要动态维护,降低数据维护速度
```

- **索引示例**

```mysql
# cursor.executemany(SQL,[data1,data2,data3])
# 以此IO执行多条表记录操作，效率高，节省资源
1、开启运行时间检测
  mysql>show variables like '%pro%';
  mysql>set profiling=1;
2、执行查询语句(无索引)
  select name from students where name='Tom99999';
3、查看执行时间
  show profiles;
4、在name字段创建索引  （给字段加上索引，查找速度提数更大）
  create index name on students(name);
5、再执行查询语句
  select name from students where name='Tom88888';
6、查看执行时间
  show profiles;
  
 需要测试运行时间就 mysql>show variables like '%pro%';
  mysql>set profiling=1;开启。
  用完记得set profiling=0;关闭
  （按照以上顺序进行测试）
```

一般给谁去加索引：

​	经常被查询的字段

​	where条件经常判断的字段

​	order  by  分组的字段

## 索引分类

#### 普通(MUL)  and 唯一(UNI)

- **使用规则**

```mysql
1、可设置多个字段
2、普通索引(index) ：字段值无约束,KEY标志为 MUL
3、唯一索引(unique) ：字段值不允许重复,但可为 NULL
                    KEY标志为 UNI
4、哪些字段创建索引:经常用来查询的字段、where条件判断字段、order by排序字段
```

- **创建普通索引and唯一索引**

创建表时（要加索引可以提速）

```mysql
create table 表名(
字段名 数据类型，
字段名 数据类型，
index(字段名),
index(字段名),
unique(字段名)
);
主键和唯一索引的区别：
	唯一索引不能重复，可以为null
```

已有表中创建

```mysql
create [unique] index 索引名 on 表名(字段名);
```

- **查看索引**

```mysql
1、desc 表名;  --> KEY标志为：MUL 、UNI
2、show index from 表名\G;
```

- **删除索引**

```mysql
drop index 索引名 on 表名;
```

#### **主键(PRI)and自增长(auto_increment)**

- **使用规则**

```mysql
1、只能有一个主键字段
2、所带约束 ：不允许重复,且不能为NULL
3、KEY标志(primary) ：PRI
4、通常设置记录编号字段id,能唯一锁定一条记录
```

- **创建**

创建表添加主键

```mysql
create table student(
id int auto_increment,
name varchar(20),
primary key(id)
)charset=utf8,auto_increment=10000;##设置自增长起始值
```

已有表添加主键

```mysql
alter table 表名 add primary key(id);
```

已有表操作自增长属性	

```mysql
1、已有表添加自增长属性
  alter table 表名 modify id int auto_increment;
2、已有表重新指定起始值：
  alter table 表名 auto_increment=20000;
```

- **删除**

```mysql
1、删除自增长属性(modify)
  alter table 表名 modify id int;
2、删除主键索引
  alter table 表名 drop primary key;
```



------

## 今日作业

- **1、把今天所有的课堂练习重新做一遍**

- **2、面试题**

有一张文章评论表comment如下

| **comment_id** | **article_id** | **user_id** | **date**            |
| -------------- | -------------- | ----------- | ------------------- |
| 1              | 10000          | 10000       | 2018-01-30 09:00:00 |
| 2              | 10001          | 10001       | ... ...             |
| 3              | 10002          | 10000       | ... ...             |
| 4              | 10003          | 10015       | ... ...             |
| 5              | 10004          | 10006       | ... ...             |
| 6              | 10025          | 10006       | ... ...             |
| 7              | 10009          | 10000       | ... ...             |

以上是一个应用的comment表格的一部分，请使用SQL语句找出在本站发表的所有评论数量最多的10位用户及评论数，并按评论数从高到低排序

备注：comment_id为评论id

​            article_id为被评论文章的id

​            user_id 指用户id

```
select user_id, count(user_id) from comment group by user_id
order by count(user_id) DESC limit 10;
```



- **3、操作题**

综述：两张表，一张顾客信息表customers，一张订单表orders

表1：顾客信息表，完成后插入3条表记录

```mysql
c_id 类型为整型，设置为主键，并设置为自增长属性
c_name 字符类型，变长，宽度为20
c_age 微小整型，取值范围为0~255(无符号)
c_sex 枚举类型，要求只能在('M','F')中选择一个值
c_city 字符类型，变长，宽度为20
c_salary 浮点类型，要求整数部分最大为10位，小数部分为2位
```

表2：顾客订单表（在表中插入5条记录）

```mysql
o_id 整型
o_name 字符类型，变长，宽度为30
o_price 浮点类型，整数最大为10位，小数部分为2位
设置此表中的o_id字段为customers表中c_id字段的外键,更新删除同步
insert into orders values(1,"iphone",5288),(1,"ipad",3299),(3,"mate9",3688),(2,"iwatch",2222),(2,"r11",4400);
```

增删改查题

```mysql
1、返回customers表中，工资大于4000元，或者年龄小于29岁，满足这样条件的前2条记录
mysql> select * from customers where c_salary>4000 or c_age<29 limit 2;

2、把customers表中，年龄大于等于25岁，并且地址是北京或者上海，这样的人的工资上调15%
mysql>  update customers set c_salary = (c_salary*0.15) + c_salary where c_age >=25 and c_city in ('北京','上海');

3、把customers表中，城市为北京的顾客，按照工资降序排列，并且只返回结果中的第一条记录
mysql> select * from customers where c_city='北京' order by c_salary desc limit 1;

4、选择工资c_salary最少的顾客的信息
mysql> select * from customers order by c_salary limit 1;

5、找到工资大于5000的顾客都买过哪些产品的记录明细		

6、删除外键限制			
7、删除customers主键限制
8、增加customers主键限制c_id
```



# MySQL高级-Day02笔记

## **外键（foreign key）**

- **定义**

  让当前表字段的值在另一个表的范围内选择

- **语法**

  ```mysql
  foreign key(参考字段名)
  references 主表(被参考字段名)
  on delete 级联动作
  on update 级联动作
  ```

- **使用规则**

1、主表、从表字段数据类型要一致
2、主表被参考字段 ：KEY的一种，一般为主键

- **示例**

表1、缴费信息表(财务)

```mysql
id   姓名     班级     缴费金额
1   唐伯虎   AID19     300
2   点秋香   AID19     300
3   祝枝山   AID19     300

库  db2
create database db2 charset utf8;
use db2;
create table master(
id int primary key,
name varchar(20),
class char(5),
money decimal(6,2) 
)charset=utf8;

insert into master values(1, '唐伯虎', 'AID19', 300),(2, '秋香','AID19',300),(3,'祝枝山', 'AID19', 300);


```

表2、学生信息表(班主任) -- 做外键关联

```mysql
stu_id   姓名   缴费金额
  1     唐伯虎    300
  2     点秋香    300

create table slave(
stu_id int,
name varchar(20),
money decimal(6,2),
foreign key(stu_id) references master(id) on delete cascade on update cascade
)charset=utf8;

insert into slave values(1, '唐伯虎', 300),(2, '点秋香',300),(3,'祝枝山', 300);




create table slave_2(
stu_id int,
name varchar(20),
money decimal(6,2),
foreign key(stu_id) references master(id) on delete restrict on update restrict
)charset=utf8;


create table slave_3(
stu_id int,
name varchar(20),
money decimal(6,2),
foreign key(stu_id) references master(id) on delete set null on update set null
)charset=utf8;




```

- **删除外键**

```mysql
alter table 表名 drop foreign key 外键名;  (此外键名需查找)
外键名 ：show create table 表名;
删除外键后，desc查看变成了普通索引
```

- **级联动作**

  关联什么字段，那个字段就必须一样。

```mysql
cascade(主表中有的数据，从表才能插入。当主表删除某数据，从表有的也会一样被删除。)
 on delete cascade on update cascade
数据级联删除、更新(参考字段) 
restrict(默认)  可以不用写
从表有相关联记录,不允许主表操作
set null
主表删除、更新,从表相关联记录字段值为NULL
on delete set null on update set null
（若主表要删除一个数据，必须先看看有没有其他级联动作从表，有就得先删除其他从表中的数据，才能删主表的数据，而set null构建的从表中的数据会变成null)
```

- **已有表添加外键**

```mysql
alter table 表名 add foreign key(参考字段) references 主表(被参考字段) on delete 级联动作 on update 级联动作
```



## 嵌套查询(子查询)

定义

把内层的查询结果作为外层的查询条件

语法格式

```mysql
select ... from 表名 where 条件(select ....);
```

示例

```mysql
1、把攻击值小于平均攻击值的英雄名字和攻击值显示出来
  select name, attack from sanguo where attack < (select avg(attack) from sanguo)
2、找出每个国家攻击力最高的英雄的名字和攻击值(子查询)
  select name, attack from sanguo where (country, attack) in(select country ,max(attack) from sanguo group by country) 
 
```



## **多表查询**

**sql脚本资料：join_query.sql**

```mysql
mysql -uroot -p123456
mysql>use db2;
mysql>source /home/tarena/join_query.sql
mysql>show tables -->多出三张表[province,county,city]
```

```mysql
create table if not exists province(
id int primary key auto_increment,
pid int,
pname varchar(15)
)default charset=utf8;

insert into province values
(1, 130000, '河北省'),
(2, 140000, '陕西省'),
(3, 150000, '四川省'),
(4, 160000, '广东省'),
(5, 170000, '山东省'),
(6, 180000, '湖北省'),
(7, 190000, '河南省'),
(8, 200000, '海南省'),
(9, 200001, '云南省'),
(10,200002,'山西省');

create table if not exists city(
id int primary key auto_increment,
cid int,
cname varchar(15),
cp_id int
)default charset=utf8;

insert into city values
(1, 131100, '石家庄市', 130000),
(2, 131101, '沧州市', 130000),
(3, 131102, '廊坊市', 130000),
(4, 131103, '西安市', 140000),
(5, 131104, '成都市', 150000),
(6, 131105, '重庆市', 150000),
(7, 131106, '广州市', 160000),
(8, 131107, '济南市', 170000),
(9, 131108, '武汉市', 180000),
(10,131109, '郑州市', 190000),
(11,131110, '北京市', 320000),
(12,131111, '天津市', 320000),
(13,131112, '上海市', 320000),
(14,131113, '哈尔滨', 320001),
(15,131114, '雄安新区', 320002);

create table if not exists county(
id int primary key auto_increment,
coid int,
coname varchar(15),
copid int
)default charset=utf8;

insert into county values
(1, 132100, '正定县', 131100),
(2, 132102, '浦东新区', 131112),
(3, 132103, '武昌区', 131108),
(4, 132104, '哈哈', 131115),
(5, 132105, '安新县', 131114),
(6, 132106, '容城县', 131114),
(7, 132107, '雄县', 131114),
(8, 132108, '嘎嘎', 131115);
```

- **笛卡尔积**(多表查询交叉，不要使用，大量消耗内存，会损坏磁盘)

```mysql
select 字段名列表 from 表名列表; 
```

- **多表查询**(不提倡)

  多表查询时字段名要写成表名.字段名

```mysql
select 字段名列表 from 表名列表 where 条件;
```

- **示例**

```mysql
1、显示省和市的详细信息
   河北省  石家庄市 
   河北省  廊坊市
   湖北省  武汉市
   select province.pname , city.cname from province,city where province.pid = city.cp_id;

2、显示 省 市 县 详细信息
select province.pname,city.cname,county.coname from province,city,county where province.pid = city.cp_id and 
city.cid = county.copid;
```



## 连接查询

多表查询时字段名要写成表名.字段名

- **内连接（结果同多表查询，显示匹配到的记录）**

````mysql
select 字段名 from  表1 inner join 表2 on 条件 inner join 表3 on 条件;
eg1 : 显示省市详细信息
  select province.pname, city.cname from province inner join city on province.pid = city.cp_id;
  
eg2 : 显示 省 市 县 详细信息
 select province.pname, city.cname , county.coname from province inner join city on province.pid = city.cp_id inner join county on city.cid = county.copid;

  
````

- **左外连接**

以 左表 为主显示查询结果

```mysql
select 字段名 from 表1 left join 表2 on 条件 left join 表3 on 条件;
eg1 : 显示 省 市 详细信息（要求省全部显示）

select province.pname, city.cname from province left join city on province.pid = city.cp_id;
 
```

- **右外连接**

用法同左连接,以右表为主显示查询结果

```mysql
select 字段名 from 表1 right join 表2 on 条件 right join 表3 on 条件;
```

## **数据导入**

==掌握大体步骤==

==source 文件名.sql==

**作用**

把文件系统的内容导入到数据库中
**语法（方式一）**

(若权限不够，就通过chmod 666 文件名  可写-可读-可修改)

load data infile "文件名"
into table 表名
fields terminated by "分隔符"     （每个字段按什么分割）
lines terminated by "\n"  心     （行与行之间按什么分割）
**示例**（后缀是csv的文件才行）
scoretable.csv文件导入到数据库db2的表

```mysql
1、将scoretable.csv放到数据库搜索路径中
	查看数据库搜索路径：
   mysql>show variables like 'secure_file_priv';
      mysql的搜索路径：     /var/lib/mysql-files/
   
   首先将根目录要导入的数据文件复制到数据库的搜索路径中
   Linux: sudo cp /home/tarena/scoreTable.csv /var/lib/mysql-files/
   
  在Linux终端中输入 sudo su --》 cd /var/lib/mysql-files/
-->ls  进行查看是否复制到此处
2、在数据库中创建对应的表（在需要的数据库中创建对应的表来存放）

  create table scoretab(
  rank int,
  name varchar(20),
  score float(5,2),
  phone char(11),
  class char(7)
  )charset=utf8;
3、执行数据导入语句
load data infile '/var/lib/mysql-files/scoreTable.csv'
into table scoretab
fields terminated by ','
lines terminated by '\n';
4、练习
  添加id字段,要求主键自增长,显示宽度为3,位数不够用0填充
  alter table scoretab add id int(3) zerofill primary key auto_increment first;
```

**语法（方式二）**（必须存的要是MySQL语句,然后在库中直接导入）

source 文件名.sql   (最好给出路径)

## **数据导出**

**作用**

将数据库中表的记录保存到系统文件里

**语法格式**

select ... from 表名
into outfile "文件名"
fields terminated by "分隔符"
lines terminated by "分隔符";

**练习**

```mysql
1、把sanguo表中英雄的姓名、攻击值和国家三个字段导出来,放到 sanguo.csv中
以下命令将数据表导出到数据库的搜索路径中
 	 select name,attack,country from sanguo
     into outfile '/var/lib/mysql-files/sanguo.csv' 	 fields terminated by ',' 
     lines terminated by '\n';
通过移动将其放到根目录下（linux下输入：sudo su
-->cd /var/lib/mysql-files/ 再进行操作）
 mv sanguo.csv /home/tarena/.

2、将mysql库下的user表中的 user、host两个字段的值导出到 user2.txt，将其存放在数据库目录下
select user,host from mysql.user 
into outfile '/var/lib/mysql-files/test.csv' 
fields terminated by ' ' 
lines terminated by '\n';

 通过移动将其放到根目录下（linux下输入：sudo su
-->cd /var/lib/mysql-files/ 再进行操作）
 mv test.csv /home/tarena/.
```

**注意**

```
1、导出的内容由SQL查询语句决定
2、执行导出命令时路径必须指定在对应的数据库目录下
```

## **表的复制**

==1、表能根据实际需求复制数据==

==2、复制表时不会把KEY属性复制过来==

**语法**  

```mysql
create table 新表名 select 查询命令;
```

**练习**

```mysql
1、复制sanguo表的全部记录和字段,sanguo2
  	create table sanguo2 select * from country.sanguo
2、复制sanguo表的 id,name,country 三个字段的前3条记录,sanguo4
  create table sanguo4 select id,name,country from country.sanguo limit 3
```

**注意** 

扩展分享-常规分表套路：

用户ID int % 表数量

用户名 ASCII  % 表数量

经典案例：  用户表分表



点赞 -》MVCC 多版本控制 解决方案

version  int 

每次update的时候 version + 1

topic_like, version = select topic_like , version from topic;   

topic_like += 1

while n<3

​	update .......  where version=version  

复制表的时候不会把原有表的 KEY 属性复制过来

**复制表结构**
create table 表名 select 查询命令 where false; 心

## **锁（自动加锁，自动解锁）**

==全程重点，理论和锁分类及特点==

**目的**

解决客户端并发访问的冲突问题

**锁类型分类** 

```
读锁(共享锁)：select 加读锁之后别人不能更改表记录,但可以进行查询
写锁(互斥锁、排他锁)：update加写锁之后别人不能查、不能改
```

**锁粒度分类**

表级锁 ：myisam
行级锁 ：innodb

## 今日作业

1、把 /etc/passwd 文件的内容导入到数据库的表中

```
tarena:x:1000:1000:tarena,,,:/home/tarena:/bin/bash

cp /etc/passwd /home/tarena/    1、将文件复制到根目录下

sudo cp /home/tarena/passwd /var/lib/mysql-files/  
2、将文件复制到mysql路径中

3、查看
 在Linux终端中输入 sudo su --》 cd /var/lib/mysql-files/
-->ls  进行查看是否复制到此处

4、创建对应的表
mysql> create table pwd(
    -> username varchar(20),
    -> password char(1),
    -> uid int,
    -> git int,
    -> comment varchar(50),
    -> homedir varchar(50),
    -> shell varchar(30)
    -> )charset=utf8;

5、执行语句进行导入
mysql> load data infile '/var/lib/mysql-files/passwd' 		   into table pwd 
	   fields terminated by ':' 
	   lines terminated by '\n';
6、完成后可进行查看
```



# **MySQL-Day03笔记**

## **存储引擎**

**定义**

```mysql
处理表的处理器
```

**基本操作**

```mysql
1、查看所有存储引擎
   mysql> show engines;
2、查看已有表的存储引擎
   mysql> show create table 表名;
3、创建表指定
   create table 表名(...)engine=MyISAM,charset=utf8,auto_increment=10000;
4、已有表指定
   alter table 表名 engine=InnoDB;
```

**==常用存储引擎及特点==**

- InnoDB		（目前默认的存储引擎就是InnoDB）

```mysql
1、支持行级锁
2、支持外键、事务、事务回滚
3、表字段和索引同存储在一个文件中
   1、表名.frm ：表结构
   2、表名.ibd : 表记录及索引文件


哈希 -->'123456774561' -->'ADBN' range 3000
密码类型选择： int char varchar text （选其一)
不可能是1和4
char
由于在密码处理上，给用户提交的密码进行散列，根据散列的特点，不论输入多长，输出一定是定长的原理，那么最佳的搭档就是char，varchar虽然也能存，但会有预留出来字段来存放当前字段实际长度，在磁盘存储上有一定的浪费
```

- MyISAM

```mysql
1、支持表级锁
2、表字段和索引分开存储
   1、表名.frm ：表结构
   2、表名.MYI : 索引文件(my index)
   3、表名.MYD : 表记录(my data)
```

- MEMORY

```mysql
1、表记录存储在内存中，效率高
2、服务或主机重启，表记录清除
```

**如何选择存储引擎**

```mysql
MyISAM:
	查询快，如下原因：
    1, 压缩前缀索引 - 加快了查询效率
    2，查询缓存中 由于压缩前缀索引技术，可容纳更多的查询结果
    其他：
    1，count(id) ；提供了一个计数器 

innodb:
	更新快，如下原因:
	1, MVCC多版本控制 导致 查询有耗损
	2，由于本身为行级锁，插入时效率较高（行级锁减少了插入、更新时锁的交换时间【按需执行锁的交换】；类比myisam为表锁，表锁插入、更新时均需执行锁的交换）
	其他：
		事务

具体问题具体分析（实在不知道-->InnoDB） 
1、执行查操作多的表用 MyISAM
2、执行写操作多的表用 InnoDB
3、临时表 ： MEMORY

最终选型： 依据压测结果【请按照实际表结构及索引结构进行有效压测】

```

## **MySQL的用户账户管理**

**开启MySQL远程连接**

```mysql
更改配置文件，重启服务！
1、sudo su
2、cd /etc/mysql/mysql.conf.d
3、cp mysqld.cnf mysqld.cnf.bak
4、vi mysqld.cnf #找到44行左右,加 # 注释
   #bind-address = 127.0.0.1

5、保存退出
6、service mysql restart

vi使用 : 按a ->编辑文件 ->ESC ->shift+: ->wq
```

**添加授权用户**

```mysql
1、用root用户登录mysql
   mysql -uroot -p123456
2、授权
   grant 权限列表 on 库.表 to "用户名"@"%" identified by "密码" with grant option;
3、刷新权限
   flush privileges;
```

**权限列表**

```
all privileges 、select 、insert ... ... 
库.表 ： *.* 代表所有库的所有表
```

**示例**

```mysql
1、添加授权用户work,密码123,对所有库的所有表有所有权限
  mysql>grant all privileges on *.* to 'work'@'%' identified by '123' with grant option;
  mysql>flush privileges;
  
2、添加用户duty,对db2库中所有表有所有权限
	mysql>grant all privileges on db2.* to 'duty'@'%' identified by '123' with grant option;
	mysql>flush privileges;

重启mysql ： service mysqlrestart
查看MySQL的进程：ps aux|gre 'mysqld'
```

## **==事务和事务回滚==**

**事务定义**

```mysql
 一件事从开始发生到结束的过程
```

**作用**

```mysql
确保数据的一致性、准确性、有效性
```

**事务操作**

```mysql
1、开启事务
   mysql>begin; # 方法1
   mysql>start transaction; # 方法2
2、开始执行事务中的1条或者n条SQL命令
3、终止事务
   mysql>commit; # 事务中SQL命令都执行成功,提交到数据库,结束!
   mysql>rollback; # 有SQL命令执行失败,回滚到初始状态,结束!
 
一般在逻辑里使用   pymysql	
```

**==事务四大特性（ACID）==**

- **1、原子性（atomicity）**  (结果：成功或失败)

```
一个事务必须视为一个不可分割的最小工作单元，整个事务中的所有操作要么全部提交成功，要么全部失败回滚，对于一个事务来说，不可能只执行其中的一部分操作
```

- **2、一致性（consistency）**

```
数据库总是从一个一致性的状态转换到另一个一致性的状态
```

- **3、隔离性（isolation）**

```
一个事务所做的修改在最终提交以前，对其他事务是不可见的
```

- **4、持久性（durability）**

```
一旦事务提交，则其所做的修改就会永久保存到数据库中。此时即使系统崩溃，修改的数据也不会丢失
```

**注意**

```mysql
1、事务只针对于表记录操作(增删改)有效,对于库和表的操作无效
2、事务一旦提交结束，对数据库中数据的更改是永久性的
```

## **E-R模型(Entry-Relationship)**

**定义**		

```mysql
E-R模型即 实体-关系 数据模型,用于数据库设计
用简单的图(E-R图)反映了现实世界中存在的事物或数据以及他们之间的关系
```

**实体、属性、关系**

- 实体(相当表)

```mysql
1、描述客观事物的概念
2、表示方法 ：矩形框
3、示例 ：一个人、一本书、一杯咖啡、一个学生
```

- 属性（相当字段）

```mysql
1、实体具有的某种特性
2、表示方法 ：椭圆形
3、示例
   学生属性 ：学号、姓名、年龄、性别、专业 ... 
   感受属性 ：悲伤、喜悦、刺激、愤怒 ...
```

- ==关系（重要）==（相当外键）

```mysql
1、实体之间的联系
表示方法 ：菱形
2、一对一关联(1:1) ：老公对老婆
   A中的一个实体,B中只能有一个实体与其发生关联
   B中的一个实体,A中只能有一个实体与其发生关联
3、一对多关联(1:n) ：父亲对孩子        （经常出现）
   A中的一个实体,B中有多个实体与其发生关联
   B中的一个实体,A中只能有一个与其发生关联
4、多对多关联(m:n) ：兄弟姐妹对兄弟姐妹、学生对课程
   A中的一个实体,B中有多个实体与其发生关联
   B中的一个实体,A中有多个实体与其发生关联
```

**ER图的绘制**

矩形框代表实体,菱形框代表关系,椭圆形代表属性

- 课堂示例（老师研究课题）

```mysql
1、实体 ：教师、课题
2、属性
   教师 ：教师代码、姓名、职称
   课题 ：课题号、课题名
3、关系
   多对多（m:n)
   # 一个老师可以选择多个课题，一个课题也可以被多个老师选
```

- 练习

设计一个学生选课系统的E-R图

```mysql
1、实体：学生、课程、老师
2、属性
3、关系
   学生 选择 课程 (m:n)
   课程 任课 老师 (1:n)
```

==**关系映射实现（重要）**==

```mysql
1:1实现 --> 主外键关联,外键字段添加唯一索引
  表t1 : id int primary key,
          1
  表t2 : t2_id int unique,    unique即代表与1：n的区别
         foreign key(t2_id) references t1(id)
          1
1:n实现 --> 主外键关联
  表t1 : id int primary key,
         1
  表t2 : t2_id int,
         foreign key(t2_id) references t1(id)
         1
         1        
m:n实现(借助中间表):
   t1 : t1_id 
   t2 : t2_id 
   
老婆们					老公们				
id	名字				id	名字	w_id		
1	 女老师1			1	郭小闹	1		
2	 女老师2								
3	 女老师3								
																										
父亲	【一】					孩子	【多】		主键设在多上
ID	name	age				id	name	age	f_id
1	王伟超	32				1	王小超	18	   1
2	祁老师	30				2	王大超	20	   1
						3	  QQ	0.5	   2
	
    
    
父亲	多					孩子	多		
ID	name	age			id	name	age	
1	王伟超	  32		   1  王小超	 18	
2	祁老师	  30		   2  王大超	 20	
						 3	QQ	     18	
						 4	QQ2	     20	
多对多需要借助第三张表来关联

			id	f_id c_id				
			1	 1	   3	（孩子3和父亲1有关系）			
			2	 2	   3	（孩子3和父亲2也有关系）	
			3	 1	   1				
			4	 1	   2				

```

**==多对多实现==**

- 老师研究课题

```mysql
表1、老师表  teacher id[int主键] tname、title
插入数据：
(1, '郭小闹', '牛X')
(2， '王伟超', '牛xx')
insert into teacher values(1, '郭小闹', '牛x'),(2, '王伟超', '牛xx')；

表2、课题表  course  id[int主键],  cname
插入数据：
(1, 'mysql'), (2, 'django'), (3, 'project')

中间表： middle  id tid cid 
```

- 后续

```mysql
1、每个老师都在研究什么课题？
select teacher.tname, course.cname from teacher inner join middle on teacher.id = middle.tid inner join course on course.id = middle.cid;

2、郭小闹在研究什么课题？
select teacher.tname, course.cname from teacher inner join middle on teacher.id = middle.tid inner join course on course.id = middle.cid 
where teacher.tname = '郭小闹';
```

## **==MySQL调优==**

**存储引擎优化**

```mysql
1、读操作多：MyISAM
2、写操作多：InnoDB  (多用于)
```

**索引优化**

```
在 select、where、order by 常涉及到的字段建立索引
```

**SQL语句优化**

```mysql
1、单条查询最后添加 LIMIT 1，停止全表扫描
2、where子句中不使用 != ,否则放弃索引全表扫描
3、尽量避免 NULL 值判断,否则放弃索引全表扫描
   优化前：select number from t1 where number is null;
   优化后：select number from t1 where number=0;
   # 在number列上设置默认值0,确保number列无NULL值
4、尽量避免 or 连接条件,否则放弃索引全表扫描
   优化前：select id from t1 where id=10 or id=20;
   优化后： select id from t1 where id=10 union all 
           select id from t1 where id=20;
5、模糊查询尽量避免使用前置 % ,否则全表扫描
   select name from t1 where name like "c%";
6、尽量避免使用 in 和 not in,否则全表扫描
   优化前：select id from t1 where id in(1,2,3,4);
   优化后：select id from t1 where id between 1 and 4;
7、尽量避免使用 select * ...;用具体字段代替 * ,不要返回用不到的任何字段
```



