# Spring Security

## Basic

### **dependency**

```xml
<dependency>
    <groupId>org.springframework.security</groupId>
    <artifactId>spring-security-web</artifactId>
</dependency>

<dependency>
    <groupId>org.springframework.security</groupId>
    <artifactId>spring-security-config</artifactId>
</dependency>
```

### **spring-security.xml**

```xml
<!-- 设置页面不登陆也可以访问 -->
<http pattern="/*.html" security="none"/>
<http pattern="/css/**" security="none"/>
<http pattern="/img/**" security="none"/>
<http pattern="/js/**" security="none"/>
<http pattern="/plugins/**" security="none"/>
<http pattern="/seller/add.do" security="none"/>

<!-- 页面的拦截规则    use-expressions:是否启动SPEL表达式 默认是true -->
<http use-expressions="false">
    <!-- 当前用户必须有ROLE_USER的角色 才可以访问根目录及所属子目录的资源 -->
    <intercept-url pattern="/**" access="ROLE_SELLER"/>
    <!-- 开启表单登陆功能 -->
    <form-login  login-page="/shoplogin.html" default-target-url="/admin/index.html" authentication-failure-url="/shoplogin.html" always-use-default-target="true"/>
    <csrf disabled="true"/>
    <headers>
        <frame-options policy="SAMEORIGIN"/>
    </headers>
    <logout/>
</http>

<!-- 认证管理器 -->
<authentication-manager>
    <authentication-provider user-service-ref="userDetailService">
        <password-encoder ref="bcryptEncoder"/>
    </authentication-provider>	
</authentication-manager>

<!-- 认证类 -->
<beans:bean id="userDetailService" class="com.pinyougou.service.UserDetailsServiceImpl">
    <beans:property name="sellerService" ref="sellerService"/>
</beans:bean>

<!-- 引用dubbo 服务 -->
<dubbo:application name="pinyougou-shop-web" />
<dubbo:registry address="zookeeper://192.168.1.254:2181"/>
<dubbo:reference id="sellerService" interface="com.pinyougou.sellergoods.service.SellerService"/>


<beans:bean id="bcryptEncoder" class="org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder"/>
```

### Add user

```java
@RequestMapping("/add")
public Result add(@RequestBody TbSeller seller) {
    //密码加密
    BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder();
    String password = passwordEncoder.encode(seller.getPassword());//加密
    seller.setPassword(password);

    try {
        sellerService.add(seller);
        return new Result(true, "增加成功");
    } catch (Exception e) {
        e.printStackTrace();
        return new Result(false, "增加失败");
    }
}
```

### UserDetailService

```java
/**
 * 认证类
 * @author Administrator
 *
 */
public class UserDetailsServiceImpl implements UserDetailsService {

	
	private SellerService sellerService;
	
	public void setSellerService(SellerService sellerService) {
		this.sellerService = sellerService;
	}

	@Override
	public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
		System.out.println("经过了UserDetailsServiceImpl");
		//构建角色列表
		List<GrantedAuthority> grantAuths=new ArrayList();
		grantAuths.add(new SimpleGrantedAuthority("ROLE_SELLER"));

		//得到商家对象
		TbSeller seller = sellerService.findOne(username);
		if(seller!=null){
			if(seller.getStatus().equals("1")){
				return new User(username,seller.getPassword(),grantAuths);
			}
		}else{
			return null;
		}
	}
}
```

### UI

```html
<form class="sui-form" action="/login" method="post" id="loginform">
    <div class="input-prepend"><span class="add-on loginname"></span>
        <input itype="text" name="username" placeholder="邮箱/用户名/手机号" class="span2 input-xfat">
    </div>
    <div class="input-prepend"><span class="add-on loginpwd"></span>
        <input type="password" name="password" placeholder="请输入密码" class="span2 input-xfat">
    </div>
    <div class="setting">
        <label class="checkbox inline"><input name="m1" type="checkbox" value="2" checked="">自动登录</label>
        <span class="forget">忘记密码？</span>
    </div>
    <div class="logined">
        <a class="sui-btn btn-block btn-xlarge btn-danger" onclick="document:loginform.submit()" target="_blank">登&nbsp;&nbsp;录</a>
    </div>
</form>
```

## BCryptPasswordEncoder

[Reference](<https://www.zhihu.com/question/54720851>)

### VS MD5

- same row code, same 32 bit hash code

- md5 + salt, user managed salt

- md5 decode, huge data mining for simple pwd

**BCrypt**

> 64 bit, system managed salt

### Analyze

```java
public class BCryptPasswordEncoderTest {
    public static void main(String[] args) {
        String pass = "admin";
        BCryptPasswordEncoder bcryptPasswordEncoder = new BCryptPasswordEncoder();
        String hashPass = bcryptPasswordEncoder.encode(pass);
        System.out.println(hashPass);

        boolean f = bcryptPasswordEncoder.matches("admin",hashPass);
        System.out.println(f);

    }
}
```

> 可以看到，每次输出的hashPass 都不一样， 但是最终的f都为 true,即匹配成功。
> 查看代码，可以看到，其实**每次的随机盐，都保存在hashPass中**。