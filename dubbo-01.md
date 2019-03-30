# DUBBO

#  架构evolution

## 集中式架构

**Problem**
有**耦合性高，无法水平扩展（集群）**的问题

![img](images/taotao-all-in-one.jpg)

##  分布式架构

按功能进行**垂直拆分**：

![img](images/taotao-vert-split-according-features.jpg)

**Solution**

**分布式架构**能解决集中式架构存在的问题，

**Problem**
但是如果只是根据功能进行拆分，会有需要重复编写同样功能方法的问题。
如上图，两个系统都需要实现根据商品id查询商品的功能

## SOA

**Solution**
可以再进行水平拆分：
把页面控制层Controller单独拆出来，

**业务层和持久层拆出来作为服务层**

![img](images/taotao-hori-split-according-service.jpg)

**Problem**

1. 当服务越来越多，调用服务的URL就越来越**难以管理**
2. 当调用服务量越来越大，很难确定服务需要多少机器支撑，什么时候增加机器

![img](images/taotao-soa.jpg)

> Dubbo就是资源调度和治理中心，用来解决这些问题的



# Java web项目系统间的通信的三种方式

- Webservice： 基于soap(**http + xml**)协议，**效率不高**。not a good choice in self project, 常用于两个公司间的通信。可垮语言垮平台。
- restful：形式：**http+json**, get请求或post请求传递json，URL不带参数，通过路径来描述。用spring中`@pathVarible`从路径中来取值。

| REQUEST METHOD | FUNCTION |
| -------------- | -------- |
| GET            | query    |
| POST           | add      |
| PUT            | update   |
| DELETE         | delete   |

- dubbo：避免服务调用的混乱，有一个统一的平台来==发布、监控、管理服务==。使用socket通信，传递的事二进制，==效率高==。有注册中心来统一监控。