# Web.xml

```xml
<!-- Struts2的核心过滤器 -->
    <filter>
        <filter-name>struts2</filter-name>
        <filter-class>org.apache.struts2.dispatcher.ng.filter.StrutsPrepareAndExecuteFilter</filter-class>
    </filter>
    <filter-mapping>
        <filter-name>struts2</filter-name>
        <url-pattern>/*</url-pattern>
    </filter-mapping>
```



# struts.xml

```xml
<struts>
    <!-- 配置Struts2的常量 -->
    <constant name="struts.action.extension" value="action"/>
    <!-- 配置Struts2中所上传的文件的总大小 -->
    <constant name="struts.multipart.maxSize" value="5242880"/>

    <package name="crm" extends="struts-default" namespace="/">
        <interceptors>
            <interceptor name="privilegeInterceptor" class="com.itheima.crm.web.interceptor.PrivilegeInterceptor"/>
        </interceptors>

        <global-results>
            <result name="login">/login.jsp</result>
        </global-results>

        <action name="user_*" class="userAction" method="{1}">
            <result name="login">/login.jsp</result>
            <result name="success" type="redirect">/index.jsp</result>

            <interceptor-ref name="privilegeInterceptor">
                <param name="excludeMethods">regist,login</param>
            </interceptor-ref>
            <interceptor-ref name="defaultStack"/>
        </action>

    </package>
</struts>

```

