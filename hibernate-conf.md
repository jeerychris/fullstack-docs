# Alone

|         |         file          | note |
| ------- | :-------------------: | ---- |
| core    | src/hibernate.cfg.xml |      |
| mapping |     aBean.hbn.xml     |      |

## hibernate.cfg.xml

```xml

```

## mapping resources

> ***1 Customer to N LinkMan, 1 BaseDict to N Customer***

### customer.hbm.xml

```xml
<hibernate-mapping>
    <class name="com.itheima.crm.domain.Customer" table="cst_customer">
        <id name="cust_id" column="cust_id">
            <generator class="native"/>
        </id>

        <property name="cust_name" column="cust_name"/>
        <!-- <property name="cust_source" column="cust_source"/>
        <property name="cust_industry" column="cust_industry"/>
        <property name="cust_level" column="cust_level"/> -->
        <property name="cust_phone" column="cust_phone"/>
        <property name="cust_mobile" column="cust_mobile"/>
        <property name="cust_image" column="cust_image"/>

        <!-- 配置客户与字典的多对一的映射 -->
        <many-to-one name="baseDictSource" class="com.itheima.crm.domain.BaseDict" column="cust_source"/>
        <many-to-one name="baseDictIndustry" class="com.itheima.crm.domain.BaseDict" column="cust_industry"/>
        <many-to-one name="baseDictLevel" class="com.itheima.crm.domain.BaseDict" column="cust_level"/>

        <!-- 配置与联系人的关系映射 -->
        <set name="linkMans" cascade="delete" inverse="true">
            <key column="lkm_cust_id"/>
            <one-to-many class="com.itheima.crm.domain.LinkMan"/>
        </set>
    </class>
</hibernate-mapping>
```

### linkMan

```xml
<hibernate-mapping>
    <class name="com.itheima.crm.domain.LinkMan" table="cst_linkman">
        <id name="lkm_id" column="lkm_id">
            <generator class="native"/>
        </id>

        <property name="lkm_name" column="lkm_name"/>
        <property name="lkm_gender" column="lkm_gender"/>
        <property name="lkm_phone" column="lkm_phone"/>
        <property name="lkm_mobile" column="lkm_mobile"/>
        <property name="lkm_email" column="lkm_email"/>
        <property name="lkm_qq" column="lkm_qq"/>
        <property name="lkm_position" column="lkm_position"/>
        <property name="lkm_memo" column="lkm_memo"/>

        <many-to-one name="customer" class="com.itheima.crm.domain.Customer" column="lkm_cust_id"/>
    </class>
</hibernate-mapping>
```

### BaseDict

```xml
<hibernate-mapping>
    <class name="com.itheima.crm.domain.BaseDict" table="base_dict">
        <id name="dict_id" column="dict_id">
            <generator class="uuid"/>
        </id>

        <property name="dict_type_code" column="dict_type_code"/>
        <property name="dict_type_name" column="dict_type_name"/>
        <property name="dict_item_name" column="dict_item_name"/>
        <property name="dict_item_code" column="dict_item_code"/>
        <property name="dict_sort" column="dict_sort"/>
        <property name="dict_enable" column="dict_enable"/>
        <property name="dict_memo" column="dict_memo"/>
        <!-- 字典和客户是一对多的关系，如果查询字典数据的时候，不需要查询客户的数据，所以在字典端可以不用配置客户相关内容。 -->
    </class>
</hibernate-mapping>
```



# With Spring

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

## Delayed Loading

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