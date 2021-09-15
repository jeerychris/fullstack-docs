# applicationContext.xml configuration
```xml
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
	xmlns:context="http://www.springframework.org/schema/context"
	xsi:schemaLocation="
        http://www.springframework.org/schema/beans 
        http://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/context 
        http://www.springframework.org/schema/context/spring-context.xsd">

	<!-- set base package using spring annotation -->
	<context:component-scan base-package="com.itheima.dao.impl"></context:component-scan>
</beans>
```
## Bean annotation ***@Conponent("name")***
subtypes
- @Service
- @Controller
- @Repository

## Spring DI
1. common
  - @Value("value")
2. Bean
  - @Autowired
  - @Qualifier

  - or @Resource(name="value")
3. others
  - lifecycle
    - @PostConstruct
    - @PreDestroy
  - scope
    - @Singleton
    - @Prototype
    - @Session
    - @GlobalSession
    - @Request

## Spring Unit Test

```java
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration("classpath*:application*.xml")
public class DaoAnnotationTest {

    @Resource(name="depDao")
    IDepDao depDao;

    @Test
    public void listTest(){
        System.out.println(depDao.getList());
    }
}
```

