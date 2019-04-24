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
```

# Feign

<https://cloud.spring.io/spring-cloud-netflix/multi/multi_spring-cloud-feign.html>

Feign is a **declarative** RESTFul http client. It makes writing web service clients easier. To use Feign create an interface and annotate it. 

**enable**

```java
@SpringBootApplication
@EnableFeignClients
public class Application {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

}
```

**FeignClient**

```java
@FeignClient(value = "itcast-microservice-item") // 申明这是一个Feign客户端，并且指明服务id
public interface ItemFeignClient {
	@RequestMapping(value = "/item/{id}", method = RequestMethod.GET)
	public Item queryItemById(@PathVariable("id") Long id);

}
```

**use**

```java
    @Autowired
    private ItemFeignClient itemFeignClient;

	@HystrixCommand(fallbackMethod = "queryItemByIdFallbackMethod") // 进行容错处理
	public Item queryItemById(Long id) {
		return this.itemFeignClient.queryItemById(id);
	}
```

# Zuul

**Router and Filter**

<https://cloud.spring.io/spring-cloud-static/Greenwich.RELEASE/multi/multi__router_and_filter_zuul.html>

Routing is an integral part of a microservice architecture. For example, `/` may be mapped to your web application, `/api/users` is mapped to the user service and `/api/shop` is mapped to the shop service. Zuul is a JVM-based router and server-side load balancer from Netflix.

![microservice-arch-without-zuul](images/microservice-arch.png)

**disadvantages**

- 首先，破坏了服务无状态特点。
为了保证对外服务的安全性，我们需要实现对服务访问的权限控制，而开放服务的权限控制机制将会贯穿并污染整个开放服务的业务逻辑，这会带来的最直接问题是，破坏了服务集群中REST API无状态的特点。
从具体开发和测试的角度来说，在工作中除了要考虑实际的业务逻辑之外，还需要额外可续对接口访问的控制处理。

- 其次，无法直接复用既有接口。
当我们需要对一个即有的集群内访问接口，实现外部服务访问时，我们不得不通过在原有接口上增加校验逻辑，或增加一个代理调用来实现权限控制，无法直接复用原有的接口。

面对类似上面的问题，我们要如何解决呢？ 答案是：服务网关！

为了解决上面这些问题，我们需要将**权限控制**这样的东西从我们的服务单元中抽离出去，而最适合这些逻辑的地方就是处于**对外访问最前端的地方**，我们需要一个更强大一些的均衡负载器 -> **服务网关**。

Netflix uses Zuul for the following:

- Authentication
- Insights
- Stress Testing
- Canary Testing
- Dynamic Routing
- Service Migration
- Load Shedding
- Security
- Static Response handling
- Active/Active traffic management

## demo

- dependency
- zuulproxy
- route rules configuration

**dep**

```xml
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-zuul</artifactId>
        </dependency>
        <!-- 导入Eureka服务的依赖 -->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-eureka-server</artifactId>
        </dependency>
```

**zuul proxy**

```java
@EnableZuulProxy
@EnableDiscoveryClient
@SpringBootApplication
public class ZuulApplication {
    public static void main(String[] args) {
        new SpringApplication().run(ZuulApplication.class);
    }
}
```

**route rules**

can user *, regular expression, prefix, etc.

```yml
server:
  port: 6767
spring:
  application:
    name: spring-cloud-microservice-zuul
zuul:
  routes:
    item-service:
      path: /item-service/**
      # url: http://localhost:8081
      service-id: spring-cloud-item-microService
eureka:
  client:
    register-with-eureka: true
    fetch-registry: true
    service-url:
      defaultZone: http://eureka:123456@localhost:6868/eureka/
```

## Zuul filter

![zuul-filter](images/zuul-filter.png)

```java
public class UserLoginZuulFilter extends ZuulFilter {

    @Override
    public boolean shouldFilter() {
        return true; // 该过滤器需要执行
    }

    @Override
    public Object run() { //编写业务逻辑
        RequestContext requestContext = RequestContext.getCurrentContext();
        HttpServletRequest request = requestContext.getRequest();
        String token = request.getParameter("token");
        if(StringUtils.isEmpty(token)){
            requestContext.setSendZuulResponse(false); // 过滤该请求，不对其进行路由
            requestContext.setResponseStatusCode(401); // 设置响应状态码
            return null;
        }
        return null;
    }
```

# spring cloud config

<https://cloud.spring.io/spring-cloud-static/Greenwich.RELEASE/single/spring-cloud.html#_spring_cloud_config>

Spring Cloud Config provides server-side and client-side support for externalized configuration in a distributed system. With the Config Server, you have a central place to manage external properties for applications across all environments. The concepts on both client and server map identically to the Spring `Environment` and `PropertySource` abstractions, so they fit very well with Spring applications but can be used with any application running in any language. 

Config Server是一个可横向扩展、集中式的配置服务器，它用于集中管理应用程序各个环境下的配置，默认使用Git.

![spring-cloud-config](images/spring-cloud-config-arch.png)

**property sources on git server**

该文件的命名规则是：{application}-{profile}.properties

## config server

- dependency
- configure application git uri
- @EnableConfigServer

### config server demo

**dep**
```xml
    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-config-server</artifactId>
        </dependency>
    </dependencies>
```

**git**
```yml
server:
  port: 6688
spring:
  application:
    name: spring-cloud-microservice-config
  cloud:
    config:
      server:
        git:
          uri: https://github.com/jeerychris/microservice-configuration.git
          # username: wshisuifeng
          # password:
          # passphrase: # ssh key
```

**enable**
```java
@EnableConfigServer
@SpringBootApplication
public class ConfigApplication {
    public static void main(String[] args) {
        new SpringApplication().run(ConfigApplication.class);
    }
}
```

### config server test

**rest uri**: `http:/localhost:6688/microservice/dev/master`

```
/{application}/{profile}/[label]
/{application}-{profile}.yml
/{label}/{application}-{profile}.yml
/{application}-{profile}.properties
/{label}/{application}-{profile}.properties
```

其中{label}是指分支，默认是master