# Basic

 ## Jars

> ${unzip}/app/struts2-blank.war

## Action class

> extends ==ActionSupport==
> or implements Action

## [struts.xml][]

> Using **wild cards**

![struts.xml action conf](images/struts-action-conf.bmp)

# Dissection

##  class StrutsPrepareAndExecute

## Configuration files and loading sequence

## struts's boot sequence

![struts-boot-sequence][]

# Data Wrapper

## Model Driven for Class

```java
public class UserAction3 extends ActionSupport implements ModelDriven<User>{
	// 模型驱动使用的对象：前提必须手动提供对象的实例
	private User user = new User(); // 手动实例化User.
	@Override
	// 模型驱动需要使用的方法:
	public User getModel() {
		return user;
	}
	@Override
	public String execute() throws Exception {
		System.out.println(user);
		return NONE;
	}
}
```



## Attribute Driven for Complex

> Product is a java bean

```java
public class ProductAction1 extends ActionSupport {
	
	private List<Product> products;
	// 提供集合的set方法:
	public void setProducts(List<Product> products) {
		this.products = products;
	}
	public List<Product> getProducts() {
		return products;
	}

	@Override
	public String execute() throws Exception {
		for (Product product : products) {
			System.out.println(product);
		}
		return NONE;
	}	
}
```

# The Logic Input View

> Struts's **Exception** dumping
> 
**SET**:  ActionError、FieldError、ActionMessage
**GET**: `<s:actionError>`

```java
public class UserAction extends ActionSupport implements ModelDriven<User>{
	// 接收数据:
	private User user = new User();
	@Override
	public User getModel() {
		return user;
	}
	
	public String login(){
		System.out.println(user);
		// 调用业务层:
		UserService userService = new UserServiceImpl();
		User existUser = userService.login(user);
		// 根据结果页面跳转：
		if(existUser == null){
			// 登录失败
			// ActionError、FieldError、ActionMessage
			this.addActionError("用户名或密码错误！");
			return LOGIN;
		}else{
			// 登录成功
			// ActionContext.getContext().getSession().put("existUser", "existUser");
			ServletActionContext.getRequest().getSession().setAttribute("existUser", existUser);
			return SUCCESS;
		}
	}
}
```



# OGNL and ValueStack

> Object Graph Navigation Language, much stronger than EL

## OGNL features

-  调用对象的方法
-  调用对象的静态方法
-  表达式串联
-  访问ActionContext和OgnlContext数据

## ValueStack

###  值栈的概述

>  ValueStack：是一个接口，实现类**OgnlValueStack**。是数据的中转站，贯穿了整个Action，有一个Action的实例，就会创建一个ValueStack对象。

###  值栈的内部结构

-  Root ：CompoundRoot，就是一个ArrayList。
-  Context ：OgnlContext，就是一个Map, 存与对象request, session, application etc.

### ActionContex & ServletActionContext

> ``

```java
ActionContext.getContext().getValueStack().push("user", user);
```



# Struts-taglib

```jsp
<%@ taglib uri="/struts-tags" prefix="s"%>
```

> use often

```jsp
<s:if />
<s:property value="" />
<s:debug />
<s:actionError />
```



# Interceptor 

> **Filter**, for request, even a html request
>
> **Interceptor**, only for action

![Struts2-Architecture][]

[struts.xml]: ./struts2-conf.md
[struts-boot-sequence]:  images/struts-boot-sequence.bmp
[Struts2-Architecture]: images/Struts2-Architecture.png