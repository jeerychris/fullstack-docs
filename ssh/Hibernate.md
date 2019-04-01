# Hibernate

> A java class persistent open source framework.

## Jars

1. the required.
2. the loggings
3. optional, most common is c3p0

## Configuration

### Alone

|         |         file          | note |
| ------- | :-------------------: | ---- |
| core    | src/hibernate.cfg.xml |      |
| mapping |     aBean.hbn.xml     |      |

### With Spring

```xml
	<!-- 引入外部属性文件=============================== -->
	<context:property-placeholder location="classpath:jdbc.properties"/>
	
	<!-- 配置C3P0连接池=============================== -->
	<bean id="dataSource" class="com.mchange.v2.c3p0.ComboPooledDataSource">
		<property name="driverClass" value="${jdbc.driverClass}"/>
		<property name="jdbcUrl" value="${jdbc.url}"/>
		<property name="user" value="${jdbc.username}"/>
		<property name="password" value="${jdbc.password}"/>
	</bean>
	
	<!-- 开启组件扫描（将类交给SPring管理）================== -->
	<context:component-scan base-package="com.itheima.ssh"/>
	
	<!-- Spring整合Hibernate========================= -->
	<bean id="sessionFactory" class="org.springframework.orm.hibernate5.LocalSessionFactoryBean">
		<property name="dataSource" ref="dataSource"/>
		
		<!-- 配置Hibernate属性 -->
		<property name="hibernateProperties">
			<props>
				<prop key="hibernate.dialect">org.hibernate.dialect.MySQLDialect</prop>
				<prop key="hibernate.show_sql">true</prop>
				<prop key="hibernate.format_sql">true</prop>
				<prop key="hibernate.hbm2ddl.auto">update</prop>
			</props>
		</property>
		
		<!-- 加载映射 -->
		<property name="packagesToScan" value="com.itheima.ssh.domain"/>
	</bean>
	
	<!-- 定义Hibernate模板 -->
	<bean id="hibernateTemplate" class="org.springframework.orm.hibernate5.HibernateTemplate">
		<property name="sessionFactory" ref="sessionFactory"/>
	</bean>
	
	<bean id="transactionManager" class="org.springframework.orm.hibernate5.HibernateTransactionManager">
		<property name="sessionFactory" ref="sessionFactory"/>
	</bean>
	
	<tx:annotation-driven transaction-manager="transactionManager"/>
```

#### Delayed Loading

```xml
<!-- spring's solution for hibernate's delay load -->
    <filter>
        <filter-name>OpenSessionInViewFilter</filter-name>
        <filter-class>org.springframework.orm.hibernate5.support.OpenSessionInViewFilter</filter-class>
    </filter>
    <filter-mapping>
        <filter-name>OpenSessionInViewFilter</filter-name>
        <url-pattern>*.action</url-pattern>
    </filter-mapping>
```





## Persistent class

come close to a database table

## Tables Relationships and Hibernate's solution

### One to Many

### Many to Many

### One to one






