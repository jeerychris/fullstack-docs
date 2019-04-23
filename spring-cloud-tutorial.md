# Spring Cloud

<https://cloud.spring.io/spring-cloud-static/Dalston.SR5/single/spring-cloud.html>

Spring Cloud focuses on providing good out of box experience for typical use cases and extensibility mechanism to cover others.

- Distributed/versioned configuration
- Service registration and discovery        Eureka,Zookeeper
- Routing
- Service-to-service calls
- Load balancing
- Circuit Breakers
- Distributed messaging

# Eureka 

/u`ri:ke/, 尤里卡

**Eureka** is the **Netflix** Service Discovery Server and Client. The server can be configured and deployed to be highly available, with each server replicating state about the registered services to the others.

Based on **REST Service**, two part, server and client, 

![service-reg-and-discovery](images/service-discovery.png)

1. 服务提供者将服务注册到注册中心
2. 服务消费者通过注册中心查找服务
3. 查找到服务后进行调用（这里就是无需硬编码url的解决方案）
4. 服务的消费者与服务注册中心保持心跳连接，一旦服务提供者的地址发生变更时，注册中心会通知服务消费者

![eureka](images/eureka-server-client.png)

Eureka包含两个组件：Eureka Server和Eureka Client。

Eureka Server提供服务注册服务，各个节点启动后，会在Eureka Server中进行注册，这样EurekaServer中的服务注册表中将会存储所有可用服务节点的信息，服务节点的信息可以在界面中直观的看到。

Eureka Client是一个java客户端，用于简化与Eureka Server的交互，客户端同时也就别一个内置的、使用轮询(round-robin)负载算法的负载均衡器。

在应用启动后，将会向Eureka Server发送心跳,默认周期为30秒，如果Eureka Server在多个心跳周期内没有接收到某个节点的心跳，Eureka Server将会从服务注册表中把这个服务节点移除(默认90秒)。

Eureka Server之间通过复制的方式完成数据的同步，Eureka还提供了客户端缓存机制，即使所有的Eureka Server都挂掉，客户端依然可以利用缓存中的信息消费其他服务的API。综上，Eureka通过**心跳检查**、**客户端缓存**等机制，确保了系统的高可用性、灵活性和可伸缩性。

## demo

OrderServie -> ItemService

- dependency
- server
- service provider configure
- service consumer configure
- databind problem
- eureka anthentication
    - server
    - service provider and consumer, 服务 registry or fetch 时设置账户信息 `http://user:pwd@host:port/path`

```xml
    <!-- 导入Spring Cloud的依赖管理 -->
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-dependencies</artifactId>
                <version>Dalston.SR3</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <dependencies>
        <!-- 导入Eureka服务的依赖 -->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-eurekakkkkkkkkkkkk-server</artifactId>
        </dependency>
        <!-- 安全认证 -->
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-security</artifactId>
		</dependency>
    </dependencies>
```

**server**

```yml
server:
  port: 6868
spring:
  application:
    name: spring-cloud-microservice-eureka
eureka:
  client:
    register-with-eureka: false
    fetch-registry: false
    serviceUrl:
      defaultZone: http://127.0.0.1:${server.port}/eureka/
security:
  basic:
    enabled: true
  user:
    name: eureka
    password: 123456
```
```java
@EnableEurekaServer
@SpringBootApplication
public class EurekaServerApplication {
    public static void main(String[] args) {
        new SpringApplication().run(EurekaServerApplication.class);
    }
}
```

**service provide**

```yml
server:
  port: 8081
spring:
  application:
    name: spring-cloud-item-microService
eureka:
  client:
    fetch-registry: true
    register-with-eureka: true
    service-url:
      defaultZone: http://eureka:123456@localhost:6868/eureka/
  instance:
    prefer-ip-address: true # registy ip to server
```
```java
@EnableDiscoverClient
@SpringBootApplication
public class ItemApplication {
    public static void main(String[] args) {
        new SpringApplication().run(ItemApplication.class);
    }
}
```

**service consumer**

