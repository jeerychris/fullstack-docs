# Spring Data

<https://spring.io/projects/spring-data>

> Spring Data’s mission is to **provide a familiar and consistent, Spring-based programming model** for **data access** while still **retaining the special traits of the underlying data store**.
>
> It makes it easy to use data access technologies, **relational and non-relational databases, map-reduce frameworks, and cloud-based data services**. This is an umbrella project which contains many subprojects that are specific to a given database. The projects are developed by working together with many of the companies and developers that are behind these exciting technologies.

## Features

- Powerful repository and custom object-mapping abstractions
- Dynamic query derivation from repository method names
- Implementation domain base classes providing basic properties
- Support for transparent auditing (created, last changed)
- Possibility to integrate custom repository code
- **Easy Spring integration via JavaConfig and custom XML namespaces**
- Advanced integration with Spring MVC controllers
- Experimental support for **cross-store persistence**

# Main modules

Spring Data Commons - Core Spring concepts underpinning every Spring Data module.

Spring Data JDBC - Spring Data repository support for JDBC.

Spring Data JDBC Ext - Support for database specific extensions to standard JDBC including support for Oracle RAC fast connection failover, AQ JMS support and support for using advanced data types.

**Spring Data JPA** - Spring Data repository support for JPA.

Spring Data MongoDB - Spring based, object-document support and repositories for MongoDB.

**Spring Data Redis** - Easy configuration and access to Redis from Spring applications.

Spring Data REST - Exports Spring Data repositories as hypermedia-driven RESTful resources.

**Spring Data for Apache Solr** - Easy configuration and access to Apache Solr for your search oriented Spring applications.

## Community modules

**Spring Data Elasticsearch** - Spring Data module for Elasticsearch.



# Spring Data JPA

```java
public interface JpaRepository<T, ID extends Serializable>
		extends PagingAndSortingRepository<T, ID>, QueryByExampleExecutor<T> {

public interface PagingAndSortingRepository<T, ID extends Serializable> extends CrudRepository<T, ID> {

public interface CrudRepository<T, ID extends Serializable> extends Repository<T, ID> {
    
public interface Repository<T, ID extends Serializable> {
}
```

## 查询方式

```java
public class RoncooUser {
	private int id;
	private String name;
	private Date createTime;
}

public interface RoncooUserLogDao extends JpaRepository<RoncooUserLog, Integer> {
	@Query(value = "select u from RoncooUserLog u where u.userName=?1")
	List<RoncooUserLog> findByUserName(String userName);

	List<RoncooUserLog> findByUserNameAndUserIp(String string, String string2);

	Page<RoncooUserLog> findByUserName(String userName, Pageable pageable);
}
```

### @Query

### 通过解析方法名创建查询

```java
    public interface UserRepository extends Repository<User, Long> {
      List<User> findByEmailAddressAndLastname(String emailAddress, String lastname);
    }
```
我们将使用`JPA criteria` `API`创建一个查询，但本质上这转换为以下查询：

框架在进行方法名解析时，会先把方法名多余的前缀截取掉，比如 find、findBy、read、readBy、get、getBy，然后对剩下部分进行解析。并且如果方法的最后一个参数是 Sort 或者 Pageable 类型，也会提取相关的信息，以便按规则进行排序或者分页查询。

```sql
select u from User u where u.emailAddress = ?1 and u.lastname = ?2
```

Spring Data  JPA  将执行属性检查并遍历属性表达式中描述的嵌套属性。下面是  JPA  支持的关键字的概述，以及包含该关键字的方法的本质含义。

### SQL关键词想细介绍

| 关键词            | Demo                                                      | JPQL 语句片段                                                |
| ----------------- | --------------------------------------------------------- | ------------------------------------------------------------ |
| And               | findByLastnameAndFirstname                                | … where x.lastname = ?1 and x.firstname = ?2                 |
| Or                | findByLastnameOrFirstname                                 | … where x.lastname = ?1 or x.firstname = ?2                  |
| Is,Equals         | findByFirstname, findByFirstnameIs, findByFirstnameEquals | … where x.firstname = ?1                                     |
| Between           | findByStartDateBetween                                    | … where x.startDate between ?1 and ?2                        |
| LessThan          | findByAgeLessThan                                         | … where x.age < ?1                                           |
| LessThanEqual     | findByAgeLessThanEqual                                    | … where x.age ⇐ ?1                                           |
| GreaterThan       | findByAgeGreaterThan                                      | … where x.age > ?1                                           |
| GreaterThanEqual  | findByAgeGreaterThanEqual                                 | … where x.age >= ?1                                          |
| After             | findByStartDateAfter                                      | … where x.startDate > ?1                                     |
| Before            | findByStartDateBefore                                     | … where x.startDate < ?1                                     |
| IsNull            | findByAgeIsNull                                           | … where x.age is null                                        |
| IsNotNull,NotNull | findByAge(Is)NotNull                                      | … where x.age not null                                       |
| Like              | findByFirstnameLike                                       | … where x.firstname like ?1                                  |
| NotLike           | findByFirstnameNotLike                                    | … where x.firstname not like ?1                              |
| StartingWith      | findByFirstnameStartingWith                               | … where x.firstname like ?1 (parameter bound with appended %) |
| EndingWith        | findByFirstnameEndingWith                                 | … where x.firstname like ?1 (parameter bound with prepended %) |
| Containing        | findByFirstnameContaining                                 | … where x.firstname like ?1 (parameter bound wrapped in %)   |
| OrderBy           | findByAgeOrderByLastnameDesc                              | … where x.age = ?1 order by x.lastname desc                  |
| Not               | findByLastnameNot                                         | … where x.lastname <> ?1                                     |
| In                | findByAgeIn(Collection<Age> ages)                         | … where x.age in ?1                                          |
| NotIn             | findByAgeNotIn(Collection<Age> age)                       | … where x.age not in ?1                                      |
| True              | findByActiveTrue()                                        | … where x.active = true                                      |
| False             | findByActiveFalse()                                       | … where x.active = false                                     |
| IgnoreCase        | findByFirstnameIgnoreCase                                 | … where UPPER(x.firstame) = UPPER(?1)                        |