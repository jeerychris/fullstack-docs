# CREATE

# UPDATE

```SQL
update table set sex= '男', name='张三' where id = 1 ;       --正确

update table set sex= '男' and name='张三' where id = 1 ;    --错误
```

# JOIN

```sql
select * from emp e left join emp_role er on e.uuid=er.empuuid left join role_menu rm on er.roleuuid=rm.roleuuid where e.uuid=9
```