```yml
server:
  port: 8082
spring:
  application:
    name: spring-cloud-order-microservice
service:
  item:
    url: http://localhost:8081/items/
eureka:
  client:
    register-with-eureka: false
    fetch-registry: true
    service-url:
      defaultZone: http://eureka:123456@localhost:6868/eureka/
```

```java
// Rest communication
@Autowired
private RestTemplate restTemplate;

@Autowired
private DiscoveryClient discoveryClient;

public Item queryItemById(Long id) {
    String serviceId = "spring-cloud-item-microService";
    List<ServiceInstance> instances = discoveryClient.getInstances(serviceId);
    if (instances == null || instances.size() == 0) {
        return null;
    } else {
        ServiceInstance instanceInfo = instances.get(0);
        String url = "http://" + instanceInfo.getHost() + ":" + instanceInfo.getPort() + "/items/" + id;
        return restTemplate.getForObject(url, Item.class);
    }
}
```

```java
@EnableDiscoverClient
@SpringBootApplication
public class OrderApplication {
    public static void main(String[] args) {
        new SpringApplication().run(OrderApplication.class);
    }
}
```

**xml problem**
```
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-eureka-server</artifactId>
    <exclusions>
        <exclusion>
            <artifactId>jackson-dataformat-xml</artifactId>
            <groupId>com.fasterxml.jackson.dataformat</groupId>
        </exclusion>
    </exclusions>
</dependency>
```

## eureka cluster

server registry each other

**server 1**

```yml
server:
  port: 6868
spring:
  application:
    name: spring-cloud-microservice-eureka
eureka:
  client:
    register-with-eureka: true
    fetch-registry: true
    serviceUrl:
      defaultZone: http://eureka:123456@127.0.0.1:${server.port}/eureka/
security:
  basic:
    enabled: true
  user:
    name: eureka
    password: 123456
```

**server 2**

```yml
server:
  port: 6869
spring:
  application:
    name: spring-cloud-microservice-eureka
eureka:
  client:
    register-with-eureka: true
    fetch-registry: true
    serviceUrl:
      defaultZone: http://eureka:123456@127.0.0.1:${server.port}/eureka/
security:
  basic:
    enabled: true
  user:
    name: eureka
    password: 123456
```

# Ribbon

client end load balance

![ribbon-arch](images/Ribbon-arch.png)

## demo

```java
    @Bean
    @LoadBalanced
    public RestTemplate getRestTemplate() {
        return new RestTemplate(new OkHttp3ClientHttpRequestFactory());
    }
```

```java
@Autowired
private RestTemplate restTemplate;

public Item queryItemById(Long id) {
    String serviceId = "spring-cloud-item-microService";
    String url = "http://" + serviceId + "/items/" + id;
    return restTemplate.getForObject(url, Item.class);
}
```

**IDEA Tips**: edit run configrations to run multiple instance

# Hystrix

## 雪崩效应 avalanche

在微服务架构中通常会有多个服务层调用，基础服务的故障可能会导致级联故障，进而造成整个系统不可用的情况，这种现象被称为服务雪崩效应。服务雪崩效应是一种因“服务提供者”的不可用导致“服务消费者”的不可用,并将不可用逐渐放大的过程。

如果下图所示：A作为服务提供者，B为A的服务消费者，C和D是B的服务消费者。A不可用引起了B的不可用，并将不可用像滚雪球一样放大到C和D时，雪崩效应就形成了。

![avalanche](images/service-avalanche.png)

## hystrx demo

```xml
		<dependency>
			<groupId>org.springframework.cloud</groupId>
			<artifactId>spring-cloud-starter-hystrix</artifactId>
		</dependency>
```


```java
	@HystrixCommand(fallbackMethod = "queryItemByIdFallbackMethod") // 进行容错处理
	public Item queryItemById(Long id) {
		return this.itemFeignClient.queryItemById(id);
	}

    public Item queryItemByIdFallbackMethod(Long id){ // 请求失败执行的方法
		return new Item(id, "查询商品信息出错!", null, null, null);
	}
```

```java
@EnableHystrix
@EnableDiscoveryClient
@SpringBootApplication
public class OrderApplication {
	
	public static void main(String[] args) {
		SpringApplication.run(OrderApplication.class, args);
	}
}